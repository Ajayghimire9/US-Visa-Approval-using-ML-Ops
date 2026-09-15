import pandas as pd

from us_visa.entity.estimator import TargetValueMapping
from visaops.train import train


def test_target_mapping_matches_offline_contract(tmp_path):
    frame = pd.DataFrame(
        {
            "case_id": list(range(40)),
            "employees": list(range(40)),
            "continent": ["Asia", "Europe"] * 20,
            "case_status": ["Certified", "Denied"] * 20,
        }
    )
    source = tmp_path / "input.csv"
    frame.to_csv(source, index=False)
    report = train(source, tmp_path / "model")
    assert report["label_mapping"] == TargetValueMapping()._asdict()
    assert report["test_rows"] == 8
