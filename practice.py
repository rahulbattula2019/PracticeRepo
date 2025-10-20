import snowflake.connector
import pymysql
import pandas as pd

# Step 0: Extract data from MySQL and export to CSV
try:
    mysqlconn = pymysql.connect(
        host='mysql-rfam-public.ebi.ac.uk',
        port=4497,
        user='rfamro',
        database='Rfam'
    )
    query = 'SELECT * FROM family'
    
    results = pd.read_sql_query(query, mysqlconn)
    csv_path = "/workspaces/PracticeRepo/output.csv"
    results.to_csv(csv_path, index=False, header=False)
    
    print(f"MySQL data exported successfully to {csv_path}")
    
except Exception as e:
    print(f"Failed to extract data from MySQL: {e}")
finally:
    if 'mysqlconn' in locals() and mysqlconn.open:
        mysqlconn.close()

# Step 1: Connect to Snowflake and create DB/Schema/Table, then load data
# After exporting CSV from MySQL...

try:
    conn = snowflake.connector.connect(
        user="Madhu13",
        password="Madhu@9908754818",
        account="ekrbhne-fa26232",
        warehouse="COMPUTE_WH",
        database="TRAININWITHSQL",
        schema="sales"
    )
    print("Snowflake connection successful!")

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS TRAININGDB")
    print("Database 'TRAININGDB' checked/created successfully.")

    cursor.execute("USE DATABASE TRAININGDB")
    cursor.execute("CREATE SCHEMA IF NOT EXISTS RFAM")
    print("Schema 'RFAM' checked/created successfully.")
    cursor.execute("USE SCHEMA RFAM")

    create_table_sql = """ 
    CREATE TABLE IF NOT EXISTS FAMILY(
        rfam_acc VARCHAR(8) NOT NULL,
        rfam_id VARCHAR(40) NOT NULL,
        auto_wiki NUMBER(10,0),
        description VARCHAR(75),
        author VARCHAR(100),
        seed_source VARCHAR(100),
        gathering_cutoff NUMBER(5, 2),
        trusted_cutoff NUMBER(5, 2),
        noise_cutoff NUMBER(5, 2),
        comment VARCHAR(10000),
        previous_id VARCHAR(100),
        cmbuild VARCHAR(100),
        cmcalibrate VARCHAR(100),
        cmsearch VARCHAR(100),
        num_seed NUMBER(38, 0),
        num_full NUMBER(38, 0),
        num_genome_seq NUMBER(38, 0),
        num_refseq NUMBER(38, 0),
        type VARCHAR(100),
        structure_source VARCHAR(100),
        number_of_species NUMBER(38, 0),
        number_3d_structures NUMBER(10,0),
        num_pseudonokts NUMBER(10,0),
        tax_seed VARCHAR(500),
        ecmli_lambda NUMBER(10, 2),
        ecmli_mu NUMBER(10, 2),
        ecmli_cal_db NUMBER(10,0),
        ecmli_cal_hits NUMBER(10,0),
        maxl NUMBER(10,0),
        clen NUMBER(10,0),
        match_pair_node BOOLEAN,
        hmm_tau NUMBER(10, 2),
        hmm_lambda NUMBER(10, 2),
        created TIMESTAMP,
        updated TIMESTAMP
    )
    """
    cursor.execute(create_table_sql)
    print("Table 'FAMILY' checked/created successfully.")

    cursor.execute("USE WAREHOUSE COMPUTE_WH")
    print("Using warehouse 'COMPUTE_WH'.")

    # Upload CSV with AUTO_COMPRESS=TRUE
    put_command = f"PUT file://{csv_path} @%FAMILY AUTO_COMPRESS=TRUE OVERWRITE=TRUE"
    cursor.execute(put_command)
    print("CSV file uploaded to Snowflake stage successfully.")

    # Create a file format with proper CSV options including quotes and skipping header if exists
    cursor.execute("""
        CREATE OR REPLACE FILE FORMAT my_csv_format 
        TYPE = 'CSV' 
        FIELD_DELIMITER = ',' 
        SKIP_HEADER = 0 
        FIELD_OPTIONALLY_ENCLOSED_BY = '"'
        EMPTY_FIELD_AS_NULL = TRUE
        ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
    """)

    # COPY with ON_ERROR = CONTINUE to skip bad rows
    copy_command = """
        COPY INTO FAMILY
        FILE_FORMAT = my_csv_format
        ON_ERROR = 'CONTINUE'
    """
    cursor.execute(copy_command)
    print("Data copied into 'FAMILY' table successfully (errors ignored).")

except Exception as e:
    print(f"Error executing Snowflake commands: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and not conn.is_closed():
        conn.close()
        print("Snowflake connection closed.")

