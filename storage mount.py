# Databricks notebook source
dbutils.fs.mount(
    source="wasbs://bronze@advwsa.blob.core.windows.net/",
    mount_point="/mnt/bronze",
    extra_configs={"fs.azure.account.key.advwsa.blob.core.windows.net": dbutils.secrets.get('advw_scope', 'adlskey')}
)

# COMMAND ----------

dbutils.fs.mount(
    source="wasbs://silver@advwsa.blob.core.windows.net/",
    mount_point="/mnt/silver",
    extra_configs={"fs.azure.account.key.advwsa.blob.core.windows.net": dbutils.secrets.get('advw_scope', 'adlskey')}
)

# COMMAND ----------

dbutils.fs.mount(
    source="wasbs://gold@advwsa.blob.core.windows.net/",
    mount_point="/mnt/gold",
    extra_configs={"fs.azure.account.key.advwsa.blob.core.windows.net": dbutils.secrets.get('advw_scope', 'adlskey')}
)

# COMMAND ----------

dbutils.fs.ls('mnt/bronze/SalesLT/')

# COMMAND ----------

dbutils.fs.ls('mnt/silver/')
dbutils.fs.ls('mnt/gold/')