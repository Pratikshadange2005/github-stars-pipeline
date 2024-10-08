import os
import zipfile
import duckdb
import tempfile
from datetime import datetime

# Step 1: Extract the zip file into a temporary directory
def extract_zip_file(zip_file_path):
    temp_dir = tempfile.TemporaryDirectory()  # Create a temporary directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir.name)
    return temp_dir

# Step 2: Load JSON files into DuckDB with 'loaded_at' and process only new files
def load_json_gz_files_in_duck_db(json_dir, duckdb_path):
    # Open the DuckDB connection (ensure you connect to the correct persistent database)
    con = duckdb.connect(duckdb_path) 

    # Create schema if not exists
    con.sql("CREATE SCHEMA IF NOT EXISTS source;")
    
    # Check if the 'src_gharchive' table exists
    try:
        con.sql("SELECT 1 FROM source.src_gharchive LIMIT 1")
        table_exists = True
    except duckdb.CatalogException:
        table_exists = False

    # If the table exists, check for the max 'loaded_at' timestamp
    if table_exists:
        try:
            last_loaded_time = con.execute("SELECT MAX(loaded_at) FROM source.src_gharchive").fetchone()[0]
        except duckdb.BinderException:
            last_loaded_time = None
    else:
        last_loaded_time = None

    # Current time for the 'loaded_at' column
    current_time = datetime.now()

    # Load only files with 'created_at' newer than the last loaded time
    query = f"""
        CREATE OR REPLACE TABLE source.src_gharchive AS
        SELECT *, '{current_time}' AS loaded_at
        FROM read_json_auto('{json_dir}/*.json.gz')
    """
    
    # Use `created_at` column for filtering 
    if last_loaded_time:
        query += f" WHERE created_at > '{last_loaded_time}'"

    # Execute the query to load or update the table
    con.sql(query)
    print(f"New data loaded into source.src_gharchive.")

    # Close the DuckDB connection
    con.close()

# Main function 
if __name__ == "__main__":
    # path to the zip file
    zip_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "gharchive_sample.zip")
    
    # Define the DuckDB file path (persistent file)
    duckdb_path = 'github_stars.db'  

    # Step 3: Extract the zip file into a temporary folder
    temp_dir = extract_zip_file(zip_file_path)

    # Step 4: Load the extracted JSON files into DuckDB
    unpacked_json_dir = os.path.join(temp_dir.name, "gharchive_sample")
    load_json_gz_files_in_duck_db(unpacked_json_dir, duckdb_path)

    # Cleanup temporary folder
    temp_dir.cleanup()  
