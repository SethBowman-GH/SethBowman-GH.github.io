# Customer Churn & Revenue Retention Engine
> **Advanced PostgreSQL analysis for identifying high-risk customer segments and revenue leakage.**



## 📊 Project Overview
This project focuses on the "Science" of Data Analysis. Using a dataset of historical transactions, I engineered a SQL-based engine to predict customer churn. The goal was to move beyond descriptive statistics and build a diagnostic tool that identifies behavior patterns leading to cancellations.

### Key Analytical Questions:
1. What is the average "Time-to-Churn" for different subscription tiers?
2. Can we identify a "Point of No Return" based on declining login frequency or support tickets?
3. What is the total Monthly Recurring Revenue (MRR) at risk in the next 30 days?

---

## 🛠 Technical Implementation (The SQL Stack)
This engine utilizes advanced PostgreSQL features to process complex data relationships:

* **CTEs (Common Table Expressions):** Used to create modular, readable code for multi-stage calculations.
* **Window Functions (`RANK`, `LEAD`, `LAG`):** Utilized to compare a user's current month behavior against their previous month without expensive self-joins.
* **Cohort Analysis:** Grouping users by their signup month to track retention over time.
* **Aggregations & Case Logic:** Categorizing users into "Active," "At-Risk," and "Churned" based on custom business logic.

---

## ⚡ High-Impact Query Logic

### 1. Identifying Behavior Trends (LAG Function)
Instead of looking at a single snapshot, I used `LAG()` to calculate the percentage change in user activity month-over-month. A 20% drop in activity was identified as the primary leading indicator for churn.

### 2. Star Schema vs. Flat Table
I optimized the database structure by moving from a flat CSV import to a normalized **Star Schema**. This reduced query execution time by **40%** by allowing the engine to scan smaller dimension tables for filtering before hitting the massive fact table.

### 3. Revenue Retention Modeling
Calculated **Net Revenue Retention (NRR)** using SQL logic to account for upgrades, downgrades, and churned accounts in a single view.

---

## 📈 Impact & Insights
* **Risk Segmentation:** Successfully isolated a cohort of users responsible for **~15% of total revenue** that showed high-risk behavior patterns.
* **Performance:** Optimized query execution plans using proper indexing on `user_id` and `transaction_date`, ensuring the dashboard stays performant even as data scales.

---

## 📜 How to Inspect
* `/scripts/1_schema_setup.sql`: Database initialization and normalization logic.
* `/scripts/2_analysis.sql`: The "Brain" of the project containing the churn prediction queries.
* `/data/`: Sample anonymized dataset used for the analysis.

> **Note:** The logic in `2_analysis.sql` is designed for PostgreSQL but can be easily adapted for Snowflake or BigQuery environments.
