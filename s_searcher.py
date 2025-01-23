import os
import time
if os.name == "nt":  # Windows
    import serial
    import serial.tools.list_ports
elif os.name == "posix":  # Linux/Android
    from usb4a import usb
    from usbserial4a import serial4a


def send_data_windows(data):
    """Send data using pyserial on Windows."""
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No serial ports found.")
        return

    selected_port = ports[0].device
    print(f"Using port: {selected_port}")

    baudrate = 115200
    bytesize = serial.EIGHTBITS
    parity = serial.PARITY_NONE
    stopbits = serial.STOPBITS_ONE
    timeout = 3

    try:
        with serial.Serial(selected_port, baudrate, bytesize, parity, stopbits, timeout=timeout) as ser:
            ser.write(data.encode())  # Send data
            print(f"Sent: {data}")
    except Exception as e:
        print(f"Error: {e}")


def send_data_linux_android(data):
    """Send data using usb4a and usbserial4a on Linux/Android."""
    usb_device_list = usb.get_usb_device_list()
    if not usb_device_list:
        print("No USB devices found.")
        return

    device_name = usb_device_list[0].getDeviceName()
    print(f"Using USB device: {device_name}")

    try:
        serial_port = serial4a.get_serial_port(device_name, 115200, 8, "N", 1)
        if serial_port and serial_port.is_open:
            serial_port.write(data.encode())  # Send data
            print(f"Sent: {data}")
            serial_port.close()
    except Exception as e:
        print(f"Error: {e}")


def send_data(data):
    """Send data based on the detected OS."""
    if os.name == "nt":  # Windows
        send_data_windows(data)
        time.sleep(0.1)
    elif os.name == "posix":  # Linux/Android
        send_data_linux_android(data)
        time.sleep(0.1)
    else:
        print("Unsupported platform!")