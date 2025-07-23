# 🚀 End-to-End Data Engineering Project on Microsoft Azure 

## Overview
This solution showcases a fully automated data platform on Microsoft Azure that takes on‑premises transactional data through a modern ETL pipeline, applies medallion‑style transformations, and dynamically creates database objects.

---

## 🎯 Business Objective

Enable organizations to:
Absolutely! Here’s a more detailed and professional version of that “Business Objective” section, tailored for GitHub and aimed at recruiters or technical stakeholders:

---

## 🎯 Business Objective (Elaborated)

This project addresses the common challenges organizations face when dealing with fragmented, on-premises SQL Server data systems. The primary goals of the solution are:

* **Modernize Legacy SQL Server Workflows**
  Organizations often rely on outdated SQL Server environments with manual data movement processes, limited scalability, and high maintenance overhead. This project demonstrates how to **lift and shift** legacy SQL Server systems to a **cloud-native, scalable Azure architecture**, enabling seamless integration, modern tooling, and long-term maintainability.

* **Automate Daily Data Ingestion and Transformation**
  Manual ETL jobs are error-prone and time-consuming. This solution showcases how **Azure Data Factory** and **Databricks** can be orchestrated to create a **fully automated data pipeline**. It dynamically ingests tables from a simulated on-prem source, applies transformations using a Medallion (Bronze-Silver-Gold) architecture, and ensures that the data is always up-to-date without manual intervention.

* **Ensure Data Quality Through Standardized Medallion Layers**
  By applying the **Medallion architecture**, this solution ensures clear separation of raw, cleaned, and aggregated data:

  * **Bronze Layer** captures raw ingested data.
  * **Silver Layer** applies schema enforcement, validation, and normalization.
  * **Gold Layer** prepares refined, business-ready data models for analytics and reporting.

  This structure enforces **data quality, traceability, and reusability**, making it easier for data teams and business users to build reliable insights.

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
   - [![Ingestion - ADF](http://img.youtube.com/vi/GvwC8Uj5L2g/0.jpg)](https://youtu.be/GvwC8Uj5L2g)


2. **Medallion Architecture (Bronze–Silver–Gold) Layers**  
   - **Bronze:** Raw data landing in Parquet format in ADLS.  
   - **Silver:** Cleaned & conformed Delta tables via Databricks notebooks.  
   - **Gold:** Aggregated, analytics‑ready Delta tables exposed via Synapse views.  
   - [![Medallion Architecture](http://img.youtube.com/vi/vDO5o7TdLqE/0.jpg)](https://youtu.be/vDO5o7TdLqE)

3. **Processing with Databricks (PySpark)**  
   - Use notebooks to handle schema evolution, filtering, joins, and aggregations.  
   - Store curated data in Delta Lake format and register Delta tables.  
   - [![Databricks Processing](http://img.youtube.com/vi/wR5JvF6uj1c/0.jpg)](https://youtu.be/wR5JvF6uj1c)

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

