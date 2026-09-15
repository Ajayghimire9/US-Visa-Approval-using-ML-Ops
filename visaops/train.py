"""Reproducible offline baseline independent of AWS and MongoDB."""

import argparse
import hashlib
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def train(source, output):
    frame = pd.read_csv(source)
    if "case_status" not in frame or frame.case_status.isna().any():
        raise ValueError("Expected non-null case_status")
    y = frame.case_status.map({"Certified": 0, "Denied": 1})
    if y.isna().any() or y.nunique() != 2:
        raise ValueError("Expected Certified and Denied labels")
    x = frame.drop(columns=["case_status", "case_id"], errors="ignore")
    train_x, test_x, train_y, test_y = train_test_split(
        x, y, stratify=y, test_size=0.2, random_state=42
    )
    numeric = train_x.select_dtypes(include="number").columns.tolist()
    categorical = train_x.columns.difference(numeric).tolist()
    transformer = ColumnTransformer(
        [
            (
                "numeric",
                make_pipeline(SimpleImputer(strategy="median"), StandardScaler()),
                numeric,
            ),
            (
                "category",
                make_pipeline(
                    SimpleImputer(strategy="most_frequent"),
                    OneHotEncoder(handle_unknown="ignore"),
                ),
                categorical,
            ),
        ]
    )
    model = make_pipeline(
        transformer,
        LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42),
    )
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    report = {
        "label_mapping": {"Certified": 0, "Denied": 1},
        "balanced_accuracy": float(balanced_accuracy_score(test_y, pred)),
        "classification_report": classification_report(
            test_y, pred, output_dict=True, zero_division=0
        ),
        "train_rows": len(train_x),
        "test_rows": len(test_x),
        "source_sha256": hashlib.sha256(Path(source).read_bytes()).hexdigest(),
    }
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, out / "model.joblib")
    (out / "metrics.json").write_text(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="notebook/Visadataset.csv")
    p.add_argument("--output", default="artifacts/offline")
    a = p.parse_args()
    print(json.dumps(train(a.data, a.output), indent=2))
