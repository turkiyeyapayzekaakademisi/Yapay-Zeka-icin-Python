# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================

ad = "Kaan"
yas = 25
ortalama = 3.45

print("SORU 1 ÇÖZÜM:")
print(type(ad))
print(type(yas))
print(type(ortalama))
print("-" * 50)

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================

print("SORU 2 ÇÖZÜM:")
yas_str = input("Yaşınızı girin: ")
print("Gelen veri tipi:", type(yas_str))

yas_int = int(yas_str)
print("5 yıl sonra yaş:", yas_int + 5)
print("-" * 50)


# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================

print("SORU 3 ÇÖZÜM:")
fiyat = float(input("Ürün fiyatını girin (örn: 99.90): "))
kdv = fiyat * 0.18
toplam = fiyat + kdv
print("KDV:", round(kdv, 2))
print("Toplam:", round(toplam, 2))
print("-" * 50)

# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================

print("SORU 4 ÇÖZÜM:")
sayilar = [10, 20, 30, 40, 50]
print("İlk eleman:", sayilar[0])
print("Son eleman:", sayilar[-1])
print("2. indexten sonrası:", sayilar[2:])

sayilar.append(60)
print("60 eklendi:", sayilar)

sayilar.remove(20)
print("20 silindi:", sayilar)
print("-" * 50)

# ============================================================
# SORU 5
# Bir tuple oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================

print("SORU 5 ÇÖZÜM:")
koordinat = (12, 34)
x, y = koordinat
print("x:", x)
print("y:", y)

# koordinat[0] = 99  # Bu satır hata verir çünkü tuple immutable (değiştirilemez)
print("-" * 50)

# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================

print("SORU 6 ÇÖZÜM:")
ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
print("İsim:", ogrenci["isim"])

ogrenci["not"] = 90
ogrenci["yas"] = 23

print("Güncel sözlük:", ogrenci)
print("Anahtarlar:", list(ogrenci.keys()))
print("Değerler:", list(ogrenci.values()))
print("-" * 50)

# ============================================================
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================
print("SORU 7 ÇÖZÜM:")
liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
benzersiz_isimler = set(liste)
print("Benzersiz isimler:", benzersiz_isimler)
print("Benzersiz isim sayısı:", len(benzersiz_isimler))
print("-" * 50)