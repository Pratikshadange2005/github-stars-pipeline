import zipfile
import os
import tempfile
import pandas as pd
import json
import gzip
from datetime import datetime

# Function to extract zip files into a temporary directory
def extract_zip_file(zip_file_path):
    temp_dir = tempfile.TemporaryDirectory()
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir.name)
    return temp_dir

# Function to get .json.gz files
def get_json_gz_files(extracted_dir):
    return [os.path.join(root, file) 
            for root, _, files in os.walk(extracted_dir) 
            for file in files if file.endswith('.json.gz')]

# Function to process JSON.GZ files
def process_json_gz_files(files, table_path):
    existing_df = pd.read_csv(table_path) if os.path.exists(table_path) else pd.DataFrame()
    last_loaded_time = pd.to_datetime(existing_df['loaded_at']).max() if not existing_df.empty else None
    
    new_data = []
    for file in files:
        with gzip.open(file, 'rt') as f:
            data = json.load(f)
            data['loaded_at'] = datetime.now()
            if last_loaded_time is None or data['date'] > last_loaded_time:
                new_data.append(data)
    
    if new_data:
        new_df = pd.DataFrame(new_data)
        pd.concat([existing_df, new_df], ignore_index=True).to_csv(table_path, index=False)

# Main script function
def main(zip_file_path, table_path):
    temp_dir = extract_zip_file(zip_file_path)
    extracted_files = get_json_gz_files(temp_dir.name)
    process_json_gz_files(extracted_files, table_path)
    temp_dir.cleanup()


