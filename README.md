# 🧠 Sistem Pakar Rekomendasi Menu & Olahraga Harian (NutriMove Expert)

## 📌 Deskripsi

NutriMove Expert adalah aplikasi berbasis web yang menggunakan pendekatan **Sistem Pakar (Expert System)** untuk memberikan rekomendasi:

* Menu makan harian (pagi, siang, malam)
* Pola olahraga harian
* Alasan berbasis pengetahuan (rule-based reasoning)

Berbeda dengan sistem fuzzy, sistem ini menggunakan **aturan IF–THEN** untuk meniru cara berpikir seorang ahli dalam memberikan rekomendasi kesehatan sederhana.

---

## 🎯 Tujuan Sistem

* Memberikan rekomendasi menu dan olahraga yang sesuai dengan kondisi pengguna
* Meniru proses pengambilan keputusan seorang ahli (rule-based)
* Membantu pengguna memahami *alasan* dari rekomendasi yang diberikan

---

## ⚙️ Teknologi yang Digunakan

* Python
* Flask (Web Framework)
* HTML & CSS (UI/UX)
* Rule-Based System (IF–THEN)

---

## 🧠 Konsep Sistem Pakar

Sistem ini terdiri dari:

### 1. Basis Pengetahuan (Knowledge Base)

Berisi kumpulan aturan IF–THEN, contoh:

```text
IF tujuan = turun_berat AND kondisi = berlebih
THEN menu = rendah_kalori AND olahraga = ringan
```

```text
IF tujuan = naik_massa AND kondisi = kurus
THEN menu = tinggi_protein AND olahraga = strength_training
```

---

### 2. Mesin Inferensi (Inference Engine)

Sistem membaca input user, lalu:

* mencocokkan dengan rule
* memilih rule yang paling relevan
* menghasilkan rekomendasi + alasan

---

### 3. User Interface

User mengisi form:

* tujuan
* kondisi tubuh
* aktivitas
* waktu olahraga
* preferensi makanan

---

## 🔄 Alur Sistem

1. User mengisi form konsultasi
2. Sistem membaca input
3. Sistem mencocokkan dengan aturan IF–THEN
4. Sistem menentukan:

   * kategori program
   * menu makan
   * olahraga
5. Sistem menampilkan hasil + alasan

---

## 📊 Input Sistem

| Variabel      | Nilai                                 |
| ------------- | ------------------------------------- |
| Tujuan        | turun_berat / jaga_berat / naik_massa |
| Kondisi Tubuh | kurus / normal / berlebih             |
| Aktivitas     | rendah / sedang / tinggi              |
| Waktu         | sedikit / cukup / banyak              |
| Preferensi    | hemat / normal / tinggi_protein       |

---

## 📈 Output Sistem

* Menu pagi
* Menu siang
* Menu malam
* Rekomendasi olahraga
* Alasan sistem

---

## 🧩 Contoh Kasus

### Input:

* Tujuan: turun_berat
* Kondisi: berlebih
* Aktivitas: rendah
* Waktu: sedikit
* Preferensi: hemat

### Output:

* Menu: rendah kalori (berbasis bahan hemat)
* Olahraga: jalan cepat ringan
* Alasan:

  * kondisi tubuh berlebih
  * aktivitas rendah
  * tujuan penurunan berat badan

---

## 🌐 Struktur Project

```text
project/
├── app.py
└── templates/
    └── index.html
```

---

## 🚀 Cara Menjalankan

1. Install dependency:

```bash
pip install flask
```

2. Jalankan aplikasi:

```bash
python app.py
```

3. Buka browser:

```text
http://127.0.0.1:5002
```

---

## 🔥 Perbedaan dengan Sistem Fuzzy

| Sistem Fuzzy                    | Sistem Pakar                   |
| ------------------------------- | ------------------------------ |
| Menggunakan derajat keanggotaan | Menggunakan aturan IF–THEN     |
| Output numerik (nilai)          | Output berbasis keputusan      |
| Perhitungan matematis           | Penalaran berbasis pengetahuan |
| Lebih fleksibel                 | Lebih deterministik            |

---

## 💡 Kelebihan Sistem

* Mudah dipahami (rule jelas)
* Transparan (ada alasan)
* Cepat dalam pengambilan keputusan
* Cocok untuk edukasi dasar sistem pakar

---

## 📌 Kesimpulan

Sistem ini menunjukkan bagaimana pendekatan sistem pakar dapat digunakan untuk memberikan rekomendasi berbasis pengetahuan manusia secara terstruktur dan transparan, khususnya dalam konteks pola makan dan olahraga harian.
