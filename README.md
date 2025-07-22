# 🚀 End-to-End Data Engineering Project on Microsoft Azure 

## Overview
This solution showcases a fully automated data platform on Microsoft Azure that takes on‑premises transactional data through a modern ETL pipeline, applies medallion‑style transformations, and dynamically creates database objects.

---

## 🎯 Business Objective

Enable organizations to:

- Modernize legacy SQL Server workflows  
- Automate daily data ingestion and transformation  
- Ensure data quality through standardized Bronze‑Silver‑Gold layers  

---

## 🛠️ Tech Stack

| Layer        | Technology                                     |
|--------------|------------------------------------------------|
| Ingestion    | Azure Data Factory (ADF), Self-Hosted IR       |
| Storage      | Azure Data Lake Storage Gen2 (ADLS)            |
| Processing   | Azure Databricks (PySpark)                     |
| Querying     | Azure Synapse Analytics (Serverless SQL)       |
| Visualization| Power BI                                       |
| Security     | Azure Key Vault, Azure Active Directory        |
| Versioning   | Git + GitHub                                   |

---

## Architecture



<img width="3520" height="1570" alt="Azure end to end" src="https://github.com/user-attachments/assets/23835b74-4656-4c38-8c24-3887e47d0a96" />



---

## ⚙️ Approach

1. **Ingestion**  
   - Configure Self‑Hosted Integration Runtime in a VM to simulate on-prem data source and pull tables from SQL Server.  
   - Parameterize pipelines for dynamic, scale‑out ingestion.  
   - ▶️ [Watch Setup & Ingestion in Azure Data Factory](https://youtu.be/GvwC8Uj5L2g)

2. **Medallion Architecture (Bronze–Silver–Gold) Layers**  
   - **Bronze:** Raw data landing in Parquet format in ADLS.  
   - **Silver:** Cleaned & conformed Delta tables via Databricks notebooks.  
   - **Gold:** Aggregated, analytics‑ready Delta tables exposed via Synapse views.  
   - ▶️ [Watch Medallion Architecture and Transformation Flow](https://youtu.be/vDO5o7TdLqE)

3. **Processing with Databricks (PySpark)**  
   - Use notebooks to handle schema evolution, filtering, joins, and aggregations.  
   - Store curated data in Delta Lake format and register Delta tables.  
   - ▶️ [Watch Databricks Processing & Transformation](https://youtu.be/wR5JvF6uj1c)

4. **Automation & Orchestration**  
   - Trigger pipelines on schedule using ADF.  
   - Execute Databricks notebooks via ADF activity chains.

5. **Data Warehousing & Serving**  
   - Use Azure Synapse Serverless SQL Pools to create views on Gold Delta tables in ADLS.  
   - Expose curated data to BI tools.

6. **Security & Governance**
   

   <img width="1279" height="633" alt="kv_ss" src="https://github.com/user-attachments/assets/c7413a38-7e21-45f7-b535-fc97e17ddacd" />


   - Manage credentials and keys securely with Azure Key Vault.  
   - Apply RBAC using Azure Active Directory.

