# OLED Eye - Raspberry Pi 5 👀

Folder ini berisi project untuk **OLED 0.96 inch I2C 128x64** sebagai **bola mata berkedip dan bergerak** menggunakan **Python**.

---

## 🔹 Konfigurasi Pin

- OLED I2C biasanya menggunakan alamat **0x3C**.  
- Sambungkan SDA dan SCL ke pin I2C Raspberry Pi:
  - SDA → Pin 3 (GPIO2)
  - SCL → Pin 5 (GPIO3)
- Pastikan I2C diaktifkan (`sudo raspi-config → Interface Options → I2C`).

---

## 🔹 Cara Menjalankan

1. Buat folder virtual environment (env):
```bash
python3 -m venv /home/debian/oled_env
```

2. Aktifkan environment:
```
source /home/debian/oled_env/bin/activate
```

3. Install dependency:
```
pip install adafruit-circuitpython-ssd1306 pillow
```

4.Jalankan script:
```
python3 oled_eye.py
```
    
⚠️ Catatan:
        Script hanya berjalan saat dijalankan ulang, tidak permanent.
        Jika ingin membuatnya permanent (misal autostart saat boot), gunakan systemd service atau cron @reboot.

🔹 Fungsi Script
    Menampilkan dua bola mata OLED yang berkedip dan bergerak.
    Bisa dikembangkan untuk integrasi sensor atau status lain.
