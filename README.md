
# E-Commerce Lakehouse Pipeline

An end-to-end Data Engineering project using Databricks, PySpark,
Delta Lake, SQL, and GitHub.

## 1. Project Overview

This project builds a production-inspired e-commerce data pipeline
that ingests structured and semi-structured data, transforms it
through Bronze, Silver, and Gold layers, validates data quality,
and produces analytics-ready datasets.

## 2. Business Objectives

- Integrate customer, product, order, payment, and seller data.
- Build reliable and reusable data ingestion pipelines.
- Clean and validate source data.
- Support incremental processing and safe pipeline reruns.
- Create analytical tables for business reporting.

## 3. Technology Stack

- Databricks
- Apache Spark and PySpark
- Delta Lake
- SQL
- Python
- Git and GitHub

## 4. Architecture

Source Data -> Bronze -> Silver -> Gold -> Analytics

- **Bronze:** Raw data ingestion with source-file and ingestion metadata.
- **Silver:** Cleaned, standardized, and validated data.
- **Gold:** Dimensional data model with fact tables, dimension tables, and business KPI tables.
- **Analytics:** SQL-based business analysis and reporting.
  
## 5. Data Sources

The project uses the public Olist Brazilian E-Commerce dataset.

Dataset page: [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

The dataset contains historical e-commerce data covering customers, orders, order items, payments, reviews, products, sellers, and geolocation.

The source files were downloaded and processed through the Bronze, Silver, and Gold layers.

## 6. Repository Structure

- docs/: Architecture and project documentation.
- data/: Local source data; raw files are excluded from Git.
- notebooks/: Databricks development notebooks.
- src/: Reusable Python and PySpark modules.
- sql/: Validation and analytical SQL queries.
- tests/: Automated tests.

## 7. Project Status

Current phase: Environment setup and repository initialization.

## 8. Engineering Practices

Planned practices include data quality checks, incremental loads,
deduplication, idempotent processing, logging, testing, and
version control.

## 9. Disclaimer

This is an educational portfolio project using public historical
data and simulated event batches. It is not a live production
e-commerce system.
