# LCD Status - Raspberry Pi 5 🖥️

Folder ini berisi project untuk **menampilkan status koneksi internet** pada **LCD 16x2 I2C (PCF8574)** menggunakan **Python**.

---

## 🔹 Konfigurasi Pin

- LCD 16x2 I2C biasanya menggunakan **alamat 0x27** atau **0x3F**.  
- Sambungkan SDA dan SCL ke pin I2C Raspberry Pi:
  - SDA → Pin 3 (GPIO2)
  - SCL → Pin 5 (GPIO3)
- Pastikan I2C diaktifkan (`sudo raspi-config → Interface Options → I2C`).

---

## 🔹 Cara Menjalankan

1. Buat folder virtual environment (env):
```bash
python3 -m venv /home/debian/lcd_env
```

2. Aktifkan environment:
```
source /home/debian/lcd_env/bin/activate
```

3. Install dependency:
```
pip install RPLCD
```
    
4. Jalankan script:
```
python3 lcd_status.py
```

⚠️ Catatan:
Script hanya berjalan saat dijalankan ulang, tidak permanent.
Jika ingin membuatnya permanent (misal autostart saat boot), gunakan systemd service atau cron @reboot.

🔹 Fungsi Script
  Menampilkan INTERNET ACCESS jika terhubung internet.
  Menampilkan CAN'T CONNECT INTERNET jika tidak ada koneksi.
  Update tiap 5 detik.
