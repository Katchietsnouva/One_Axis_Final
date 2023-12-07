import tkinter as tk

class Switch(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        tk.Canvas.__init__(self, master, **kwargs)
        self.width = kwargs.get('width', 60)
        self.height = kwargs.get('height', 30)
        self.background_color = kwargs.get('background_color', 'lightgray')
        self.switch_color = kwargs.get('switch_color', 'green')
        self.state = kwargs.get('state', 'off')
        self.bind("<Button-1>", self.toggle_switch)
        self.draw_switch()

    def draw_switch(self):
        self.delete("all")
        self.create_rectangle(0, 0, self.width, self.height, fill=self.background_color, outline='black')
        if self.state == 'on':
            switch_position = self.width - self.height
        else:
            switch_position = 0
        self.create_oval(switch_position, 0, switch_position + self.height, self.height, fill=self.switch_color, outline='black')

    def toggle_switch(self, event=None):
        if self.state == 'on':
            self.state = 'off'
        else:
            self.state = 'on'
        self.draw_switch()

# Create the main window
root = tk.Tk()
root.title("Switch Widget Example")

# Switch attributes
switch_width = 60
switch_height = 30
switch_bg_color = 'lightgray'
switch_color = 'green'
switch_state = 'off'

# Create the switch with specified attributes
switch = Switch(root,
                width=switch_width,
                height=switch_height,
                background_color=switch_bg_color,
                switch_color=switch_color,
                state=switch_state)

# Place the switch in the window
switch.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
