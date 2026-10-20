# Studi Kasus Webinar 3 – Sistem Informasi Geografis (GIS) untuk Pemetaan Aset Infrastruktur

## Deskripsi
Program ini merupakan implementasi materi webinar tentang penerapan teknologi informasi dalam bidang Geographic Information System (GIS). Studi kasus yang digunakan adalah pemetaan dan analisis persebaran aset infrastruktur di Kota Bengkulu.

Program dikembangkan menggunakan Python untuk menampilkan lokasi aset pada peta interaktif, mengelompokkan aset berdasarkan kategori, menampilkan informasi kondisi aset, serta menghitung jarak geografis ke aset terdekat.

Data yang digunakan merupakan data ilustratif untuk keperluan pembelajaran, bukan data resmi aset Pemerintah Kota Bengkulu.

## Tujuan
- Menerapkan GIS untuk memetakan informasi aset berdasarkan koordinat geografis.
- Menampilkan persebaran aset melalui peta interaktif.
- Mengelompokkan aset berdasarkan kategori dan kondisi.
- Menghitung jarak geografis antara setiap aset dan aset terdekat.
- Menyimpan hasil analisis dalam format CSV.

## Teknologi yang Digunakan
- **Python** — bahasa pemrograman utama.
- **Pandas** — mengelola dan menganalisis data aset.
- **Folium** — membuat peta interaktif berbasis web.
- **OpenStreetMap** — menyediakan data peta dasar melalui layanan tile yang digunakan.

## Struktur Proyek

```text
webinar3/
├── webinar_3.py
├── README.md
├── requirements.txt
├── peta_aset_bengkulu.html
└── analisis_aset_bengkulu.csv
```

## Cara Menjalankan

### 1. Persiapan
Pastikan Python sudah terinstal di komputer dan terminal berada di folder `webinar3`.

### 2. Instal dependensi
Jalankan perintah berikut:

```bash
python -m pip install -r requirements.txt
```

### 3. Jalankan program
Eksekusi file Python menggunakan perintah:

```bash
python webinar_3.py
```

### 4. Buka hasil peta
Setelah program selesai, buka file `peta_aset_bengkulu.html` melalui browser untuk melihat peta interaktif.

## Fitur Program
- **Pemetaan aset:** menampilkan delapan data aset ilustratif pada peta Kota Bengkulu.
- **Filter kategori:** memisahkan tampilan aset Pendidikan, Kesehatan, Ruang Terbuka, dan Infrastruktur Jalan.
- **Informasi aset:** menampilkan nama, kategori, kondisi, aset terdekat, dan jarak ketika penanda dipilih.
- **Analisis jarak:** menghitung jarak geografis menggunakan rumus Haversine.
- **Ekspor data:** menyimpan hasil analisis ke file CSV untuk diperiksa atau diolah lebih lanjut.

## Hasil Program

Program menghasilkan dua file utama:

| File | Keterangan |
|---|---|
| `peta_aset_bengkulu.html` | Peta interaktif yang menampilkan lokasi dan informasi aset. |
| `analisis_aset_bengkulu.csv` | Data aset beserta kategori, koordinat, kondisi, aset terdekat, dan jarak geografisnya. |

Ringkasan pengujian dengan data ilustratif:

- Jumlah aset: 8.
- Kategori aset: 4.
- Kondisi baik: 5 aset.
- Perlu pemeriksaan: 2 aset.
- Perlu perbaikan: 1 aset.

## Kesimpulan
Implementasi ini menunjukkan bagaimana GIS dapat digunakan untuk memvisualisasikan persebaran aset, mengelompokkan informasi berdasarkan kategori, dan melakukan analisis jarak geografis. Sistem ini dapat dikembangkan lebih lanjut dengan menambahkan basis data, fitur pengelolaan aset, serta data lapangan yang valid untuk mendukung pengelolaan infrastruktur dan perencanaan kota.
Hasil analisis masih berdasarkan data ilustratif. Jarak yang dihitung merupakan jarak geografis garis lurus, bukan jarak tempuh melalui jaringan jalan. Peta dasar memerlukan koneksi internet agar tile peta dapat dimuat.
