import re
from datetime import datetime, timedelta

# Teks contoh
teks = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."

# Pola regex untuk mencocokkan tanggal dengan format YYYY-MM-DD
pola = r"\d{4}-\d{2}-\d{2}"

# Mencari semua tanggal dalam teks
tanggal = re.findall(pola, teks)

# Mengubah format tanggal menjadi DD-MM-YYYY dan menghitung selisih dengan tanggal sekarang
hasil = []
for t in tanggal:
    t_datetime = datetime.strptime(t, "%Y-%m-%d")
    selisih = (datetime.now() - t_datetime).days
    t_formatted = t_datetime.strftime("%d-%m-%Y %H:%M:%S")
    hasil.append(f"{t_formatted} selisih {selisih} hari")

# Menampilkan hasil
for h in hasil:
    print(h)