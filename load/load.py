import os
import zipfile
import duckdb
import tempfile
from datetime import datetime

# Extract the zip file into the provided directory
def extract_zip_file(zip_file_path, target_dir):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

# Load JSON files into DuckDB with 'loaded_at' and process only new files
def load_json_gz_files_in_duck_db(json_dir, duckdb_path):
    con = duckdb.connect(duckdb_path) 

    con.sql("CREATE SCHEMA IF NOT EXISTS source;")
    
    try:
        con.sql("SELECT 1 FROM source.src_gharchive LIMIT 1")
        table_exists = True
    except duckdb.CatalogException:
        table_exists = False

    if table_exists:
        try:
            last_loaded_time = con.execute("SELECT MAX(loaded_at) FROM source.src_gharchive").fetchone()[0]
        except duckdb.BinderException:
            last_loaded_time = None
    else:
        last_loaded_time = None

    current_time = datetime.now()

    query = f"""
        CREATE OR REPLACE TABLE source.src_gharchive AS
        SELECT *, '{current_time}' AS loaded_at
        FROM read_json_auto('{json_dir}/*.json.gz')
    """
    
    if last_loaded_time:
        query += f" WHERE created_at > '{last_loaded_time}'"

    con.sql(query)
    print(f"New data loaded into source.src_gharchive.")
    con.close()

if __name__ == "__main__":
    zip_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "gharchive_sample.zip")
    duckdb_path = 'github_stars.db'  


    with tempfile.TemporaryDirectory() as temp_dir:
        extract_zip_file(zip_file_path, temp_dir)
        unpacked_json_dir = os.path.join(temp_dir, "gharchive_sample")
        load_json_gz_files_in_duck_db(unpacked_json_dir, duckdb_path)
