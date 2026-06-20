# MindCalm PSS-10: Sistem Pakar Analisis Tingkat Stres

MindCalm PSS-10 adalah sebuah aplikasi berbasis web (sistem pakar) yang membantu mahasiswa (atau pengguna umum) mengidentifikasi dan mengukur tingkat stres mereka menggunakan instrumen psikologis standar internasional yang diakui, yaitu **Perceived Stress Scale (PSS-10)**.

Aplikasi ini menggunakan metode *Certainty Factor* (CF) pada sistem pakarnya untuk tidak hanya menghitung skor total stres, tetapi juga menentukan **gejala dominan** yang paling berpengaruh pada kondisi psikologis pengguna beserta tingkat kepastian (CF) dari hasil tersebut.

## ⚠️ Disclaimer
Sistem pakar ini merupakan instrumen *skrining* awal (berdasarkan PSS-10) dan **bukan** sebagai alat diagnosis medis atau klinis yang definitif. Jika Anda atau orang di sekitar Anda membutuhkan pertolongan serius terkait kesehatan mental, harap segera hubungi psikolog, psikiater, atau fasilitas layanan kesehatan terdekat.

## 🚀 Fitur Utama

- **Kuesioner Interaktif PSS-10**: Antarmuka modern yang nyaman untuk mengisi 10 pertanyaan standar PSS-10.
- **Analisis Skor Otomatis**: Secara otomatis menghitung nilai (*scoring*) konvensional PSS-10 (termasuk *reverse scoring* untuk pertanyaan positif).
- **Sistem Pakar dengan Certainty Factor**: Menemukan gejala dominan penyebab stres dan mengukur persentase keyakinan (CF).
- **Interpretasi dan Rekomendasi**: Memberikan tingkat stres (Ringan, Sedang, Berat) beserta saran atau rekomendasi tindakan.
- **Cetak Hasil PDF**: Fitur bagi pengguna untuk menyimpan dan mencetak hasil laporan tes (Ringkasan Klinis) untuk didiskusikan dengan konselor atau psikolog profesional.
- **Responsif dan Modern**: Desain yang indah dan responsif di berbagai perangkat menggunakan Tailwind CSS.

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python 3.x, Flask (Web Framework)
- **Frontend**: HTML5, JavaScript (Vanilla), Tailwind CSS (melalui CDN)
- **Dependency Manager** (Opsional tapi disarankan): `uv` atau `pip`

---

## ⚙️ Persyaratan Sistem (Prerequisites)

Sebelum menjalankan aplikasi ini di komputer Anda, pastikan Anda telah menginstal:
1. **Python** (versi 3.8 atau lebih baru). Bisa diunduh di [python.org](https://www.python.org/downloads/).
2. **Git** (opsional, jika Anda ingin melakukan *clone* repositori).
3. Anda juga disarankan menginstal **`uv`** (sebagai *package manager* Python yang sangat cepat), meskipun menggunakan pip bawaan Python juga tidak masalah.

---

## 📖 Cara Menjalankan Aplikasi (Langkah demi Langkah)

Berikut adalah panduan lengkap cara menjalankan aplikasi ini di komputer lokal Anda:

### Langkah 1: Unduh Kode Program (Clone / Download)
Jika Anda menggunakan Git, jalankan perintah ini di terminal/Command Prompt Anda:
```bash
git clone https://github.com/rakanabiyyu/expertsys_pss10.git
cd expertsys_pss10
```
*(Atau Anda bisa mengunduh file `.zip` dari repositori dan mengekstraknya, lalu buka folder hasil ekstraksi di terminal Anda).*

### Langkah 2: Buat Virtual Environment (Sangat Disarankan)
Untuk menjaga agar dependensi (*library*) aplikasi ini tidak mengganggu *library* Python global di komputer Anda, buat sebuah *Virtual Environment*.

**Pengguna Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Pengguna Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
*(Setelah command ini dijalankan, di terminal Anda akan muncul tulisan `(venv)` yang menandakan Anda sudah berada di dalam virtual environment).*

### Langkah 3: Instal Dependensi
Aplikasi ini menggunakan **Flask** sebagai *framework*. Instal *library* yang dibutuhkan dengan perintah:
```bash
pip install -r requirements.txt
```

*(Jika Anda menggunakan `uv`, Anda bisa menginstal dan menjalankan langsung dengan `uv run app.py` tanpa perlu aktivasi venv secara manual).*

### Langkah 4: Jalankan Aplikasi
Sekarang Anda siap untuk menjalankan web server! Ketik perintah berikut:
```bash
python app.py
```

### Langkah 5: Buka di Browser
Jika berhasil, terminal akan menampilkan pesan bahwa server sedang berjalan (biasanya di port 5000). 
Buka web browser favorit Anda (Chrome, Firefox, Safari) dan ketikkan alamat berikut:
👉 **http://127.0.0.1:5000** atau **http://localhost:5000**

Selamat! Anda sudah bisa menggunakan aplikasi MindCalm PSS-10.

---

## 📂 Struktur Folder Proyek

Penjelasan singkat tentang isi dari proyek ini:
- `app.py`: File utama aplikasi Backend (Flask). Berisi logika perhitungan PSS-10, rute (*routing*), dan metode *Certainty Factor*.
- `requirements.txt`: Daftar pustaka Python (*library*) yang dibutuhkan.
- `templates/`: Folder yang berisi file antarmuka (HTML).
  - `index.html`: Halaman utama (Landing Page).
  - `register.html`: Halaman pendaftaran sebelum mulai tes.
  - `test.html`: Halaman kuesioner yang interaktif.
  - `result.html`: Halaman yang menampilkan hasil tes dan tingkat stres.
  - `print.html`: Format halaman cetak khusus untuk PDF.
  - `education.html`: Halaman informasi dan edukasi tentang manajemen stres.


