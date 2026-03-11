"""
Numpy: yüksek performanslı sayısal hesap kütüphanesi
    - büyük veri, hızlı matematik, matris hesaplamaları, bilimsel ve istatistiksel işlem
    - numpy C dili yazılmıştır

Numpy Neden Gerekli?
    - daha hızlı hesaplama
    - çok boyutlu veri yapıları
        - matrisler, N boyutlu dizi ile, veri tabloları
    - matematiksel işlem kolaylığı

Numpy ve Yapay Zeka
    - scikit-learn (ml)
    - tensorflow ve pytorch (dl)
    - pandas (data science)

Numpy bölümünde ne öğrenicez?
    - Diziler
    - matematiksel işlemler
    - indeksleme ve dilimleme
    - dizi birleştirme ve bölme
    - çok boyutlu diziler
    - matris işlemleri
    - rastgele sayı üretimi
"""
import numpy as np

"""
Diziler (array)
    - ndarray: n-dimensional array
"""

# liste ile numpy dizisi arasındaki fark

sayilar = [1, 2, 3, 4, 5] # liste
print(sayilar)

# np.array() -> pyton listesini numpy arrayine dönüştürür
dizi = np.array(sayilar) # numpy dizisi
print(dizi)

# numpy dizisi tipini inceleme
print(type(dizi)) # <class 'numpy.ndarray'>

# numpy dizisi boyutu öğrenme
print(dizi.shape) # (5,) -> 5 elemanlı tek boyutlu bir dizi

# numpy dizisinin veri tipi
print(dizi.dtype) # int64 -> integer

# numpy ile dizi oluşturmanın farklı yollarına
dizi = np.zeros(5) # [0. 0. 0. 0. 0.]  
print(dizi)

dizi = np.ones(5) # [1. 1. 1. 1. 1.]
print(dizi)

# belirli bir aralıkta sayı dizisi oluşturma
dizi = np.arange(0, 10)
print(dizi) # [0 1 2 3 4 5 6 7 8 9] 0'dan başlar 10'a kadar sayıları üretir

# belirli aralıklarla sayı üretme 
dizi = np.arange(0, 10, 2)
print(dizi) # [0 2 4 6 8]

# belirli bir aralığa eşit bölünmüş diziler
dizi = np.linspace(0, 10, 5) # 0 ile 10 arasında 5 sayı üret
print(dizi) # [ 0.   2.5  5.   7.5 10. ]

"""
matematiksel işlemler
"""

# toplama: z = a0 + a1w1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sonuc = a + b
print(sonuc) # [5 7 9]

# çıkarma
sonuc = a - b
print(sonuc) # [-3 -3 -3]

# çarğma
sonuc = a * b
print(sonuc) # [ 4 10 18]

# bölme
sonuc = a / b
print(sonuc) # [0.25 0.4  0.5 ]

# dizi ile sayı arasında işlem yapma
a = np.array([1, 2, 3])
sonuc = a * 2 
print(sonuc) # [2 4 6]

# dizinin karesini almak
a = np.array([1, 2, 3, 4])
sonuc = a ** 2
print(sonuc) # [ 1  4  9 16]

# karekökünü alma mse -> rmse
a = np.array([1, 4, 9, 16])
sonuc = np.sqrt(a)
print(sonuc) # [1. 2. 3. 4.]

# dizinin toplamını bulma
a = np.array([1, 2, 3, 4])
print(np.sum(a)) # 10

# ortalama
print(np.mean(a)) # 2.5

# min ve max değerler
print(np.max(a)) # 4
print(np.min(a)) # 1

# standart sapma
print(np.std(a)) # 1.1

"""
indeksleme (indexing) - dilimleme (slicing)
"""
# dizilerde indeksleme
dizi = np.array([10, 20, 30, 40, 50])
print(dizi[0]) # dizinin ilk elemanına 0 indeksi ile erişmiş olurum
print(dizi[1])

# negatif indeksleme
print(dizi[-1]) # 50

# slicing (dilimleme)
# genel kullanım: dizi[başlangıç:bitiş]
print(dizi[1:4]) # 20, 30, 40 # 1. indeksten başlar 4. indekse kadar gider fakat 4 dahil değildir.

# baştan dilimleme
print(dizi[:3]) # 10, 20, 30

# sondan dilimleme
print(dizi[2:]) # 30, 40, 50

# adım (stem) kullanımı
print(dizi[::2]) # diziden ikişer adım ile eleman seçmek [10 30 50]

# 2 boyutlu dizilerde indeksleme
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

print(matris[0, 0]) # 1 

# belirli bir satırı seçmek
print(matris[1, :]) # [4 5 6]

# belirli bir sutunu seçmek
print(matris[:, 2]) # [3 6 9]

# matris dilimleme
print(matris[0:2, 0:2])

"""
Dizi birleştirme ve bölme
"""

# dizi birleştirme
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = np.concatenate((a, b))
print(sonuc) # [1 2 3 4 5 6]

# iki boyutlu dizi birleştirme
a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [
        [5, 6], 
        [7, 8]
    ]
)

