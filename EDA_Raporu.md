## Data Science Intern Case Study — EDA Raporu

### Veri Kümesi
- Toplam gözlem: 2235 (temizleme/ayıklama sonrası analizde ~1307 satır aktif)
- Değişken sayısı: 13
- Hedef değişken: `TedaviSuresi` (seans)
- `HastaNo` analizden çıkarıldı.

### Önişleme
- `TedaviSuresi`, `UygulamaSuresi`: birimler temizlenip sayısala dönüştürüldü.
- Tam duplike satırlar kaldırıldı.
- Kategoriklerde trim; nadir sınıflar (~%1 altı) `Diğer` altında birleştirildi.

### Eksik Veri
- Toplam eksik hücre ≈ %10.
- Öne çıkan eksikler: `Alerji` 540, `KanGrubu` 365, `KronikHastalik` 345, `UygulamaYerleri` 157, `Cinsiyet` 104, `Bolum` 7.
- Hedefte eksik yok. Eksik veri ısı haritasıyla incelendi.

### Hedef Değişken: TedaviSuresi
- Özet (aktif örneklem): Ortalama ≈ 14.23, Medyan 15, Min 1, Max 37.
- Histogram, boxplot ve `log1p` histogram ile dağılım kontrol edildi.

### Sayısal İlişkiler ve Korelasyon
- İncelenen sayısallar: `Yas`, `UygulamaSuresi`, `TedaviSuresi`.
- Korelasyonlar zayıf-orta; güçlü kolinearite yok.
- `Yas` vs `TedaviSuresi` saçılımında belirgin doğrusal ilişki yok.

### Kategorik Dağılımlar ve Hedefle İlişki
- `Cinsiyet`: Kadın ~723, Erkek ~480 (eksikler hariç). Medyan hedef benzer.
- `KanGrubu`: 8 sınıf; nadirler birleştirildi.
- `Uyruk`: Türkiye baskın; nadir ülkeler mevcut.
- `Bolum`: Büyük çoğunluk `Fiziksel Tıp Ve Rehabilitasyon,Solunum Merkezi`. İlk 10 bölüm için hedef medyanları karşılaştırıldı.
- `TedaviAdi`: 200+ farklı değer; Top-10 için hedef medyanları karşılaştırıldı. Tedavi adı protokol süresini yansıtabileceği için sızıntı riski not edildi.

### Karmaşık Metin Alanları (virgülle ayrılı)
- Sütunlar: `KronikHastalik`, `Alerji`, `Tanilar`, `UygulamaYerleri`.
- Satır başına öğe sayısı özellikleri üretildi: `n_kronikhastalik`, `n_alerji`, `n_tanilar`, `n_uygulamayerleri`.
- En sık 10 terim listeleri çıkarıldı (ör. `Tanilar`: DORSALJİ, DİĞER…; `UygulamaYerleri`: Bel, Boyun…).

### Aykırı Değerler (IQR)
- `Yas`: 2, 92 gibi uçlar klinik olarak mümkün; otomatik çıkarma önerilmez.
- `TedaviSuresi`: 30+ seans üst uç; protokol kaynaklı olabilir. Winsorize yerine raporlama ve sağlam istatistik önerilir.
- `UygulamaSuresi`: 45 dk üst uç kümelenmesi; protokol etkisi olası.

### Model-İçin Hazır Veri Önerisi
- Hedef: `TedaviSuresi` (tamsayı)
- Örnek özellik seti:
  - Sayısal: `Yas`, `UygulamaSuresi`, `n_kronikhastalik`, `n_alerji`, `n_tanilar`, `n_uygulamayerleri`.
  - Kategorik (azaltılmış sınıf): `Cinsiyet`, `KanGrubu`, `Uyruk`, `Bolum`.
  - Not: `TedaviAdi` dahil edilirse klinik onay önerilir (sızıntı/protokol etkisi).
- Önerilen çıktılar: `data/cleaned.csv`, `data/cleaned.parquet`.

### Öneriler — Sonraki Adımlar
- Eksik stratejisi: kategorikler için `Eksik`/`Diğer`, sayısallar için medyan veya klinik uygun değer.
- Özellik mühendisliği: çoklu-seçim sütunlarından en sık 10–20 terim için ikili bayraklar; mevcut sayım özellikleri kullanılsın.
- Kodlama: ağaç tabanlılar için doğrudan; lineer modeller için one-hot (nadirler birleştirildikten sonra).
- Aykırı yönetimi: sağlam metrikler veya quantile-regression; otomatik kırpma önerilmez.
- Klinik validasyon: `TedaviAdi`/`Bolum` etkilerinin uzman onayı.

### Kısa Sonuç
- Veri temizlendi, tutarlılık sağlandı, hedef sayısala çevrildi; duplikeler kaldırıldı, eksikler raporlandı, kategorikler sadeleştirildi, metin alanlarından özet özellikler türetildi ve ilişkiler görselleştirildi. Modellemeye hazır bir temel oluşturuldu.
