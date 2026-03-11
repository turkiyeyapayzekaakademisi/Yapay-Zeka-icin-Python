"""
- Değişken Kavramı: veriyi saklamak için kullandığımız isimlendirilmiş bir alandır.
    - değişken = bilgiyi tuttuğumuz kutu
    - değişkenlerin isimlendirme kuralları:
        - rakamla başlanmaz: 1_var = 
        - boşluk içermer kaan hoca = 
        - özel karakter içermez önemli_değişken
        - büyük küçük harf duyarlıdır degisken ile Degisken aynı değildir neden çünkü d-D farklı harflerdir ve büyük-küçük harf duyarlılığı vardır.
- Integer: tam sayıları temsil eden değişken tipimiz. 
- float: ondalıklı sayıları temsil eder.
- string: metinsel verileri temsil eder
- Veri tipi kontrolü ve Tip dönüşümleri: bir değişkenin hangi veri tipinde olduğunu öğrenmek ve veri tipleri arasında dönüşüm yapmak
- liste: birden fazla veriyi tel bir değişken içerisinde saklamamızı sağlar
    - indeksleme ve slicing
    - list metotları
- tuple: birden fazla veriyi saklayan bir veri yapısıdır, tuple değiştirilemez.
- sözlük (dictionary): verileri anahtar-değer (key-value) mantığıyla saklar.
- set: benzersiz yani unique elemanlardan oluşan bir veri yapısıdır. Aynı elemandan birden fazla kez olamaz.
- veri yapıları arasındaki farklar: liste, tuple, sözlük, set
"""

# integer (int)
# yaş =  özel karakter içeriri
# 1_yas = rakamla baslanmaz
# ogrenci yas = boşluk içermez

yas = 35
ogrenci_sayisi = 55000
sicaklik = -15 

print(yas)
print(35)

# hesaplama
a = 10
b = 5 

toplam = a + b # a ve b değerlerini toplamış oluruz
print(toplam)

carpma = a * b
print(carpma)

cikarma = a - b
print(cikarma)

bolme = a/b
print(bolme)

# gercek hayat örneği: ürün sayısı var ve her bir ürünün birim fiyatı, amaç: toplam ürün fiyatı
urun_sayisi = 8 # 8 adet ürün var
birim_fiyat = 10 # birim fiyat 10 tl

toplam = urun_sayisi * birim_fiyat
print(toplam)

# # zam uygulaması
# birim_fiyat = 10 # ürünün birim fiyatı 10 tl
# yuzde = int(input("Yüzdeyi yazın: "))
# print(yuzde)
# zamli_fiyat = birim_fiyat + birim_fiyat*yuzde/100
# print(zamli_fiyat)

# float
pi = 3.14
# pi = 3,14bu yanlış
sicaklik = 35.5
urun_fiyati = 99.99

print(sicaklik)

# matematiksel işlemler
a = 3.5
b = 2.0 

print(a + b) # toplama
print(a/b) # bolme

# ondalık hassasiyeti
print(0.1 + 0.2) # 0.3 -> 0.30000000000000004

# yuvarlama (round)
sonuc = 0.1 + 0.2
print(sonuc)

sonuc_yuvarlanmis = round(sonuc, 2)
print(sonuc_yuvarlanmis)

# # proje: gelen fiyat üzerinden kdv (%20) hesapla
# fiyat = float(input("Fiyat Girin: "))
# print(fiyat)
# kdvli_fiyat = fiyat + 20*fiyat/100
# print(kdvli_fiyat)

# string
isim = "kaan" # çift tırnak örneği
sirket = 'ucanble' # tek tırnak örneği

bilgi = "kaan hocanın şirketinin ismi ucanble teknoloji"
print(bilgi)

# string birleştirme (concatenation)
isim = "kaan"
sirket = 'ucanble'
bilgi2 = isim + " hocanın şirketinin ismi " + sirket + " " + "teknoloji"
print(bilgi2)

