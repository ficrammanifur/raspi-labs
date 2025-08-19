import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import socket

# OLED setup
WIDTH = 128
HEIGHT = 64
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Buat canvas
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Posisi mata
LEFT_EYE = (28, 10, 52, 34)
RIGHT_EYE = (76, 10, 100, 34)

# Font untuk status
font = ImageFont.load_default()

# Fungsi cek internet
def check_internet(host="8.8.8.8", port=53, timeout=1):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

# Fungsi gambar mata
def draw_eyes(left_offset=0, right_offset=0, blink=False):
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)  # bersihkan layar

    # Gambar mata
    if blink:
        draw.line((LEFT_EYE[0], 22, LEFT_EYE[2], 22), fill=255, width=2)
        draw.line((RIGHT_EYE[0], 22, RIGHT_EYE[2], 22), fill=255, width=2)
    else:
        draw.ellipse((LEFT_EYE[0]+left_offset, LEFT_EYE[1], LEFT_EYE[2]+left_offset, LEFT_EYE[3]), outline=255, fill=255)
        draw.ellipse((RIGHT_EYE[0]+right_offset, RIGHT_EYE[1], RIGHT_EYE[2]+right_offset, RIGHT_EYE[3]), outline=255, fill=255)

    # Status internet
    status = "INTERNET ACCESS" if check_internet() else "NO INTERNET"
    w, h = draw.textsize(status, font=font)
    draw.text(((WIDTH-w)//2, HEIGHT-10), status, font=font, fill=255)

    oled.image(image)
    oled.show()

# Loop animasi mata
pos_list = [-4, -2, 0, 2, 4, 2, 0, -2]

try:
    while True:
        # Mata terbuka, gerak kiri-kanan
        for pos in pos_list:
            draw_eyes(left_offset=pos, right_offset=pos, blink=False)
            time.sleep(0.15)
        # Kedip
        draw_eyes(blink=True)
        time.sleep(0.2)
        draw_eyes(blink=False)
        time.sleep(0.2)
except KeyboardInterrupt:
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)
    oled.image(image)
    oled.show()
    print("Program berhenti.")
