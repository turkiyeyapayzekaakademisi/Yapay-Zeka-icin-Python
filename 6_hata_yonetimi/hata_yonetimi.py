"""
Hata yönetimi: 
    - hata (error) ve ististna (exception) 
    - en sık karşılaşılan hata tipleri

Neden önemli:
    - hata yönetimi programın çökmeden kontrollü bir şekilde çalışmasını sağlar

hata yönetimi = can dostumuz

yapay zeka da nerelerde kullanılır?
    - veri hazırlama
    - dosya okuma
    - model eğitim döngüsü
    - rag sistemleri
"""

# yazım hatası (syntax error)
if 5 > 3: # SyntaxError: expected ':'
    print("ok") # NameError: name 'ok' is not defined

# name error (tanımsız değişken)
# print(x) # NameError: name 'x' is not defined

# type error (tip uyusmazlığı)
# print("10" + 5) # TypeError: can only concatenate str (not "int") to str

# value error (değer uygun değil)
# int("kaan") # ValueError: invalid literal for int() with base 10: 'kaan'

# zero division error (sifra bölme hatası)
# print(10/0) # ZeroDivisionError: division by zero

# indeks hatası 
liste = [1, 2, 3, 4]
# print(liste[10]) # IndexError: list index out of range

# key error (sözlükte anahtar hatası)
ogrenci = {"isim": "kaan"}
# print(ogrenci["yas"]) # KeyError: 'yas'

# file not found hatası
# with open("kaan.txt", "r") as f:
#     print(f.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'kaan.txt'

# attribute hatasi (yanlış metot özellik hatası)
sayi = 10
# sayi.append(5)  # AttributeError: 'int' object has no attribute 'append'

# try - except - else - finally

"""
try - except
    - program hata verdiğinde durmasını istemeyiz
    - hata olursa yakalyıp kontrollü şekilde yönetmesi lazım
"""
# try:
#     sayi = int(input("Sayı girin: "))
#     print(10/sayi)
# except:
#     print("bir hata oluştu")

# print("program başarılı bir şekilde çalışmaya devam ediyor.")

# belirli bir hata yakalama yöntemi
try:
    sayi = int(input("Sayı girin: "))
    print(10/sayi)
except ValueError:
    print("Lütfen bir sayı girin")
except ZeroDivisionError:
    print("Sıfıra bölme yapılamaz")

# else: hata yoksa çalışır
try:
    sayi = int(input("Sayı girin: "))
    sonuc = 10/sayi
except (ValueError, ZeroDivisionError):
    print("Hatalı giriş.")
else: # hata yoksa
    print(f"Sonuç: {sonuc}")

# finally: her durumda çalışır
try: 
    dosya = open("veri.txt", "r", encoding="utf-8")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı")
finally:
    try:
        dosya.close()
    except:
        pass

# kendi hatamızı üretmek istersek ne yapalım
yas = int(input("Yaş: "))

if yas < 0:
    raise ValueError("Yaş negatif olamaz.") # ValueError: Yaş negatif olamaz.

# genel hata ayıklama mantığı
try:
    sayi = int(input("bir sayı girin: "))
    print(10/sayi)
except Exception as e:
    print(f"Hata: {str(e)}")