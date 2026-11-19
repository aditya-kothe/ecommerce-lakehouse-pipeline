# Gold Layer Documentation

## 1. Project Overview

The Gold layer is the final layer of the Medallion Architecture in this Databricks E-Commerce Lakehouse project.

It transforms cleaned Silver layer data into business-ready dimensional models and aggregated KPI reporting tables.

The primary objective is to support business analytics, reporting, and decision-making using SQL and PySpark.

### Technology Stack

- **Cloud/Data Platform:** Databricks Free Edition
- **Processing:** Apache Spark / PySpark
- **Query Language:** SQL
- **Storage Format:** Delta Tables
- **Dataset:** Brazilian E-Commerce (Olist)
- **Architecture:** Medallion Architecture (Bronze → Silver → Gold)

## 2. Medallion Architecture

The project follows three data-processing layers:

### Bronze Layer
- Stores the raw source datasets.
- Preserves the original source data for downstream processing.
- Contains customer, order, product, seller, payment, review, and geolocation data.

### Silver Layer
- Contains cleaned and prepared datasets.
- Handles data quality checks and transformations.
- Provides structured tables for Gold layer processing.

### Gold Layer
- Contains dimensional models consisting of fact and dimension tables.
- Implements business analytics and KPI calculations.
- Provides reusable reporting tables for business analysis.

### Architecture Flow

Bronze → Silver → Gold

Raw Data → Cleaned Data → Business-Ready Data
