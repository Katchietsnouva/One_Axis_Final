import os
import pandas as pd

# Define the project path and compilation directory
project_path = r"J:\Projects Folders Drive\EmbeddedSystemsEngineerReload\embeddedEngineer\One_Axis_Final"
compilation_directory = os.path.join(project_path, "data_compilation")

# Create the compilation directory if it doesn't exist
if not os.path.exists(compilation_directory):
    os.makedirs(compilation_directory)

# Define the data directory
data_directory = os.path.join(project_path, "data")

# Loop through all files in the data directory
for root, _, files in os.walk(data_directory):
    for file in files:
        if file.endswith(".csv"):
            # Extract the file name without extension
            file_name, _ = os.path.splitext(file)

            # Get the full path to the csv file
            file_path = os.path.join(root, file)

            # Read the csv file
            data = pd.read_csv(file_path)

            # Save the data to a new csv file with the extracted file name
            data.to_csv(os.path.join(compilation_directory, f"{file_name}.csv"), index=False)

print("Data compilation completed successfully!")
