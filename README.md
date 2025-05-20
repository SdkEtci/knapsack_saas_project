# Knapsack SaaS Uygulaması

Bu proje, Knapsack problemini çözen ve sonuçları görselleştiren bir SaaS uygulamasıdır.

## Yapı
- `backend/`: Flask kullanarak REST API ve frontend sunucusu sağlar
- `frontend/`: Chart.js ile görselleştirilmiş sonuçları gösterir
- `data/`: Knapsack problemi için örnek veri seti içerir

## Kurulum

### 1. Sanal Ortam Oluşturma ve Paketlerin Kurulumu
```bash
# Backend dizinine git
cd backend

# Sanal ortam oluştur
python3 -m venv venv

# Sanal ortamı aktifleştir
source venv/bin/activate

# Gerekli paketleri yükle
pip install flask flask-cors pandas numpy
```

### 2. Uygulamayı Çalıştırma
```bash
# Backend dizininde olduğunuzdan emin olun
cd backend

# Sanal ortamı aktifleştir
source venv/bin/activate

# Flask uygulamasını başlat
python app.py
```

Uygulama varsayılan olarak `http://localhost:5000` adresinde çalışacaktır.

## Kullanım
1. Tarayıcınızda `http://localhost:5000` adresine gidin
2. Sayfa otomatik olarak:
   - Toplam bütçe ve zaman bilgilerini
   - Her iki strateji (Benefit ve Efficiency) için:
     - Toplam proje sayısı
     - Toplam maliyet
     - Toplam fayda
     - Kalan bütçe
   - Görsel grafikler
   bilgilerini gösterecektir.

## Teknolojiler
- Backend: Flask, Pandas, NumPy
- Frontend: HTML, JavaScript, Chart.js
- Veri İşleme: Pandas, NumPy
