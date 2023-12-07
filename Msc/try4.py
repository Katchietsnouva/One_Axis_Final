import customtkinter as ctk
import ctypes

root = ctk.CTk()
group_1b = ctk.CTkFrame(root)

dark_mode = False

try:
    value = ctypes.windll.uxtheme.IsThemeActive()
    dark_mode = value == 1
except Exception as e:
    print(f'A Theme Error has occurred: {e}')
    dark_mode = False

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_Theme()

def update_Theme():
    theme = "dark" if dark_mode else "light"
    root.configure(background='black' if dark_mode else 'light')
    ctk.set_appearance_mode(theme)
    print(f"Switching to {theme} Mode")
    switch_1.configure(text='Light Mode' if dark_mode else 'Dark Mode')
    # canvas3.get_tk_widget().configure(bg='black' if dark_mode else 'white')

# Initialize the switch based on the initial dark mode state
initial_switch_state = 'on' if dark_mode else 'off'
# switch_1 = ctk.CTkSwitch(master=group_1b, text=f'Light Mode {initial_switch_state}', command=toggle_dark_mode, state=ctk.NORMAL)
switch_1 = ctk.CTkSwitch(master=group_1b, text=f'Light Mode {initial_switch_state}',
                          command=toggle_dark_mode, offvalue=1)
switch_1.pack()
group_1b.pack()

root.title("MOTOR CONTROL GUI:          ONE AXIS AUTOMATED DRILL")
root.configure(background='lightblue')
root.mainloop()
