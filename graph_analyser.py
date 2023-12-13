import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

import io

# Your sample data
data = """
Vibration,Temperature,Force
23.0,20.04,-0.0
23.21,20.04,-0.0
23.21,20.04,-0.0
23.21,20.04,-0.0
23.17,20.04,-0.0
23.17,20.04,-0.0
23.17,20.04,-0.0
23.15,20.04,-0.0
"""

# Create a DataFrame from the data
# df = pd.read_csv(pd.compat.StringIO(data))

# Create a StringIO object
data_stream = StringIO(data)

# Read the data using pandas.read_csv
df = pd.read_csv(data_stream)
# df = pd.read_csv(data)

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




