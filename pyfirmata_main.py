from pyfirmata import Arduino
import time

if __name__ == '__main__':
    board = Arduino('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0')
    print("Communication Successfully started")

    while True:
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)
