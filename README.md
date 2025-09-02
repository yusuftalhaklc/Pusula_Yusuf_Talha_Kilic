# Pusula Data Science Intern Case Study

**İsim:** Yusuf Talha Kılıç  
**E-posta:** info@yusuftalhaklc.com

## Proje Özeti

Bu proje, sağlık verileri üzerinde Exploratory Data Analysis (EDA) ve Data Pre-Processing çalışması içerir. Hedef değişken `TedaviSuresi` (seans sayısı) olup, hasta demografik bilgileri, kronik hastalıklar, alerjiler ve tedavi bilgileri analiz edilmiştir.

## Veri Seti Bilgileri

- **Toplam Gözlem:** 1,307 (duplikeler temizlendikten sonra)
- **Değişken Sayısı:** 13
- **Hedef Değişken:** TedaviSuresi (seans)
- **Eksik Veri Oranı:** %9.2

### Ana Değişkenler
- **Demografik:** Yas, Cinsiyet, KanGrubu, Uyruk
- **Sağlık:** KronikHastalik, Alerji, Tanilar
- **Tedavi:** TedaviAdi, UygulamaSuresi, UygulamaYerleri, Bolum
- **Hedef:** TedaviSuresi

## Kurulum ve Çalıştırma

### 1. Ortam Hazırlığı
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -U pip
pip install jupyter pandas numpy seaborn matplotlib openpyxl scikit-learn
```

### 2. Jupyter Notebook Başlatma
```bash
jupyter notebook
```

### 3. Analiz Sırası
1. `notebook/pusula_eda.ipynb` dosyasını açın
2. Hücreleri sırayla çalıştırın
3. EDA sonuçlarını inceleyin
4. Data Pre-Processing bölümünü tamamlayın

## Çıktılar

### Notebook Çıktıları
- Eksik veri analizi ve görselleştirmeleri
- Kategorik değişken dağılımları
- Sayısal değişken korelasyonları
- Aykırı değer tespiti
- Özellik mühendisliği sonuçları

## Ana Bulgular

### Hedef Değişken (TedaviSuresi)
- **Ortalama:** 14.23 seans
- **Medyan:** 15 seans
- **Aralık:** 1-37 seans
- **En Sık:** 15 seans (%71.8)

### Eksik Veri Durumu
- **Alerji:** 540 eksik (%41.3)
- **KanGrubu:** 365 eksik (%27.9)
- **KronikHastalik:** 345 eksik (%26.4)
- **UygulamaYerleri:** 157 eksik (%12.0)
- **Cinsiyet:** 104 eksik (%8.0)

### Kategorik Dağılımlar
- **Cinsiyet:** Kadın (%60.1), Erkek (%39.9)
- **KanGrubu:** 0 Rh+ (%27.0), A Rh+ (%24.6), B Rh+ (%9.5)
- **Uyruk:** Türkiye (%97.0), diğer ülkeler (%3.0)
- **Bolum:** Fiziksel Tıp Ve Rehabilitasyon (%88.5)

### Özellik Mühendisliği
- Çoklu-seçim alanlarından sayım özellikleri üretildi
- Nadir kategoriler "Diğer" altında birleştirildi
- Eksik değerler mod ile dolduruldu
- Kategorik değişkenler One-Hot Encoding ile kodlandı
- Sayısal değişkenler StandardScaler ile ölçeklendi

## Modelleme Hazırlığı

### Ön İşleme Adımları
1. **Eksik Veri Yönetimi:** Kategoriklerde mod, sayısallarda medyan
2. **Kategorik Kodlama:** One-Hot Encoding
3. **Ölçekleme:** StandardScaler
4. **Özellik Mühendisliği:** Çoklu-seçim sayımları
5. **Veri Temizliği:** Duplikeler kaldırıldı, tip dönüşümleri yapıldı

### Model-Ready Veri
- **Boyut:** 1,307 satır × 1,000+ özellik (One-Hot Encoding sonrası)
- **Format:** CSV, Parquet
- **Hedef:** TedaviSuresi (sayısal, 1-37 arası)

## Teknik Detaylar

### Kullanılan Kütüphaneler
- **Veri İşleme:** pandas, numpy
- **Görselleştirme:** matplotlib, seaborn
- **Makine Öğrenmesi:** scikit-learn
- **Dosya İşlemleri:** openpyxl