import sqlite3
from datetime import datetime

# 1. VERİTABANI BAĞLANTISI VE TABLO OLUŞTURMA
# Bu kod çalıştırıldığında klasöründe otomatik olarak 'kutuphane.db' adında bir veritabanı dosyası oluşur.
conn = sqlite3.connect('kutuphane.db')
cursor = conn.cursor()

# Tabloları kod tarafında da garantiye alıyoruz
cursor.execute('''CREATE TABLE IF NOT EXISTS kitaplar (
    id INTEGER PRIMARY KEY AUTOINCREMENT, baslik TEXT, yazar TEXT, yayin_yili INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS uyeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT, ad TEXT, soyad TEXT, eposta TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS odunc_alma (
    id INTEGER PRIMARY KEY AUTOINCREMENT, kitap_id INTEGER, uye_id INTEGER, odunc_tarihi TEXT)''')
conn.commit()

# 2. CRUD FONKSİYONLARI (İş Mantığı)

def kitap_ekle():
    """CREATE (Ekleme) İşlemi"""
    print("\n--- Yeni Kitap Ekle ---")
    baslik = input("Kitap Adı: ")
    yazar = input("Yazar Adı: ")
    yil = input("Yayın Yılı: ")
    
    cursor.execute("INSERT INTO kitaplar (baslik, yazar, yayin_yili) VALUES (?, ?, ?)", (baslik, yazar, yil))
    conn.commit()
    print(f"'{baslik}' başarıyla eklendi!\n")

def kitaplari_listele():
    """READ (Okuma/Listeleme) İşlemi"""
    cursor.execute("SELECT * FROM kitaplar")
    kitaplar = cursor.fetchall()
    
    print("\n--- KÜTÜPHANEDEKİ KİTAPLAR ---")
    if not kitaplar:
        print("Kütüphanede henüz kitap yok.")
    for k in kitaplar:
        print(f"ID: {k[0]} | Başlık: {k[1]} | Yazar: {k[2]} | Yıl: {k[3]}")
    print("------------------------------\n")

def kitap_sil():
    """DELETE (Silme) İşlemi"""
    kitaplari_listele()
    kitap_id = input("Silmek istediğiniz kitabın ID'sini girin: ")
    
    # Önce kitap var mı kontrol et
    cursor.execute("SELECT * FROM kitaplar WHERE id = ?", (kitap_id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM kitaplar WHERE id = ?", (kitap_id,))
        conn.commit()
        print(f"ID'si {kitap_id} olan kitap başarıyla silindi!\n")
    else:
        print("Bu ID ile eşleşen bir kitap bulunamadı.\n")

def uye_ekle():
    """Üye Ekleme İşlemi"""
    print("\n--- Yeni Üye Kaydı ---")
    ad = input("Üye Adı: ")
    soyad = input("Üye Soyadı: ")
    eposta = input("E-posta Adresi: ")
    
    cursor.execute("INSERT INTO uyeler (ad, soyad, eposta) VALUES (?, ?, ?)", (ad, soyad, eposta))
    conn.commit()
    print(f"{ad} {soyad} başarıyla kütüphaneye üye yapıldı!\n")

def odunc_ver():
    """İlişkili Tablo İşlemi (Ödünç Verme)"""
    print("\n--- Kitap Ödünç Verme İşlemi ---")
    kitap_id = input("Ödünç Verilecek Kitap ID: ")
    uye_id = input("Ödünç Alacak Üye ID: ")
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("INSERT INTO odunc_alma (kitap_id, uye_id, odunc_tarihi) VALUES (?, ?, ?)", (kitap_id, uye_id, tarih))
    conn.commit()
    print("Ödünç verme işlemi başarıyla kaydedildi!\n")

# 3. KULLANICI ARAYÜZÜ (CLI Menü)
def ana_menu():
    while True:
        print("======== OSTIMTECH KÜTÜPHANE SİSTEMİ ========")
        print("1. Kitap Ekle (Create)")
        print("2. Kitapları Listele (Read)")
        print("3. Kitap Sil (Delete)")
        print("4. Yeni Üye Ekle")
        print("5. Kitap Ödünç Ver")
        print("6. Sistemden Çıkış")
        print("=============================================")
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-6): ")
        
        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            kitap_sil()
        elif secim == "4":
            uye_ekle()
        elif secim == "5":
            odunc_ver()
        elif secim == "6":
            print("Sistemden çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-6 arasında bir değer girin.\n")

if __name__ == "__main__":
    ana_menu()
    conn.close()