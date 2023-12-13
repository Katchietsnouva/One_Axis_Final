import os
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Get the current script directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path for the CSV file in the "data_compilation" folder
csv_file_path = os.path.join(current_directory, 'data_compilation', 'longspanfastdrillspeed1.csv')

# Read the data from the CSV file
df = pd.read_csv(csv_file_path)

# Plot the data
plt.figure(figsize=(10, 6))

# Plot each column
plt.plot(df['Vibration'], label='Vibration')
plt.plot(df['Temperature'], label='Temperature')
plt.plot(df['Force'], label='Force')

# Customize the plot
plt.title('Vibration, Temperature, and Force over Time')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
