import tkinter as tk

def on_drop(event):
    # Get the path of the dropped file
    file_path = event.data

    # Check if it's a CSV file
    if file_path.endswith(".csv"):
        # Open the file and process the data
        with open(file_path, "r") as file:
            # Your code to read and analyze the data goes here
            print(f"Opened file: {file_path}")

# Create the main window
root = tk.Tk()

# Create a label to display information
label = tk.Label(root, text="Drop your CSV file here")
label.pack()

# Bind the drop event to the label
label.bind("<Drop>", on_drop)

# Start the main loop
root.mainloop()
