from PyQt5.QtWidgets import QApplication, QWidget

import os
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


class DropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        # Check if it's a CSV file and process it
        # ... (similar to Tkinter example)
        # Check if it's a CSV file
        if file_path.endswith(".csv"):
            # Open the file and process the data
            with open(file_path, "r") as file:
                # Your code to read and analyze the data goes here
                print(f"Opened file: {file_path}")

                df = pd.read_csv(file_path)

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


app = QApplication([])
widget = DropWidget()
widget.show()
app.exec_()

# Read the data from the CSV file

