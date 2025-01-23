import tkinter as tk
import s_searcher

# Function to send "11111111"
def send_ones():
    s_searcher.send_data("11111111")

# Function to send "00000000"
def send_zeros():
    s_searcher.send_data("00000000")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Serial Sender")

# Create buttons
button_ones = tk.Button(root, text='Send "11111111"', command=send_ones, width=20, height=2)
button_ones.pack(pady=10)

button_zeros = tk.Button(root, text='Send "00000000"', command=send_zeros, width=20, height=2)
button_zeros.pack(pady=10)

# Run the GUI
root.mainloop()