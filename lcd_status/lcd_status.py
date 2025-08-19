import socket
import time
from RPLCD.i2c import CharLCD

# Inisialisasi LCD (alamat I2C biasanya 0x27 atau 0x3F)
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

def check_internet(host="8.8.8.8", port=53, timeout=3):
    """Cek apakah ada koneksi internet"""
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

while True:
    lcd.clear()
    if check_internet():
        # Jika ada internet
        line1 = "INTERNET"
        line2 = "ACCESS"
        lcd.cursor_pos = (0, (16 - len(line1)) // 2)  # rata tengah baris 1
        lcd.write_string(line1)
        lcd.cursor_pos = (1, (16 - len(line2)) // 2)  # rata tengah baris 2
        lcd.write_string(line2)
    else:
        # Jika tidak ada internet
        line1 = "CAN'T CONNECT"
        line2 = "INTERNET"
        lcd.cursor_pos = (0, (16 - len(line1)) // 2)
        lcd.write_string(line1)
        lcd.cursor_pos = (1, (16 - len(line2)) // 2)
        lcd.write_string(line2)
    
    time.sleep(5)  # update tiap 5 detik
