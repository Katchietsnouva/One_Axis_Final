import os
import pandas as pd

# Set your project and data paths
project_path = r'J:\Projects Folders Drive\EmbeddedSystemsEngineerReload\embeddedEngineer\One_Axis_Final'
data_path = os.path.join(project_path, 'data')
compilation_path = os.path.join(project_path, 'data_compilation')

# Create the compilation directory if it doesn't exist
os.makedirs(compilation_path, exist_ok=True)

# Function to combine CSV files in a directory and save the result
def combine_and_save_csv(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    if not files:
        print(f"No CSV files found in {folder_path}")
        return
    
    # Sort files based on numerical values in descending order
    files.sort(key=lambda x: int(x.split('sensors')[-1].split('.')[0]), reverse=False)
    
    # Create an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()
    
    # Iterate through each CSV file and concatenate data
    for file in files:
        file_path = os.path.join(folder_path, file)
        data = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, data], ignore_index=True)
    
    # Extract the folder name from the path
    folder_name = os.path.basename(folder_path)
    
    # Create the output file name
    output_file_name = f"{folder_name}.csv"
    
    # Save the combined data to the compilation directory
    output_file_path = os.path.join(compilation_path, output_file_name)
    combined_data.to_csv(output_file_path, index=False)
    print(f"Combined data saved to {output_file_path}")

# Iterate through each subdirectory in the data folder
# Iterate through each subdirectory in the data folder
for subfolder in os.listdir(data_path):
    subfolder_path = os.path.join(data_path, subfolder)
    
    # Check if it's a directory
    if os.path.isdir(subfolder_path):
        combine_and_save_csv(subfolder_path)
