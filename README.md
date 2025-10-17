# 🚕 AWS Data Engineering Project — NYC Taxi Trip Analysis

## 📘 Overview
An end-to-end AWS Data Engineering pipeline using the NYC Taxi dataset.  
Built with **AWS S3, Glue, Athena, and QuickSight**, this project processes millions of taxi trip records to extract insights on demand patterns, revenue, and tipping behavior.

## 🧱 Architecture
<img width="760" height="508" alt="nyc-taxi-trip-architecture drawio" src="https://github.com/user-attachments/assets/0734d676-c9d5-45f7-abde-5d440600bc40" />


## ⚙️ Services Used
- **Amazon S3:** Data Lake (Raw + Curated Zones)
- **AWS Glue Crawler:** Schema discovery for raw & cleaned data
- **AWS Glue ETL (PySpark):** Data cleaning and transformation
- **AWS Athena:** SQL analysis on curated data
- **AWS QuickSight:** Dashboard visualizations
- **AWS IAM:** Access & permissions

## 📊 Key Insights
| Metric | Observation |
|--------|--------------|
| Peak Hours | 8–9 AM, 6–8 PM |
| Avg Fare | $16 per trip |
| Tip % | 18% (Credit), 0% (Cash) |

## 📂 Project Structure
- glue-etl/ → Glue PySpark ETL script
- athena-queries/ → SQL queries for analysis
- dashboard/ → QuickSight screenshots


## 💡 How to Reproduce
1. Create two S3 buckets: `raw-zone` and `curated-zone`
2. Use AWS Glue Crawler to register schema
3. Run ETL job to clean and transform
4. Crawl cleaned data
5. Query using Athena
6. Visualize using QuickSight

## 🧑‍💻 Author
**Abhishek S P**  
Data Engineer | AWS | PySpark | SQL  
📧 spabhishek67@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/spabhishek) | [GitHub](https://github.com/Abhisheksp2002)
