# Databricks notebook source
# MAGIC %md
# MAGIC # Single table column transformation
# MAGIC

# COMMAND ----------

dbutils.fs.ls('mnt/bronze/SalesLT')

# COMMAND ----------

dbutils.fs.ls('mnt/silver/')

# COMMAND ----------

df_address = spark.read.format('parquet').load('/mnt/bronze/SalesLT/Address/Address.parquet')
display(df_address)

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

df_address = df_address.withColumn("ModifiedDate", date_format(from_utc_timestamp(df_address['ModifiedDate'].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))

# COMMAND ----------

display(df_address)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transforming date for each table

# COMMAND ----------

table_name = []
for i in dbutils.fs.ls('mnt/bronze/SalesLT/'):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------


for i in table_name:
    path = '/mnt/bronze/SalesLT/' + i + '/' + i +'.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))
    
    output_path = '/mnt/silver/SalesLT/' + i + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

