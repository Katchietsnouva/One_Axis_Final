import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "Hello, Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Attributes Example")

# Button attributes
button_text = "Click Me"
button_bg_color = "lightblue"
button_command = on_button_click
button_state = "normal"  # Options: "normal", "active", "disabled"
button_font = ("Arial", 12, "bold")
button_relief = "ridge"  # Options: "flat", "raised", "sunken", "ridge", "groove", "solid"

# Create the button with specified attributes
button = tk.Button(root,
                   text=button_text,
                   background=button_bg_color,
                   command=button_command,
                   state=button_state,
                   font=button_font,
                   relief=button_relief)

# Place the button in the window
button.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