# string ve sayı birleştirme
yas = 35 # int
int_to_str = str(yas) # 35 -> "35"
isim = "kaan" # string
sonuc = isim + " hocanın yaşı: " + int_to_str # kaan hocanın yaşı: 35
print(sonuc)

kurulum_tarihi = 2023
print("Ucanble teknoloji " + str(kurulum_tarihi) +  " yılında kurulmuştur.")
print(f"Ucanble teknoloji {kurulum_tarihi} yılında kurulmuştur.") # f string

accuracy = 95
print(f"Karar ağacı accuracy: {accuracy} %")

# string indexleme
kelime = "python" # string = karakter dizisi
print(kelime[0])
print(kelime[3])

# string metotları
metin = "PythoN"
metin_kucuk_harf = metin.lower()
print(metin_kucuk_harf)

# uzunluk bulma
metin = "python"
metin_uzunlugu = len(metin)
print(metin_uzunlugu)

# yer değiştirme
metin = "python"
print(metin.replace("o", "O"))

# veri tipi kontrolü
x = 10
print(type(x)) # <class 'int'>

x = "10"
print(type(x)) # <class 'str'>

# print("25" + 5) # TypeError: can only concatenate str (not "int") to str

# tip dönüşümleri (casting)
x = "25" # str
print(type(int(x))) # <class 'int'>
print(type(float(x))) # <class 'float'>

x = 35
print(type(str(x))) # <class 'str'>

# sayi = int(input("Bir sayı girin: ")) # input fonksiyonu çıktısı ne olabilir int? str?
# print(sayi) # 45 int? str? 
# print(type(sayi)) # <class 'str'>

# print(int("abc")) # ValueError: invalid literal for int() with base 10: 'abc'

# listeler
# liste tanımlaması köşeli parantez ile gerçekleşir
sayilar = [1, 2, 3, 4, 5, 6] # integer listesi
isimler = ["kaan", "can", "ucanble", "yılmaz"] # string listesi
karisik = ["kaan", 1, "can", "ucanble", 55, 65.5] # farklı veri tiplerini aynı anda tutabilir.

print(karisik) # ['kaan', 1, 'can', 'ucanble', 55, 65.5]

# liste indeksleme: listelerde indeks 0 dan başlar
meyveler = ["elma", "muz", "kivi"]

print(meyveler[0]) # elma
print(meyveler[2]) # kivi
print(meyveler[-1]) # kivi

# liste uzunluğu
print(len(meyveler)) # 3

# listelerde slicing
sayilar = [10, 20, 30, 40, 50, 60]
print(sayilar[1:4]) # 20, 30, 40   [a:b] a dahil, b dahil değil
print(sayilar[0:3]) # ilk 3 eleman 10, 20, 30
print(sayilar[:3]) # ilk 3 eleman 10, 20, 30
print(sayilar[2:]) # 30dan sonrası [30, 40, 50, 60]

# listeye eleman eklemek
sayilar = [1, 2, 3]
sayilar.append(4)
print(sayilar) # [1, 2, 3, 4]

sayilar.insert(1, 100)
print(sayilar) # [1, 100, 2, 3, 4]

sayilar.remove(100) # eleman silme
print(sayilar) # [1, 2, 3, 4]

sayilar.pop() # en son indekste bulunan değer çıkartılır
print(sayilar) # [1, 2, 3]

sayilar.pop(0) # belirli bir indeks silme
print(sayilar) # [2, 3]

sayilar[0] = 999 # belirli bir indeksde ki değeri bşka bir değer ile değiştir
print(sayilar) # [999, 3]

# tuple -> ()
koordinat = (10, 20)
renkler = ("kırmızı", "mavi", "yeşil")

# liste vs tuple
liste = [1, 2, 3]
liste[0] = 99 # çalışır
print(liste) # [99, 2, 3]

tup = (1, 2, 3)
# tup[0] = 99 # TypeError: 'tuple' object does not support item assignment

