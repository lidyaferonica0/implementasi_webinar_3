
import math
import pandas as pd
import folium
from folium.plugins import Fullscreen

# ==========================================
# WEBGIS PEMETAAN ASET INFRASTRUKTUR
# Studi kasus: Kota Bengkulu
# Data contoh untuk demonstrasi
# ==========================================

data_aset = [
    {
        "nama": "Fasilitas Pendidikan A",
        "kategori": "Pendidikan",
        "latitude": -3.7865,
        "longitude": 102.2784,
        "kondisi": "Baik"
    },
    {
        "nama": "Fasilitas Kesehatan A",
        "kategori": "Kesehatan",
        "latitude": -3.8130,
        "longitude": 102.3005,
        "kondisi": "Baik"
    },
    {
        "nama": "Fasilitas Pendidikan B",
        "kategori": "Pendidikan",
        "latitude": -3.8000,
        "longitude": 102.2850,
        "kondisi": "Perlu pemeriksaan"
    },
    {
        "nama": "Taman Kota A",
        "kategori": "Ruang Terbuka",
        "latitude": -3.8050,
        "longitude": 102.2700,
        "kondisi": "Baik"
    },
    {
        "nama": "Fasilitas Kesehatan B",
        "kategori": "Kesehatan",
        "latitude": -3.7950,
        "longitude": 102.2650,
        "kondisi": "Perlu pemeriksaan"
    },
    {
        "nama": "Infrastruktur Jalan A",
        "kategori": "Infrastruktur Jalan",
        "latitude": -3.8100,
        "longitude": 102.2800,
        "kondisi": "Perlu perbaikan"
    },
    {
        "nama": "Taman Kota B",
        "kategori": "Ruang Terbuka",
        "latitude": -3.7900,
        "longitude": 102.2900,
        "kondisi": "Baik"
    },
    {
        "nama": "Infrastruktur Jalan B",
        "kategori": "Infrastruktur Jalan",
        "latitude": -3.7980,
        "longitude": 102.2750,
        "kondisi": "Baik"
    }
]

df = pd.DataFrame(data_aset)


# Menghitung jarak geografis menggunakan rumus Haversine
def hitung_jarak(lat1, lon1, lat2, lon2):
    radius_bumi = 6371  # kilometer

    lat1, lon1, lat2, lon2 = map(
        math.radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_bumi * c


# Mencari aset terdekat untuk setiap aset
nama_terdekat = []
jarak_terdekat = []

for i, aset in df.iterrows():
    kandidat = []

    for j, pembanding in df.iterrows():
        if i == j:
            continue

        jarak = hitung_jarak(
            aset["latitude"],
            aset["longitude"],
            pembanding["latitude"],
            pembanding["longitude"]
        )

        kandidat.append((pembanding["nama"], jarak))

    nama, jarak = min(kandidat, key=lambda item: item[1])
    nama_terdekat.append(nama)
    jarak_terdekat.append(round(jarak, 3))

df["aset_terdekat"] = nama_terdekat
df["jarak_terdekat_km"] = jarak_terdekat


# Membuat peta interaktif


peta = folium.Map(
    location=[-3.8000, 102.2800],
    zoom_start=13,
    tiles="https://tile.openstreetmap.de/{z}/{x}/{y}.png",
    attr="© OpenStreetMap contributors"
)



Fullscreen().add_to(peta)

warna_kategori = {
    "Pendidikan": "blue",
    "Kesehatan": "red",
    "Ruang Terbuka": "green",
    "Infrastruktur Jalan": "orange"
}

for kategori in df["kategori"].unique():
    layer = folium.FeatureGroup(name=kategori)

    data_kategori = df[df["kategori"] == kategori]

    for _, aset in data_kategori.iterrows():
        popup_html = f"""
        <b>{aset['nama']}</b><br>
        Kategori: {aset['kategori']}<br>
        Kondisi: {aset['kondisi']}<br>
        Aset terdekat: {aset['aset_terdekat']}<br>
        Jarak terdekat: {aset['jarak_terdekat_km']} km
        """

        folium.CircleMarker(
            location=[
                aset["latitude"],
                aset["longitude"]
            ],
            radius=7,
            color=warna_kategori[kategori],
            fill=True,
            fill_color=warna_kategori[kategori],
            fill_opacity=0.8,
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=aset["nama"]
        ).add_to(layer)

    layer.add_to(peta)

folium.LayerControl(collapsed=False).add_to(peta)

# Menyimpan hasil
peta.save("peta_aset_bengkulu.html")
df.to_csv("analisis_aset_bengkulu.csv", index=False)

# Menampilkan ringkasan di terminal
print("=" * 50)
print("SISTEM INFORMASI GEOGRAFIS ASET INFRASTRUKTUR")
print("=" * 50)
print(f"Jumlah aset       : {len(df)}")
print("\nJumlah aset per kategori:")
print(df["kategori"].value_counts().to_string())

print("\nJumlah aset berdasarkan kondisi:")
print(df["kondisi"].value_counts().to_string())

print("\nAnalisis jarak aset terdekat:")
print(
    df[["nama", "aset_terdekat", "jarak_terdekat_km"]]
    .to_string(index=False)
)

print("\nFile berhasil dibuat:")
print("- peta_aset_bengkulu.html")
print("- analisis_aset_bengkulu.csv")
print("\n data merupakan data ilustratif.")
