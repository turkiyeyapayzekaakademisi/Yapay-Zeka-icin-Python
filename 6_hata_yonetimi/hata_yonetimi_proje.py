"""
Bozuk veri temizleme
veri:
        70
        85
        abc
        90
        50
        hata
        60
Amaç:
    - dosyayı oku
    - sayıya çevrilemeyen satıları atla
    - geçerli notları topla
    - ortalama hesapla
"""

notlar = [] # notları saklamak için
hata_sayisi = 0 # hata sayisini tespit etmek için

with open("notlar.txt", "r", encoding="utf-8") as dosya:

    for satir in dosya:

        try: 
            not_degeri = int(satir.strip()) # satir eşit değildir int ise burada hata olacak
            notlar.append(not_degeri)
        except ValueError:
            print(f"Hatalı veri bulundu: {satir.strip()}")
            hata_sayisi += 1 # dosyada hatalı satir sayısı

print(f"notlar: {notlar}") # [70, 85, 90, 50, 60]
print(f"hata_sayisi: {hata_sayisi}") #  2

ortalama = sum(notlar) / len(notlar)

print(f"ortalama: {ortalama}")