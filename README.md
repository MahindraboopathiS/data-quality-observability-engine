# Data Quality & Pipeline Monitoring System

## Overview

This project builds an end-to-end **data quality monitoring system** designed to ensure the reliability and integrity of analytics pipelines. It detects anomalies, tracks data health over time, and provides visibility into pipeline performance through automated checks and dashboards.

The system uses a real-world transactional dataset to simulate how production data pipelines are monitored in modern analytics environments.

---

## Dataset

This project uses the **Online Retail II dataset from the UCI Machine Learning Repository.

* Contains **1M+ transactions** from a UK-based online retailer ([UCI Machine Learning Repository][1])
* Covers **Dec 2009 – Dec 2011** ([UCI Machine Learning Repository][2])
* Includes:

  * Invoice number
  * Product (StockCode)
  * Quantity
  * Price
  * Customer ID
  * Country ([UCI Machine Learning Repository][2])

The dataset includes **missing values and anomalies**, making it ideal for data quality projects.

---

## Objectives

* Identify and detect data quality issues in pipelines
* Build automated validation checks using SQL
* Monitor data health through dashboards
* Improve trust in analytics outputs

---

## Methodology

### 1. Data Quality Framework

Validation categories:

* **Completeness** → Missing values
* **Uniqueness** → Duplicate records
* **Validity** → Invalid values (negative price/quantity)
* **Consistency** → Metric mismatches

---

### 2. SQL Validation Checks

Detect:

* Missing Customer IDs
* Duplicate invoices
* Negative quantities or prices
* Cancellation inconsistencies

---

### 3. Monitoring System

* Store results in `data_quality_logs`
* Track failures over time
* Assign severity levels

---

### 4. Visualization

Dashboard includes:

* Errors over time
* Error type distribution
* Data health score

---

## Tech Stack

* SQL (core validation logic)
* Python (ETL + automation)
* SQLite (database)
* Dashboard: Streamlit / Tableau / Amazon QuickSight

---

## Project Structure

```bash
data-quality-project/
│
├── data/                     # Dataset + database
├── scripts/                  # ETL scripts
├── data_quality/             # Validation logic
├── dashboard/                # Visualization
├── docs/                     # Documentation
└── README.md
```

---

## Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/data-quality-project.git
cd data-quality-project
```

---

### Step 2: Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## Download Dataset

### Option A: Manual Download (Recommended)

1. Go to:
   https://archive.ics.uci.edu/dataset/502/online+retail+ii

2. Download:

```text
online_retail_II.xlsx
```

---

### Step 4: Create data folder

```bash
mkdir data
```

---

### Step 5: Move dataset into project

Place the file here:

```text
data/online_retail_II.xlsx
```

---

## Run the Pipeline

### Step 1: Load raw data

```bash
python scripts/load_data.py
```

Output:

```text
data/Pipeline.db
```

This step:

* Reads Excel file
* Cleans column names
* Loads into SQLite

---

### Step 2: Transform data

```bash
python scripts/transform_data.py
```

Creates:

* `raw_transactions`
* `transactions`
* `customers`
* `products`

---

### Step 3: Run data quality checks

```bash
python data_quality/run_checks.py
```

Example output:

```text
Missing Customers: 243007
Invalid Price: 6207
Invalid Quantity: 3457
```

---

### Step 4: (Optional) Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

## Expected Outcomes

* Automated detection of data issues
* Historical tracking of data quality
* Dashboard for monitoring pipeline health
* Increased trust in analytics

---

## Impact

This project demonstrates:

* Data pipeline reliability engineering
* SQL-based validation systems
* Monitoring and observability
* Business-ready data quality reporting

These skills directly align with real-world analytics systems used at companies like Amazon.

---

## Future Improvements

* Schedule automated pipeline runs
* Integrate cloud storage (S3)
* Add warehouse layer (Redshift)
* Properly implement AI-generated anomaly explanations

---

## Contact

Feel free to reach out for collaboration or feedback.

[1]: https://archive-beta.ics.uci.edu/dataset/502/online%2Bretail%2Bii?utm_source=chatgpt.com "Online Retail II - UCI Machine Learning Repository"
[2]: https://www.archive.ics.uci.edu/ml/datasets/Online%20Retail%20II?utm_source=chatgpt.com "UCI Machine Learning Repository"
