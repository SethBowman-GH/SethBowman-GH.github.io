Project Overview
Objective: Developed an interactive executive dashboard to analyze global sales performance for a fictional retail giant (Contoso). The goal was to identify high-margin product categories and underperforming store locations to improve net profit.

Tech Stack: Power BI Desktop, Power Query, DAX.

Key Features & Methodology
Data Modeling (Star Schema):

Designed a robust star schema connecting a central Fact table (Sales) to four Dimension tables (Products, Customers, Stores, Date).

Ensured 1-to-Many relationships to enable accurate filtering and drill-down capabilities.

Advanced DAX Calculations:

Total Profit Margin %: Calculated to track profitability, not just raw revenue.

Year-Over-Year (YoY) Growth: Created time-intelligence measures to compare 2026 performance vs. 2025.

Active Store Analysis: Used the Store Status column to filter out closed locations for accurate current-state forecasting.

Data Transformation (ETL):

Cleaned customer demographic data to standardize "Occupation" and "Country" fields for accurate segmentation.
