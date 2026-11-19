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

## 3. Gold Dimensional Model

The Gold layer follows a dimensional modelling approach using fact tables and dimension tables.

### 3.1 Dimension Tables

| Table | Grain | Description |
|---|---|---|
| gold_dim_customers | One row per customer_unique_id | Stores customer-level information and location attributes |
| gold_dim_products | One row per product_id | Stores product details and product categories |
| gold_dim_sellers | One row per seller_id | Stores seller information and geographic attributes |
| gold_dim_date | One row per calendar date | Stores date attributes for time-based analysis |

### 3.2 Fact Tables

| Table | Grain | Description |
|---|---|---|
| gold_fact_orders | One row per order_id | Stores order-level information, status and lifecycle dates |
| gold_fact_order_items | One row per order_id and order_item_id | Stores individual product items, prices and freight values |
| gold_fact_payments | One row per order_id and payment_sequential | Stores payment transactions and payment values |
| gold_fact_reviews | One row per order_id and review_id | Stores customer review scores and review information |

### 3.3 Fact and Dimension Relationships

The Gold dimensional model connects business events to descriptive dimensions through surrogate keys.

Key relationships include:

- Orders → Customers using customer_key.
- Order Items → Products using product_key.
- Order Items → Sellers using seller_key.
- Orders and Order Items → Date using date_key fields.
- Payments → Orders using order_id.
- Reviews → Orders using order_id.

Customer mapping is performed through the following relationship:

silver_orders.customer_id → silver_customers.customer_id → customer_unique_id → gold_dim_customers.customer_unique_id → customer_key.

This mapping ensures that multiple customer records belonging to the same actual customer are associated with one customer dimension record.

### 3.4 Important Grain Considerations

- The grain of a fact table determines what one row represents.
- An order can contain multiple order items.
- An order can have multiple payment records.
- Review identifiers may repeat across different orders.
- Therefore, the correct composite grain must be considered when joining and aggregating fact tables.

These grain definitions help prevent duplicate counting and incorrect business metrics.

## 4. Gold KPI Reporting Tables

The Gold layer includes five reusable KPI reporting tables designed to support business analytics and reporting.

### 4.1 Monthly KPI – gold_monthly_kpi

**Grain:** One row per year and month.

Metrics:
- Total orders
- Total items sold
- Total product revenue
- Total freight
- Average order value
- Delivered orders

### 4.2 Payment KPI – gold_payment_kpi

**Grain:** One row per payment type.

Metrics:
- Total payment transactions
- Distinct orders
- Total payment value
- Average payment value
- Payment percentage contribution

### 4.3 Order Status KPI – gold_order_status_kpi

**Grain:** One row per order status.

Metrics:
- Total orders
- Order percentage

### 4.4 Customer KPI – gold_customer_kpi

**Grain:** One overall customer summary row.

Metrics:
- Total customers
- One-time customers
- Repeat customers
- Average orders per customer
- Repeat customer percentage

### 4.5 Review KPI – gold_review_kpi

**Grain:** One overall review summary row.

Metrics:
- Total reviews
- Average review score
- Positive reviews (scores 4–5)
- Negative reviews (scores 1–2)
- Neutral reviews (score 3)
- Positive review percentage

## 5. Gold Layer Validation

The Gold layer was validated through:

- Row-count validation for all dimension and fact tables.
- Foreign-key integrity checks.
- Silver-to-Gold measure reconciliation.
- KPI reporting table validation.
- Business metric reconciliation against analytical SQL queries.

All 13 Gold tables passed the final row-count validation.

### Gold Layer Summary

| Category | Number of Tables |
|---|---:|
| Dimension tables | 4 |
| Fact tables | 4 |
| KPI reporting tables | 5 |
| **Total** | **13** |