sonuc = np.concatenate((a, b))
print(sonuc)
"""
varsayılan olarak satır yönünde birleştirdik
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

# axis parametresi
# axis = 0 -> satır yönünde birleştirme
# axis = 1 -> sütun yönünde birleştirme

sonuc = np.concatenate((a, b), axis = 1)
print(sonuc)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""

# vstack (dikey birleştirme): axis = 0 gibi yapar
sonuc = np.vstack((a, b))
print(sonuc)

# hstack (yatay birleştirme): axis = 1 gibi yapar
sonuc = np.hstack((a, b))
print(sonuc)

# diziyi parçalara bölme
dizi = np.array([1,2,3,4,5,6])

sonuc = np.split(dizi, 2) # 2 parçaya böl
print(sonuc) # [array([1, 2, 3]), array([4, 5, 6])]

sonuc = np.split(dizi, 3)
print(sonuc) # [array([1, 2]), array([3, 4]), array([5, 6])]

# 2 boyutlu dizilerde bölme
matris = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
)

sonuc = np.split(matris, 2) # satır bazında 2 ye bölme
print(sonuc)
"""
[array([[1, 2],
       [3, 4]]), 
       
array([[5, 6],
       [7, 8]])]
"""

sonuc = np.split(matris, 2, axis = 1) # sütun bazında ikiye bölme
print(sonuc)
"""
[array([[1],
       [3],
       [5],
       [7]]), 
array([[2],
       [4],
       [6],
       [8]])]
"""

"""
Çok boyutlu diziler
"""
# 2 boyutlu dizi oluşturma
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

# dizinin boyutunu öğrenme
print(matris.shape) # (3, 3)

# dizinin kaç boyutlu olduğunu öğrenmek
print(matris.ndim) # 2

# dizideki eleman sayısı
print(matris.size) # 9

# 3 boyutlu dizi oluşturma
"""
görsel -> (height, width) -> (yükseklik ve genişlik) -> (1920, 1080), (1920, 1080), (1920, 1080), ... (1920, 1080) -> (N, 1920, 1080)
"""
dizi3 = np.array(
    [
        [
            [1,2],
            [3,4]
        ],
        [   
            [5,6],
            [7,8]
        ]
    ]
)
print(dizi3)

"""
(2 adet matris, her matriste 2 satır, her matriste 2 satır)
"""
print(dizi3.shape) # (2, 2, 2)

# numpy ile çok boyutlu dizi oluşturma (reshape)
dizi = np.arange(12)
print(dizi) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# matrise dönüştürma
matris = dizi.reshape(3, 4)
print(matris)
"""
3 satır, 4 sütun
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

# matris = dizi.reshape(3, 5) # ValueError: cannot reshape array of size 12 into shape (3,5)


"""
Matris işlemleri
"""

# matris oluşturma
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a)
print(b)

print(a + b) # toplama
print(a - b) # çıkarma
print(a * b) # çarpma

# gerçek matris çarpımı
sonuc = np.dot(a, b)
print(sonuc)
"""
[1, 2],
[3, 4]
*
[5, 6],
[7, 8]
=
[[19 22]
 [43 50]]
"""

# matris transpose (matrisin ters çevrilmesi)
print(a.T)

"""
[1, 2],
[3, 4]

[[1 3]
 [2 4]]
"""

# matris determinantı
det = np.linalg.det(a)
print(det) # -2.0000000000000004

# matrisin tersi
ters = np.linalg.inv(a)
print(ters)
"""
[[-2.   1. ]
 [ 1.5 -0.5]]
"""

"""
Rastgele sayı üretme
"""

# rastgele ondalık sayılar üretme [0-1] arasında
rastgele = np.random.rand(5)
print(rastgele) # [0.01305906 0.49617281 0.8339516  0.34911464 0.63700101]

# rastgele matris oluşturma
rastgele = np.random.rand(3, 3)
print(rastgele)
"""
[[0.2350457  0.99922835 0.25611634]
 [0.27177059 0.13965271 0.72517363]
 [0.56062539 0.14892058 0.04243103]]
"""

# rastgele tam sayı üretme
rastgele = np.random.randint(1, 10, 5) # 1 ile 10 arasında 5 adet rastgele tam sayı üret
print(rastgele) # [1 1 4 8 6]

# rastgele tam sayı matrisi üretme
rastgele = np.random.randint(1, 20, (3, 4)) # 1 ile 20 arasında 3 satır 4 sütun dan oluşan 12 tane tam sayı üret
print(rastgele)
"""
[[13 12  8  2]
 [ 1  2 13 12]
 [12 18  4  3]]"""

# aynı rastgele sonucu üretmek için (seed)

np.random.seed(42)
rastgele = np.random.rand(5)
print(rastgele) # [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]

# bir diziden rastgele eleman seçmek
dizi = np.array([10, 20, 30, 40, 50])
secim = np.random.choice(dizi)
print(secim)

# birden fazla eleman seçme 
secim = np.random.choice(dizi, 3)
print(secim)