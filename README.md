**Micropython_UART**

This project provides a simple way to communicate with a microcontroller (like Raspberry Pi Pico, ESP32, etc.) over UART. It includes:

* A library (s_searcher.py) to handle OS detection and serial communication.
* A GUI application (serialcomm.py) for sending data to the microcontroller.
* A MicroPython script (UART_MICRO.py) to run on the microcontroller.

**File Descriptions**

1. **s_searcher.py**

   * Detects the operating system (Windows, Linux, or Android) using os.name.
   * Configures and manages UART communication for each OS.
   * Provides a `send_data(data)` function to send data to the microcontroller.

2. **serialcomm.py**

   * The main script for user interaction.
   * Provides a Tkinter GUI with buttons to send data ("11111111" or "00000000") to the microcontroller.
   * Relies on s_searcher.py for serial communication.

3. **UART_MICRO.py**

   * The MicroPython script for the microcontroller.
   * Listens for incoming data on the UART channel at 115200 baud.
   * Performs actions based on the received data.
   * Requires correct UART pin configuration on your microcontroller.

**Requirements**

* **Windows:**
    * Python 3.x
    * `pyserial` library (install using `pip install pyserial`)
* **Linux:**
    * Python 3.x
    * `pyserial` library (install using `pip install pyserial`)
* **Android (using Pydroid):**
    * Pydroid 3 app from Google Play Store
    * `usb4a` and `usbserial4a` libraries (install via Pydroid's Pip interface)

**How to Use**

1. **Flash MicroPython Code:**
   Upload `UART_MICRO.py` to your microcontroller using a MicroPython IDE (like Thonny).

2. **Run GUI Application:**
   Execute `serialcomm.py` on your computer or Android device.

3. **Connect Microcontroller:**
   * Windows/Linux: Connect via USB.
   * Android: Use an OTG adapter for connection.

**Contributions**

Feel free to contribute by opening issues or submitting pull requests.
