# 🧠 Sistem Pakar Diagnosa Penyakit Menggunakan Experta

Program ini merupakan sistem pakar sederhana berbasis aturan (rule-based) yang dibangun menggunakan pustaka **[experta](https://github.com/noxdafox/experta)** dalam bahasa Python. Sistem ini membantu mendiagnosa penyakit berdasarkan gejala yang dialami pengguna.

---

## 📦 Instalasi

Sebelum menjalankan kode, pastikan kamu telah menginstal dependensi berikut:

```bash
!pip install experta
!pip install --upgrade frozendict
```

## 🚀 Cara Menjalankan

Simpan kode Python ke file bernama main.py.

1. Jalankan file tersebut di Jupyter Notebook, Google Colab, atau langsung dari terminal menggunakan Python.
2. Program akan menampilkan serangkaian pertanyaan terkait gejala.
3. Jawab setiap pertanyaan dengan yes atau no.
4. Setelah semua gejala dikonfirmasi, sistem akan menampilkan hasil diagnosis berdasarkan aturan yang cocok.

## 💬 Gejala yang Ditanyakan
Berikut adalah daftar gejala yang akan ditanyakan oleh sistem:
- Cough (Batuk)
- Fever (Demam)
- Fatigue (Kelelahan)
- Breathing Difficulty (Sulit bernapas)
- Sneezing (Bersin)
- Runny Nose (Hidung meler)
- Sore Throat (Sakit tenggorokan)
- Loss of Taste or Smell (Kehilangan penciuman/perasa)
- Itchy Eyes (Mata gatal)
- Wheezing (Mengi)
- Swollen Tonsils (Amandel bengkak)

## 📌 Catatan Penting
- Jawaban hanya bisa berupa yes atau no (tidak case-sensitive).
- Sistem menggunakan pendekatan rule-based, sehingga bisa memberikan lebih dari satu diagnosis jika gejala yang diberikan cocok dengan lebih dari satu penyakit.
- Program tidak menggantikan diagnosis medis profesional. Gunakan hanya sebagai referensi awal.

