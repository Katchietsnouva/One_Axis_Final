import tkinter as tk
from tkinter import ttk
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading    
import numpy as np
from matplotlib.figure import Figure
import csv

# Variables
is_plotting = False
pulses = np.array([])
max_data_points = 50
data_counter = 0  # Counter for unique data files
csv_data = []  # List to hold the data
# Lock for synchronizing access to shared data
data_lock = threading.Lock()
# Function to start reading data from Arduino
def start_plotting():
    global is_plotting
    is_plotting = True
    thread = threading.Thread(target=update_plot)
    thread.daemon = True
    thread.start()
    ser.reset_input_buffer()

# Function to stop reading data from Arduino
def stop_plotting():
    global is_plotting
    is_plotting = False

# Function to update the first plot
def update_plot():
    global is_plotting,pulses,csv_data, data_counter
    while is_plotting:
        try:
            data = ser.readline().decode('utf-8').strip()
            comb_data= data.split(',')
            #if(len(comb_data)==3):
            
            pwm = comb_data[0]
            
            with data_lock:
                if len(pulses) < 50:
                    pulses = np.append(pulses, int(pwm[0:4]))
                    
                    
                else:
                    pulses[0:49] = pulses[1:50]
                    pulses[49] = float(pwm[0:4])

            pwm_label.config(text=f'PWM: {pwm}')

                        # Append data to csv_data
            csv_data.append([pwm])

            # Check if data exceeds 200 points and save to a new CSV file
            if len(csv_data) >= max_data_points:
                save_data_to_csv(data_counter)
                data_counter += 1
                csv_data = []
            root.after(1, update_plot3)
        except Exception as e:
          print(e)
        #root.update()

# Function to save data to a CSV file with a unique identifier
def save_data_to_csv(counter):
    filename = f'datapwm{counter}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['PWM'])
        for data_point in csv_data:
            csvwriter.writerow(data_point)
# Start a separate thread to continuously update data and plots
data_thread = threading.Thread(target=update_plot)
data_thread.daemon = True
data_thread.start()


# Function to update the third plot
def update_plot3():
    with data_lock:
        lines3.set_xdata(np.arange(0, len(pulses)))
        lines3.set_ydata(pulses)
    canvas3.draw()

# Function to send commands to Arduino
def send_command(command):
    ser.write(command.encode('utf-8'))

# Function to update the serial connection with selected COM port and baud rate
def update_serial_connection(): 
    selected_com_port = com_port_combo.get()
    selected_baud_rate = baud_rate_combo.get()
    
    global ser
    ser.close()
    ser = serial.Serial(selected_com_port, int(selected_baud_rate))
    ser.reset_input_buffer()

# Initialize tkinter window
root = tk.Tk()
root.title("ONE AXIS AUTOMATED DRILL GRAPHICAL USER INTERFACE FOR MOTOR CONTROL")
root.configure(background='lightblue')

# Serial communication setup
ser = serial.Serial()  # Initialize with default values
#ser.reset_input_buffer()

# Create GUI components
root.update()
start_button = ttk.Button(root, text="Start Plot", command=start_plotting)
stop_button = ttk.Button(root, text="Stop Plot", command=stop_plotting)
pwm_label = ttk.Label(root, text="PWM: ",font=("Helvetica",10))

fast_drill_speed_button = ttk.Button(root, text="FAST DRILL SPEED", command=lambda: send_command('fastdrill'))
fast_drill_speed_button.grid(row=4, column=0, padx=10, pady=10)

slow_drill_speed_button = ttk.Button(root, text="SLOW DRILL SPEED", command=lambda: send_command('slowdrill'))
slow_drill_speed_button.grid(row=4, column=2, padx=10, pady=10)

stop_machine_button = ttk.Button(root, text="STOP MACHINE", command=lambda: send_command('stopmachine'))
stop_machine_button.grid(row=4, column=4)
# Dropdown menu for COM port selection
com_port_label = ttk.Label(root, text="Select COM Port:")
com_port_label.grid(row=1, column=0, sticky="w",padx=10,pady=5)
com_ports = ["COM1", "COM2", "COM3", "COM4","COM5"]  # Replace with your available COM ports
com_port_combo = ttk.Combobox(root, values=com_ports)
com_port_combo.grid(row=1, column=1,padx=10,pady=5)
com_port_combo.set("COM1")  # Set a default COM port

# Dropdown menu for baud rate selection
baud_rate_label = ttk.Label(root, text="Select Baud Rate:")
baud_rate_label.grid(row=2, column=0, sticky="w",padx=10,pady=5)
baud_rates = ["9600", "115200", "57600", "38400"]  # Replace with your available baud rates
baud_rate_combo = ttk.Combobox(root, values=baud_rates)
baud_rate_combo.grid(row=2, column=1,padx=10,pady=5)
baud_rate_combo.set("9600")  # Set a default baud rate

# Button to update the serial connection with selected COM port and baud rate
update_button = ttk.Button(root, text="Update Serial Connection", command=update_serial_connection)
update_button.grid(row=3, column=0, columnspan=2)

# Matplotlib setup for the third plot
fig3 = Figure(figsize=(6,4))
ax3 = fig3.add_subplot(111)
ax3.set_title("PWM")
#ax3.set_xlabel("Time")
ax3.set_ylabel("pwm")
ax3.grid(True)
ax3.set_xlim([0, 50])
ax3.set_ylim([0, 260])
lines3 = ax3.plot([], [])[0]
canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.get_tk_widget().grid(row=0, column=4, columnspan=1,rowspan=4,padx=20, pady=10)
canvas3.draw()

# Grid layout
start_button.grid(row=0, column=0)
stop_button.grid(row=0, column=1)
pwm_label.grid(row=20, column=0)
root.after(1, update_plot)
root.mainloop()
