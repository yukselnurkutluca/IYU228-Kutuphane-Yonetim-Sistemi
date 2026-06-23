# IYU 228 İş Yeri Uygulaması - Faz 2 Projesi

## Proje Adı: Kütüphane Yönetim Sistemi

Bu proje, OSTİM Teknik Üniversitesi Bilgisayar Mühendisliği bölümü IYU 228 İş Yeri Uygulaması dersi kapsamında geliştirilmiştir.

## Kullanılan Teknolojiler
- Python 3
- SQLite3 (SQL Veritabanı)
- GitHub

## Proje İçeriği ve Yapısı
Proje, kütüphane yönetim süreçlerini otomatize eden ve ilişkisel veritabanı mantığını kullanan bir CLI (Komut Satırı) uygulamasıdır. İçerisinde hocamızın talep ettiği tüm CRUD işlemleri yer almaktadır:
- **Create (Ekleme):** `kitap_ekle()` ve `uye_ekle()` fonksiyonları ile sisteme dinamik veri eklenir.
- **Read (Listeleme):** `kitaplari_listele()` fonksiyonu veritabanındaki tüm kitap verilerini çeker.
- **Delete (Silme):** `kitap_sil()` fonksiyonu seçilen benzersiz ID'ye göre veritabanından veri temizler.
- **İlişkisel Veritabanı:** `odunc_alma` tablosu üzerinden FOREIGN KEY kullanılarak kitaplar ve üyeler tabloları birbirine bağlanmıştır.

## Çalıştırma Talimatı
Proje dizininde terminal üzerinden aşağıdaki komut çalıştırılarak sistem menüsüne erişilebilir:
`python main.py`
