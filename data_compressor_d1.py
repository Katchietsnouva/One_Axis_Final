import os
import pandas as pd

# Set your project and data paths
project_path = r'J:\Projects Folders Drive\EmbeddedSystemsEngineerReload\embeddedEngineer\One_Axis_Final'
compilation_path = os.path.join(project_path, 'data_compilation2')
cleaned_path = os.path.join(project_path, 'data_compilation_cleaned')

# Create the cleaned directory if it doesn't exist
os.makedirs(cleaned_path, exist_ok=True)

# Function to sample and save CSV files
def sample_and_save_csv(file_path, interval=100):
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Calculate the number of rows (excluding header)
    num_rows = len(data) - 1
    
    # Ensure there are enough rows to sample
    if num_rows <= interval:
        print(f"Skipping {file_path}: Not enough rows to sample.")
        return
    
    # Calculate the sampling interval
    sampling_interval = max(1, num_rows // interval)
    
    # Sample the data at approximate intervals
    sampled_data = data.iloc[::sampling_interval]
    
    # Extract the file name from the path
    file_name = os.path.basename(file_path)
    
    # Create the output file name
    output_file_name = f"{file_name[:-4]}_cleaned.csv"
    
    # Save the sampled data to the cleaned directory
    output_file_path = os.path.join(cleaned_path, output_file_name)
    sampled_data.to_csv(output_file_path, index=False)
    print(f"Sampled data saved to {output_file_path}")

# Iterate through each merged CSV file in the compilation folder
for file_name in os.listdir(compilation_path):
    file_path = os.path.join(compilation_path, file_name)
    
    # Check if it's a CSV file
    if file_name.endswith('.csv') and os.path.isfile(file_path):
        sample_and_save_csv(file_path)
