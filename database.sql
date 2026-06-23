-- 1. KİTAPLAR TABLOSU
-- Kitapların benzersiz ID'sini, başlığını, yazarını ve yayın yılını tutar.
CREATE TABLE IF NOT EXISTS kitaplar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    baslik TEXT NOT NULL,
    yazar TEXT NOT NULL,
    yayin_yili INTEGER
);

-- 2. ÜYELER TABLOSU
-- Kütüphaneye üye olan kişilerin bilgilerini tutar.
CREATE TABLE IF NOT EXISTS uyeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL,
    eposta TEXT
);

-- 3. ÖDÜNÇ ALMA TABLOSU (İlişkisel Yapı)
-- Hangi kitabın (kitap_id) hangi üye tarafından (uye_id) ne zaman alındığını tutar.
CREATE TABLE IF NOT EXISTS odunc_alma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kitap_id INTEGER,
    uye_id INTEGER,
    odunc_tarihi TEXT,
    FOREIGN KEY(kitap_id) REFERENCES kitaplar(id),
    FOREIGN KEY(uye_id) REFERENCES uyeler(id)
);