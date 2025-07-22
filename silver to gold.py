# Databricks notebook source
# MAGIC %md
# MAGIC #Single column name transformation

# COMMAND ----------

dbutils.fs.ls('/mnt/silver/SalesLT/')

# COMMAND ----------

dbutils.fs.ls('/mnt/gold/')

# COMMAND ----------

df_address = spark.read.format('delta').load('/mnt/silver/SalesLT/Address')
display(df_address)

# COMMAND ----------

def rename_col_to_snake_case(df):
    """
    Convert column names from PascalCase or camelCase to snake_case in a PySpark DataFrame.

    Args:
        df (DataFrame): The input DataFrame with columns to be renamed.

    Returns:
        DataFrame: A new DataFrame with column names converted to snake_case.
    """

    # Get the column names
    col_names = df.columns

    # Dict to hold old and new names
    dict_map = {}

    for old_col_name in col_names:
        # Convert column name from PascalCase or camelCase to snake_case
        new_col_name = "".join([
            "_" + char.lower() if (
                char.isupper()              # Check if the current character is uppercase
                and idx > 0                 # Ensure it's not the first character
                and not old_col_name[idx - 1].isupper()  # Ensure the previous character is not uppercase
            ) else char.lower()  # Convert character to lowercase
            for idx, char in enumerate(old_col_name)
        ]).lstrip("_")  # Remove any leading underscore

        # Avoid renaming to an existing column name
        if new_col_name in dict_map.values():
            raise ValueError(f"Duplicate column name found after renaming: '{new_col_name}'")

        # Map the old column name to the new column name
        dict_map[old_col_name] = new_col_name

    # Rename columns using the mapping
    for old_col_name, new_col_name in dict_map.items():
        df = df.withColumnRenamed(old_col_name, new_col_name)

    return df

# COMMAND ----------

df_address = rename_col_to_snake_case(df_address)
display(df_address)


# COMMAND ----------

# MAGIC %md
# MAGIC # Duplicate check for each df

# COMMAND ----------

def check_duplicates(df) -> bool:
    """
    Check if the DataFrame has duplicate rows.
    
    Parameters:
        df (DataFrame): Input PySpark DataFrame.
        
    Returns:
        has_duplicates (bool): True if duplicates exist, False otherwise.
    """
    original_count = df.count()
    dedup_count = df.dropDuplicates().count()
    
    if original_count > dedup_count:
        print(f"Duplicates found: {original_count - dedup_count}")
        return True
    else:
        print(" No duplicate rows found.")
        return False

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('mnt/silver/SalesLT'):
    table_name.append(i)

for i in dbutils.fs.ls('mnt/silver/SalesLT'):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

for table in table_name:
    path = f'/mnt/silver/SalesLT/{table}'
    print(path)
    try:
        df = spark.read.format('delta').load(path)
        print(check_duplicates(df))
    except Exception as e:
        print(f"Error loading table {table}: {e}")

# COMMAND ----------

# MAGIC %md
# MAGIC # Col name transformation for each table

# COMMAND ----------

for name in table_name:
    path = '/mnt/silver/SalesLT/' + str(name)
    print(path)
    try:
        df = spark.read.format('delta').load(path)
        df = rename_col_to_snake_case(df)
        output_path = '/mnt/gold/SalesLT/' + str(name) + '/'
        df.write.mode('overwrite').format('delta').save(output_path)
    except Exception as e:
        print(f"Error loading table {table}: {e}")