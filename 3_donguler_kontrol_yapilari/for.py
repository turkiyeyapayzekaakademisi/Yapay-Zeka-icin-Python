"""
Döngü (loop) nedir?
    - bir işlemi tekrar tekrar yapmamıza sağlayan yapılardır.
    - örn: bir listede ki tüm elemanları yazdırmak

For loop:

for degisken in koleksiyon:
    yapilacak_islem

degisken: her turda (iterasyon) değişen geçici isim
koleksiyon: liste, tuple gibi veri yapıları
"""

# liste ile for döngüsü
sayilar = [10, 20 , 30]

# # mantıksız
# sayi1 = sayilar[0] + 5 # 10 + 5
# sayi2 = sayilar[1] + 5 # 20 + 5
# sayi3 = sayilar[2] + 5 # 30 + 5

for sayi in sayilar:
    print(sayi + 5)

# range fonksiyonu ile for döngüsü
for i in range(5): # [0, 1, 2, 3, 4]
    print(i)

for i in range(1, 7):
    print(i)

# for ile toplama işlemi
sayilar = [10, 20, 30]

# 10 + 20 + 30 -> sayilar[0] + sayilar[1] + sayilar[2]
toplam = 0
for s in sayilar:
    print(s)
    toplam = toplam + s

print(toplam) # 60
"""
                 toplam  s
1. iterasyon        0   10
2. iterasyon        10  20
3. iterason         30  30
toplam = 60

"""

# for + if kullanımı
sayilar = [1,2,3,4,5,6]

for sayi in sayilar:
    if sayi % 2 == 0:
        print(f"Çift: {sayi}")

# string üzerinden for döngüsü
kelime = "ucanble"

for harf in kelime:
    print(harf)