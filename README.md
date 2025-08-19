# Raspi Labs 🐍💡

Koleksi **basic Raspberry Pi projects** untuk pemula hingga menengah.  
Fokus pada **display & visual projects**, termasuk OLED, LCD 16x2 I2C, dan eksperimen interaktif sederhana.

---

## 🔹 Daftar Project

| Nama Project         | Deskripsi                               | File/Folder        |
|---------------------|-----------------------------------------|------------------|
| OLED Blink Eye       | Bola mata OLED yang bisa berkedip & bergerak | `oled_eye/`      |
| LCD 16x2 I2C Display | Menampilkan teks sederhana di LCD 16x2 | `lcd_16x2/`      |
| LED Blink           | Blinking LED menggunakan GPIO           | `led_blink/`      |
| Button Input        | Basic input dari tombol dengan GPIO     | `button_input/`   |

---

## 🔹 Setup

1. Clone repo
```bash
git clone https://github.com/username/raspi-labs.git
cd raspi-labs
```

2. Buat virtual environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Jalankan project sesuai foldernya
```
cd oled_eye
python oled_eye.py
```

🔹 Catatan

Pastikan I2C diaktifkan di Raspberry Pi (sudo raspi-config)

Pastikan koneksi hardware sesuai pinout

Semua project bersifat educational / eksperimen
