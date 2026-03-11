"""
Kontrol yapıları nedir?
    - programın çalışma akışını koşullara bağlı olarak değiştirmesini sağlayan yapılardır
    - kontrol yapıları sayesinde program koşul doğruysa bir kod bloğunu veya koşul yanlış ise başka bir kod bloğunu çalıştırabilir

"""

"""
if yapısı: bir koşul doğruysa kod bloğunu çalıştırır

if kosul:
    yapilacak_islem
"""

sayi = 10 
if sayi > 0: # koşul: eğer sayı 0 dan büyükse
    print("Sayı pozitiftir.") # eğer bu koşul = doğru ise print fonksiyonu çağrılır

# if sayi > 0:
# print("burası çalşmaz.") # IndentationError: expected an indented block after 'if' statement on line 19

# if else yapısı: else koşul yanlış ise çalışır
sayi = -3

if sayi > 0:
    print("pozitif")
else:
    print("pozitif değil")

# if - elif - else: ilk doğru koşul çalışır, diğerleri kontrol edilmez, hiç biri doğru değilse else çalışır

ogrenci_not = 72
if ogrenci_not > 85:
    print("A")
elif ogrenci_not > 70:
    print("B")
elif ogrenci_not > 50:
    print("C")
else:
    print("F")

# mantıksal operatörler: birden fazla koşulun birleşmesi

yas = 20
ogrenci = True # boolean

# eğer öğrencinin yaşı 25 den küçükse ve öğrenci ise öğrenci indirimi uygula
if yas < 25 and ogrenci == True:
    print("Öğrenci indirimi uygula")

if yas < 25 or ogrenci == True: # yaşı 25 ten küçükse veya öğrenci ise 
    print("Öğrenci indirimi uygula")


# if ve liste kullanımı
meyveler = ["elma", "armut", "muz"]

if "elma" in meyveler:
    print("elma listede var")
else:
    print("elma listede yok")

# stok kontrol örneği

meyveler = ["elma", "armut", "muz"]

urun = input("Bir meyve girin: ")

if urun in meyveler:
    print("Stokta var")
else:
    print("Stokta yok")