# indeksleme
t = (10, 20, 30)
print(t[1]) # 20
print(t[-1]) # 30

# slicing
t = (10, 20, 30, 40)
print(t[1:3]) # (20, 30)

# tek elemanlı tuple
x = (5) # x = 5
print(type(x)) # tuple? int? cevap <class 'int'>

x = (5,)
print(type(x)) # <class 'tuple'>

# tuple unpacking 
koordinat = (10, 20)
x, y = koordinat
print(x) # 10
print(y) # 20

# tuple metotları
t = (20, 20, 30, 40)

print(t.count(20)) # 2
print(t.index(30)) # 2

# sözlük (dictionary)
ogrenci = { # isim = anahtar, ali = key değeri -> {anahtar: değer}
    "isim": "ali", 
    "yas": 25,
    "bolum": "bilgisayar"
}

print(ogrenci)

# dictionary ye erişim
print(ogrenci["isim"]) # ali
print(ogrenci["yas"])

# dictionary yeni değer ekleme
ogrenci["not"] = 85
print(ogrenci) # {'isim': 'ali', 'yas': 25, 'bolum': 'bilgisayar', 'not': 85}

# dictionary değer güncelleme
ogrenci["yas"] = 26
print(ogrenci) # {'isim': 'ali', 'yas': 26, 'bolum': 'bilgisayar', 'not': 85}

# dictionary eleman silme
del ogrenci["bolum"]
print(ogrenci) # {'isim': 'ali', 'yas': 26, 'not': 85}

# anahtarları ve değerleri al
print(ogrenci.keys()) # anahtarlar
print(ogrenci.values()) # değerler
print(ogrenci.items()) # anahtar - değer 

"""
dict_keys(['isim', 'yas', 'not'])
dict_values(['ali', 26, 85])
dict_items([('isim', 'ali'), ('yas', 26), ('not', 85)])
"""

# set
sayilar = {1, 2, 3, 4}
print(sayilar) # {1, 2, 3, 4}

# set tekrar eden elemanlar
sayilar = {1, 2, 2, 3, 3, 3}
print(sayilar) # {1, 2, 3}

# set özellikleri: setler sırasızdır yani indeksi yoktur
# print(sayilar[2]) # TypeError: 'set' object is not subscriptable

# listeyi set e çevirme
liste = [1, 2, 2, 3, 4, 4]
benzersiz = set(liste)
print(benzersiz) # {1, 2, 3, 4}

# set eleman ekleme
sayilar.add(5)
print(sayilar) # {1, 2, 3, 5}

# set eleman silme
sayilar.remove(2)
print(sayilar) # {1, 3, 5}

# set işlemleri
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # birleşim {1, 2, 3, 4, 5}
print(a.intersection(b)) # kesişim {3}
print(a.difference(b)) # fark {1, 2}

"""
liste:
    - sıralıdır, değiştirilebilir, tekrar eden elemanlara izin verir
    - liste = [1, 2, 3]
    - kullanım: eleman sırası önemliyse, veri güncellenecekse
    - numpy array in temelini oluşturmaktadır

Tuple:
    - sıralıdır, değiştirilemez, tekrar eden elemanlara izin verir
    - tuple = (1, 2, 3, 4)    
    - kullanım: veri sabit kalacaksa, güvenli yapı gerekiyorsa

dictionary:
    - anahtar-değer (key-value pair)
    - anahtarlar benzersizdir
    - değerler tekrar edebilir
    - değiştirilebilir
    - ogrenci = {"isim":"kaan", "yas": 35}
    - anlamlı veri saklamak, etiketli veri tutmak
    - pandas dataframe temelini oluşturur

Set:
    - sırasızdır, tekrar eden elemanları kabul etmez, değiştirilebilir
    - set = {1, 2, 3, 4}
    - kullanım: tekrar eden değerleri temizlemek için, küme işlemleri yapmak için
"""
