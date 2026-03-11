# ============================================================
# SORU 1 (IF)
# Kullanıcıdan bir sayı alın.
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
# ============================================================

print("SORU 1 ÇÖZÜM (IF):")
sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")

print("-" * 50)

# ============================================================
# SORU 2 (FOR)
# 1'den 10'a kadar (10 dahil) sayıları yazdırın.
# Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
# ============================================================

print("SORU 2 ÇÖZÜM (FOR):")
toplam = 0

for i in range(1, 11):
    print(i)
    toplam += i

print("Toplam:", toplam)
print("-" * 50)

# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================

print("SORU 3 ÇÖZÜM (WHILE):")
giris = ""

while giris != "q":
    giris = input("Bir şey yazın (çıkmak için q): ")
    if giris != "q":
        print(f"Girdiniz: {giris}")

print("Çıkış yapıldı")
print("-" * 50)

# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

print("SORU 4 ÇÖZÜM (NESTED):")

for i in range(1, 21):
    # İlk kontrol: çift mi tek mi?
    if i % 2 == 0:
        tur = "Çift"
    else:
        tur = "Tek"

    # İkinci kontrol: 10'dan büyük mü?
    if i > 10:
        boyut = "Büyük"
    else:
        boyut = "Küçük/Eşit"

    print(f"{i} -> {tur} - {boyut}")

print("-" * 50)
print("ÖDEV TAMAMLANDI")