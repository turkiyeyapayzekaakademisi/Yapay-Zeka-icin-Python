"""
Class Nedir?    
    - bir nesnenin (object) nasıl olacağını tanımlayan bir şablondur.
    - class bir taslak yada plan gibidir
    - öğrenci:
        - isim, yaş, bmlüm 
        - ders çalışmak, sınava girmek 

Class tanımlama: Ogrenci > class ismi
class Ogrenci:
    pass
    
Class neden kullanırız?
    - kodun daha düzenli olması için
    - kod tekrarını azaltır
    - büyük projelerde yönetimi kolaylaştırır
    - scikit learn -> en önemli machine learning kütüphanesi -> LinearRegression() class tanımlamış olur.

Neler Öğreneceğiz?
    - __init__ metodu (initializer): nesne oluşturulduğunda otomatik olarak çalışan özel bir metottur. (kurucu metod)
    - attribute ve method
    - object oluşturma
    - Mini proje
"""

"""
Ogrenci class
    - isim
    - yaş
"""

class Ogrenci:

    def __init__(self, isim, yas): # self = oluşturulan nesneyi temsil eder, isim ve yaş başlangıç parametrelerimiz
        print(f"Yeni bir öğrenci oluşturuluyor: isim: {isim}, yaş: {yas}")

# nesne (object) oluşturma
ogrenci1 = Ogrenci("Ali", 21)

"""
Attribute bir class a veya nesneye ait özellikleri temsil eden değişkenlerdir.
yani bir nesnenin verilerini tutan yapılarıdır
Öğrenci:
    - isim, yaş ve bölüm: bunlar öğrencinin attribute larıdır.
"""

class Ogrenci:

    def __init__(self, isim, yas):
        self.isim = isim  # isim attribute
        self.yas = yas    # yas attribute

# attribute kullanımı
ogrenci1 = Ogrenci("Ali", 21) 

# ogrenci1 nesnesinin attribute larına nasıl ulaşabiliriz?
print(ogrenci1.isim) # Ali
print(ogrenci1.yas)  # 21

"""
Metot (method): bir class içerisinde tanımlanan fonksiyonlardır
bir nesnenin yapabileceği işlemleri temsil ederler
"""

class Ogrenci:

    def __init__ (self, isim, yas):
        self.isim = isim
        self.yas = yas

    def tanit(self):
        print(f"Merhaba benim adım: {self.isim}")

ogrenci1 = Ogrenci("Ali", 21)
ogrenci2 = Ogrenci("Kaan", 25)

ogrenci1.tanit()
ogrenci2.tanit()

"""
Object oluşturma ve class kullanımı
    - class: şablon -> araba
    - object (nesne): şablondan üretilen yapı (mercedes, audi)

"""
class Kitap: # ad, yazar, sayfa

    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def bilgi_goster(self):
        print(f"Kitap: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa sayısı: {self.sayfa}")

# object oluşturma
kitap1 = Kitap("Python programlama", "Kaan", 500)

# attribute değerlerine erişim
print(kitap1.ad)
print(kitap1.yazar)
print(kitap1.sayfa)

# method
kitap1.bilgi_goster()
"""
Kitap: Python programlama
Yazar: Kaan
Sayfa sayısı: 500
"""

# birden fazla obje oluşturma
kitap1 = Kitap("Python programlama", "Kaan", 500)
kitap2 = Kitap("Python programlamaya Giriş", "Can", 150)
kitap3 = Kitap("Python", "Kaan", 250)

print(kitap2.ad)
kitap3.bilgi_goster()