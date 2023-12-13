import tkinter as tk

class DragAndDrop(tk.Frame):

  def __init__(self, parent):
    tk.Frame.__init__(self, parent)
    self.parent = parent
    self.parent.columnconfigure(0, weight=1)
    self.grid_columnconfigure(0, weight=1)

    self.block_count = 0

    self.button = tk.Button(self, text='Add', command=self.addblock)
    self.button.grid(row=0, column=0, columnspan=2, sticky='new')

    self.container = tk.Frame(self)
    self.container.grid(row=1, column=0, sticky='nsew')

    self.canvas = tk.Canvas(self.container, width=200, height=450)
    self.scrollbar = tk.Scrollbar(self.container,
                                  orient='vertical',command=self.canvas.yview)
    self.canvas.config(yscrollcommand=self.scrollbar.set)
    self.canvas.grid(row=0, column=0, sticky='nsew')
    self.scrollbar.grid(row=0, column=1, sticky='nse')

    self.container.bind('<Configure>', self.handle_scroll)

  def addblock(self):
    self.block = tk.Frame(self.canvas, bd=1, relief='solid')
    self.block.columnconfigure(0, weight=1)

    self.grip = tk.Label(self.block, bitmap="gray25")
    self.grip.grid(row=0, column=0, sticky='w')

    self.grip.bind("<ButtonPress-1>", self.StartMove)
    self.grip.bind("<ButtonRelease-1>", self.StopMove)
    self.grip.bind("<B1-Motion>", self.OnMotion)

    self.canvas.create_window((0, (self.block_count*25)),
                              window=self.block, anchor="nw",
                              width=200, height=24)
    self.block_count += 1
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

  def handle_scroll(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

  def StartMove(self, event):
    self.y = event.y
    self.cy = event.widget.nametowidget(event.widget.winfo_parent()).winfo_y()
    self.current = self.canvas.find_closest(10, self.cy)[0]

  def OnMotion(self, event):
    self.canvas.move(self.current, 0, event.y - 10)

  def StopMove(self, event):
    self.y = None

root = tk.Tk()
app = DragAndDrop(root)
app.grid(row=0, column=0, sticky='ew')
root.mainloop()