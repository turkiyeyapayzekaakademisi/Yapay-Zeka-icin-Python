"""
Break Nedir?
    - döngüyü tamamen durdurmak için kullanılır.
    - koşul sağlandığında döngüden çıkar ve bir daha devam etmez
"""

for i in range(10):
    
    # eğer i değeri 5 e eşitse döngüden çıksın, yani döngü devam etmesin
    if i == 5:
        break
    print(i)

"""
Continue Nedir?
    - o anki turun atlanması ama döngünün devam etmesi 
"""

for i in range(10):
    if i == 5:
        continue
    print(i)

"""
Pass 
    - henüz kod yazmadığımız yerde boş bırakmak için kullanılır
    - program hata vermez ama hiçbir işlem yapılmaz
"""

if True:
    # burayı sonra doldur
    pass

for i in range(3):
    if i == 1:
        pass
        # todo: eğer 1 ise buraya bir şeyler yap
    print(i)

"""
nested yapılar:
    - yapıların birbirinin içinde olması
    - if içerisinde if
    - for içerisinde if gibi
    - if içerisinde while gibi
"""

# for içerisinde if 
for i in range(5):
    if i % 2 == 0:
        print(i)

# if içerisinde if
yas = 20
ogrenci = True

# if içerisinde if
if yas < 25:
    if ogrenci:
        print("Öğrenci indirimi")

# for içerisinde for
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")