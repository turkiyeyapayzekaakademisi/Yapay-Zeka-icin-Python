"""
Fonksiyon Nedir?
    - belirli bir işi yapan ve çağrıldığında çalışan kod bloğudur.
    - bir fonksiyon genellikle:
        - girdi (input) 
        - bir işlem yapar
        - sonuç (output) üretir

Kahve makinesi:
    - kahve türünü alır (input)
    - kahveyi hazırlar (işlem)
    - kahveyi verir (output)

girdi -> işlem -> çıktı

1) build in functions: pythonda tanımlı fonksiyonlar
2) user defined functions: developer tanımlar
"""

# print: ekrana çıktı üretir
print("merhaba")
"""
girdi     -> işlem -> çıktı
"merhaba" -> print -> ekrana yazı basılması
"""

# len: bir veri yapısının uzunluğunu verir
liste = [1, 2, 3]
print(len(liste))
"""
girdi: liste
işlem: eleman sayısının hesaplanması
çıktı: 3
"""
# type: bir değişkenin veri tipini verir
x = 3.14
print(type(x)) # <class 'float'>

# veri tipi dönüşüm fonksiyonları: int(), float(), str()
sayi = "10"
print(int(sayi) + 5) # 15

# sum(), max(), min()
sayilar = [ 1, 2, 3, 5]
print(sum(sayilar)) # 11
print(max(sayilar)) # 5
print(min(sayilar)) # 1

# abs()
x = -8
print(abs(x))

# round()
x = 3.56546546546
print(round(x, 3)) # 3.565

# sorted()
sayilar = [5,3,7,1,9,2]
print(sorted(sayilar)) # [1, 2, 3, 5, 7, 9]

# machine learning -> sınıflandırma -> sklearn fit()

# derin öğrenme -> tahmin -> tensorflow predict()