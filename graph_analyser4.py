import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the current script directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the data folder path
data_folder_path = os.path.join(current_directory, 'data_compilation')

# Iterate through all files in the folder
for filename in os.listdir(data_folder_path):
    # Check if it's a CSV file
    if filename.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(data_folder_path, filename)

        # Read the data from the CSV file
        df = pd.read_csv(file_path)

        # Create a figure for the current file's data
        plt.figure(figsize=(10, 6))

        # Plot each column
        plt.plot(df['Temperature'], label='Temperature')
        plt.plot(df['Vibration'], label='Vibration')
        plt.plot(df['Force'], label='Force')

        # Customize the plot
        plt.title(f'Vibration, Temperature, and Force in {filename[:-4]}')  # Extract file name without extension
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.legend()
        plt.grid(True)

        # Save the plot as a PNG image with the original filename
        plt.savefig(os.path.join(data_folder_path, f'{filename[:-4]}.png'))

        # Close the figure to avoid overlapping plots
        plt.close()

print(f'Finished processing all files in {data_folder_path}')

