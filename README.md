# Credit Portfolio Optimization & Default Prediction Platform

> **End-to-end portfolio project** demonstrating senior-level Data Science, Data Engineering, and MLOps skills applied to credit risk - covering default prediction, model explainability, pipeline orchestration, and production-grade serving infrastructure.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Airflow](https://img.shields.io/badge/Airflow-2.x-017CEE?logo=apache-airflow)
![MLflow](https://img.shields.io/badge/MLflow-Tracking%20%26%20Registry-0194E2?logo=mlflow)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![LightGBM](https://img.shields.io/badge/LightGBM-Gradient%20Boosting-9ACD32)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Table of Contents

- [Overview](#overview)
- [Skills & Concepts Demonstrated](#skills--concepts-demonstrated)
- [Tech Stack](#tech-stack)
- [Architecture Overview](#architecture-overview)
- [Data Policy](#data-policy)
- [Quickstart](#quickstart)
- [Project Structure](#project-structure)
- [Key Design Decisions](#key-design-decisions)
- [Documentation](#documentation)

---

## Overview

This platform is built on the **[Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk)** dataset - a multi-table, real-world credit dataset covering applicant demographics, credit bureau history, previous loan behavior, and installment patterns.

The system demonstrates the full lifecycle of a credit risk model:

1. **Ingestion & data engineering** - joining multiple source tables, handling imbalanced data, feature engineering from behavioral history.
2. **Default prediction** - binary classification with calibrated probability outputs suitable for scorecard-style decisions.
3. **Portfolio optimization** - threshold selection, expected loss estimation, risk-return tradeoffs at portfolio level.
4. **Model monitoring** - concept drift detection, PSI tracking, and automated retraining triggers.

This is not intended as a production system. It is a structured portfolio exercise designed to demonstrate depth across the full DS/DE stack in a regulated-domain context.

---

## Skills & Concepts Demonstrated

| Area | Details |
|---|---|
| **Credit Risk Modeling** | PD (Probability of Default) estimation, scorecard design, calibration |
| **Feature Engineering** | Multi-table joins, aggregation features, behavioral ratios, bureau feature extraction |
| **ML Modeling** | LightGBM, XGBoost, logistic regression baseline, stacking |
| **Model Explainability** | SHAP values, feature importance, partial dependence plots |
| **Imbalanced Data** | SMOTE, class weighting, threshold optimization (F-beta, KS statistic) |
| **Pipeline Orchestration** | DAG design with Apache Airflow, multi-step dependencies, scheduling |
| **Experiment Tracking** | MLflow runs, parameter logging, model registry, artifact versioning |
| **Model Serving** | Batch scoring pipeline + lightweight REST API (FastAPI) |
| **Data Quality & Governance** | Schema validation, null/outlier handling, data contracts |
| **Monitoring** | PSI (Population Stability Index), feature drift, performance degradation alerts |
| **Software Engineering** | Modular design, unit & integration testing, synthetic fixtures, CI-ready structure |

---

## Tech Stack

| Layer | Tools |
|---|---|
| **Modeling** | LightGBM, XGBoost, scikit-learn, imbalanced-learn |
| **Explainability** | SHAP |
| **Feature Engineering** | pandas, numpy, feature-engine |
| **Orchestration** | Apache Airflow 2.x |
| **Experiment Tracking** | MLflow |
| **Model Serving** | FastAPI (batch + online scoring) |
| **Data Validation** | Great Expectations / Pandera |
| **Monitoring** | Evidently AI (drift & PSI) |
| **Testing** | pytest |
| **Infrastructure** | Docker Compose (local), Makefile |

---

## Architecture Overview

```
Home Credit Raw Tables (bureau, previous_application, installments, etc.)
        │
        v
┌──────────────────────────┐
│  Ingestion & Validation   │  <- Airflow DAG + Pandera schemas
└────────────┬─────────────┘
             │
             v
┌──────────────────────────┐
│   Feature Engineering     │  <- Aggregations, behavioral ratios, bureau features
└────────────┬─────────────┘
             │
             v
┌──────────────────────────┐
│   Model Training          │  <- LightGBM + MLflow tracking
│   (CV + Calibration)      │
└────────────┬─────────────┘
             │
        ┌────┴────┐
        v         v
┌──────────┐  ┌──────────────┐
│  Batch   │  │  API Serving │  <- FastAPI / scoring endpoint
│ Scoring  │  │              │
└──────────┘  └──────────────┘
             │
             v
┌──────────────────────────┐
│  Monitoring & Drift       │  <- Evidently AI + alerting
└──────────────────────────┘
```

---

## Data Policy

| What | Status |
|---|---|
| Source code, DAGs, configs | Versioned |
| Tests & synthetic fixtures | Versioned |
| Documentation | Versioned |
| Raw CSVs, model binaries | Git-ignored |
| Credentials / secrets | Git-ignored |

Raw data must be downloaded manually from [Kaggle](https://www.kaggle.com/c/home-credit-default-risk) and placed in `data/raw/`.

---

## Quickstart

```bash
# 1. Clone and set up environment
git clone <repo-url> && cd <repo>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Start infrastructure (Airflow + MLflow)
docker compose up -d

# 3. Add raw data (download from Kaggle manually)
#    Place CSVs in data/raw/

# 4. Run tests
make test

# 5. Trigger the ingestion DAG
make run-ingestion
```

---

## Project Structure

```
│   .env.example
│   .gitignore
│   develop.ipynb
│   docker-compose.yml
│   Dockerfile.api
│   Makefile
│   pyproject.toml
│   requirements.txt
│
├── airflow/
│   ├── dags/
│   │   ├── data_ingestion_dag.py
│   │   ├── data_preparation_dag.py
│   │   ├── monitoring_dag.py
│   │   ├── scoring_dag.py
│   │   └── training_dag.py
│   └── plugins/
│
├── api/                         # FastAPI serving layer
│   ├── app.py
│   ├── model_loader.py
│   └── schemas.py
│
├── configs/                     # Environment-specific configuration
│   ├── base.yaml
│   ├── dev.yaml
│   ├── model_config.yaml
│   └── prod.yaml
│
├── data/
│   ├── raw/                     # Home Credit CSVs (git-ignored)
│   ├── processed/               # Intermediate outputs (git-ignored)
│   └── features/                # Feature sets (git-ignored)
│
├── docs/                        # Project documentation
│   ├── airflow_dags.md
│   ├── architecture.md
│   ├── assumptions_and_constraints.md
│   ├── business_case.md
│   ├── data_dictionary_template.md
│   ├── governance.md
│   ├── implementation_plan_6_weeks.md
│   ├── model_card_template.md
│   ├── roadmap.md
│   └── testing_strategy.md
│
├── notebooks/                   # Exploratory analysis & model development
│   ├── 01_eda.md
│   ├── 02_data_quality.md
│   ├── 03_feature_engineering.md
│   ├── 04_model_baselines.md
│   ├── 05_model_explainability.md
│   └── 06_threshold_portfolio_strategy.md
│
├── quality/                     # Data quality & monitoring
│   ├── evidently/               # Drift detection reports
│   └── great_expectations/      # Schema validation & checkpoints
│       ├── checkpoints/
│       └── expectation_suites/
│
├── scripts/                     # Standalone execution scripts
│   ├── generate_reports.py
│   ├── register_model.py
│   ├── run_score.py
│   └── run_train.py
│
├── src/                         # Core source code
│   ├── config.py
│   ├── logging_config.py
│   ├── evaluation/              # Metrics, calibration, thresholding
│   ├── features/                # Multi-table aggregations & feature building
│   ├── inference/               # Batch scoring & prediction service
│   ├── ingestion/               # Raw data loading & registry
│   ├── monitoring/              # Drift, PSI & alerting
│   ├── pipelines/               # End-to-end pipeline orchestration
│   ├── preprocessing/           # Cleaning & preparation
│   ├── training/                # Model training (baseline + boosting)
│   └── utils/                   # I/O helpers, path management
│
└── tests/                       # Automated tests
    ├── fixtures/                 # Synthetic test data
    ├── integration/              # API health & import checks
    └── unit/                    # Schema, config & unit tests
```

---

## Key Design Decisions

- **Multi-table feature engineering:** The dataset's complexity (7+ joined tables) simulates real data warehouse environments. Feature aggregation logic is separated from modeling to enforce reusability and testability.
- **Calibrated probability outputs:** Raw classifier scores are calibrated (Platt / isotonic) to produce reliable PD estimates suitable for expected loss calculations - a standard requirement in risk contexts.
- **Threshold optimization beyond accuracy:** Default classification uses KS statistic and F-beta optimization rather than naive 0.5 threshold, reflecting real credit decisioning trade-offs.
- **PSI monitoring built in:** Population Stability Index tracking is included from day one, since distribution shift is the dominant failure mode in credit models deployed over time.
- **Batch + API serving:** Demonstrates both the offline scoring pipeline (for portfolio-level decisions) and an online serving pattern (for real-time applications).

---

## Documentation

- [`docs/implementation_plan_6_weeks.md`](docs/implementation_plan_6_weeks.md) - Phased delivery plan
- [`docs/testing_strategy.md`](docs/testing_strategy.md) - Testing approach and maintainability rationale
- [`docs/assumptions_and_constraints.md`](docs/assumptions_and_constraints.md) - Scope, limitations, and design choices
