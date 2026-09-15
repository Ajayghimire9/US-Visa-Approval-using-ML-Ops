# VisaOps

Historical classification pipeline.

VisaOps studies classification on a historical visa dataset. The maintained offline baseline runs independently of the original MongoDB and AWS infrastructure, making its assumptions and outputs easier to reproduce.

## Run locally

Use Python 3.11 or newer in a virtual environment.

```bash
pip install -r requirements-portfolio.txt
python -m visaops.train --data notebook/Visadataset.csv
```

## Design decisions

A ColumnTransformer handles numerical and categorical columns inside one fitted pipeline; unknown categories are accepted during inference.

The label mapping is explicit: Certified=0 and Denied=1. The legacy UI now uses that same mapping.

The legacy transformation stage resamples training data only. The held-out population is left unchanged for evaluation.

Training is a command-line operation; the unauthenticated HTTP training endpoint has been removed. Legacy AWS deployment is manually triggered.

## Technology

Python, pandas, scikit-learn, joblib; legacy FastAPI, MongoDB and AWS integrations.

## Validation

Run `python -m pytest tests -q` from the repository root. CI runs the maintained test suite and lint checks. Tests use local fixtures or mocks and do not deploy cloud resources.

## Scope and limitations

The dataset contains historical decisions and potentially biased proxies. Outputs are research predictions, not immigration advice or a basis for real eligibility decisions. Balanced accuracy and per-class metrics do not establish fairness. The cloud path has separate dependencies and requires configured credentials.
