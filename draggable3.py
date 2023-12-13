from PyQt5.QtWidgets import QApplication, QWidget

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

app = QApplication([])
widget = DropWidget()
widget.show()
app.exec_()




# import tkinter as tk

# def on_drop(event):
#     # Get the path of the dropped file
#     file_path = event.data

#     # Check if it's a CSV file
#     if file_path.endswith(".csv"):
#         # Open the file and process the data
#         with open(file_path, "r") as file:
#             # Your code to read and analyze the data goes here
#             print(f"Opened file: {file_path}")

# # Create the main window
# root = tk.Tk()

# # Create a label to display information
# label = tk.Label(root, text="Drop your CSV file here")
# label.pack()

# # Bind the drop event to the label
# label.bind("<Drop>", on_drop)

# # Start the main loop
# root.mainloop()
