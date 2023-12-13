# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# # Get the current script directory
# current_directory = os.path.dirname(os.path.abspath(__file__))
# data_folder = os.path.join(current_directory, 'data_compilation')

# # Iterate through all files in the folder
# for file_name in os.listdir(data_folder):
#     # Check if the file is a CSV file
#     if file_name.endswith('.csv'):
#         # Construct the file path for the CSV file
#         csv_file_path = os.path.join(data_folder, file_name)

#         # Read the data from the CSV file
#         df = pd.read_csv(csv_file_path)

#         # Plot the data
#         plt.figure(figsize=(10, 6))

#         # Plot each column
#         plt.plot(df['Vibration'], label='Vibration')
#         plt.plot(df['Temperature'], label='Temperature')
#         plt.plot(df['Force'], label='Force')

#         # Customize the plot
#         plt.title(f'Vibration, Temperature, and Force over Time - {file_name}')
#         plt.xlabel('Time')
#         plt.ylabel('Values')
#         plt.legend()
#         plt.grid(True)

#         # Show the plot
#         plt.show()



