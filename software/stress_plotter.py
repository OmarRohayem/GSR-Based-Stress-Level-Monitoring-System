import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re
import csv
from datetime import datetime

# --- CONFIGURATION ---
# CHANGE THIS to your actual Arduino Port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Mac/Linux)
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

# --- SETUP ---
# Initialize lists to hold data
x_vals = []
y_vals = []
index = 0

# Initialize Serial Connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print(f"Connected to {SERIAL_PORT}")
except:
    print(f"ERROR: Could not connect to {SERIAL_PORT}. Check your port name.")
    exit()

# Setup CSV logging
filename = f"stress_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "GSR_Value", "Status"])

def read_and_process_data():
    """Reads a line from Arduino, parses the GSR value, and returns it."""
    if ser.in_waiting > 0:
        try:
            # Read line from Arduino
            line = ser.readline().decode('utf-8').strip()
            print(f"Arduino says: {line}") # Debugging print
            
            # Parse the specific format: "Time: 1234 ms, GSR Avg: 512 --> Normal..."
            # We look for the number after "GSR Avg:"
            match = re.search(r"GSR Avg:\s*(\d+)", line)
            
            if match:
                gsr_value = int(match.group(1))
                return gsr_value, line
        except Exception as e:
            print(f"Error reading data: {e}")
    return None, None

def update(frame):
    global index
    val, original_line = read_and_process_data()
    
    if val is not None:
        x_vals.append(index)
        y_vals.append(val)
        index += 1
        
        # Keep only the last 50 data points to keep the graph moving smoothly
        if len(x_vals) > 50:
            x_vals.pop(0)
            y_vals.pop(0)
            
        # Log to CSV
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), val, original_line])

        # Clear and redraw plot
        plt.cla()
        plt.plot(x_vals, y_vals, label='GSR Skin Resistance', color='blue')
        plt.axhline(y=650, color='r', linestyle='--', label='Stress Threshold')
        plt.axhline(y=500, color='g', linestyle='--', label='Calm Threshold')
        plt.legend(loc='upper left')
        plt.title('Real-Time Physiological Stress Monitor')
        plt.ylabel('GSR Value (Analog 0-1023)')
        plt.xlabel('Time (Readings)')
        plt.grid(True)

# Start the Animation
ani = FuncAnimation(plt.gcf(), update, interval=100)
plt.tight_layout()
plt.show()
