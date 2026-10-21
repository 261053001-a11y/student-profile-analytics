# 🎓 Dashboard Analisis Profil Mahasiswa
link Demo : https://student-profile-analytics-jhxqpiodxdmhdsgrsyxf25.streamlit.app/

> **Bedah Kasus 2: Dataset Profil Mahasiswa (1.000 Data)**  
> **Nama:** Hudzaifah Aini  
> **NIM:** 261053001  

Aplikasi *Dashboard* interaktif berbasis web menggunakan **Streamlit**, **Pandas**, dan **Plotly** untuk memvisualisasikan serta menganalisis data profil dan performa akademik mahasiswa.

---

## 🚀 Fitur Utama Dashboard
1. **Filter Data Interaktif (Sidebar):**
   - Filter berdasarkan **Jurusan** (Sistem Informasi, Manajemen, Teknik Informatika, Akuntansi, Ilmu Komunikasi).
   - Filter berdasarkan **Semester** (Tingkat 1 s.d. 8).
2. **Metrik KPI Utama:**
   - Total Mahasiswa
   - Rata-Rata IPK
   - Rata-Rata Usia
   - Jumlah Jurusan
3. **Visualisasi Data Interaktif (Plotly):**
   - 📊 **Distribusi Mahasiswa per Semester** (*Bar Chart Berurutan*)
   - 🍰 **Proporsi Mahasiswa per Jurusan** (*Donut Chart*)
   - 🔔 **Distribusi IPK Mahasiswa** (*Histogram*)
   - 📦 **Sebaran & Outlier Usia dan IPK** (*Box Plot per Jurusan & Semester*)
4. **Tabel Data Mentah (*Raw Data Table*):** Menampilkan detail profil mahasiswa secara dinamis lengkap dengan format kolom yang disesuaikan.

---

## 📁 Struktur File Repository
- `app.py`: File utama aplikasi dashboard Streamlit.
- `data.py`: Skrip untuk menghasilkan 1.000 data sintesis profil mahasiswa (`dataset_mahasiswa_1000.csv`).
- `dataset_mahasiswa_1000.csv`: Berkas data profil mahasiswa.
- `requirements.txt`: Daftar pustaka/dependencies Python yang dibutuhkan.

---

## 🛠️ Cara Menjalankan Project

1. **Clone repository ini atau unduh file project.**
2. **Install semua dependencies:**
   ```bash
   pip install -r requirements.txt
