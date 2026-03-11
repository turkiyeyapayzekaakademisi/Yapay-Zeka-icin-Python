import numpy as np


# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

dizi = np.arange(1, 21)
print("Dizi:", dizi)
print("Eleman sayısı:", dizi.size)


# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

dizi = np.array([5, 10, 15, 20, 25])
sonuc = dizi * 3
print("Sonuç:", sonuc)


# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

dizi = np.arange(0, 31)
secim = dizi[10:21]
print("Seçilen elemanlar:", secim)


# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

a = np.array([1,2,3])
b = np.array([4,5,6])

birlesmis = np.concatenate((a,b))
print("Birleşmiş dizi:", birlesmis)


# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

dizi = np.arange(1,13)
matris = dizi.reshape(3,4)

print("Matris:\n", matris)
print("Shape:", matris.shape)


# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

matris = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("İkinci satır:", matris[1])
print("İkinci sütun:", matris[:,1])


# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.

matris = np.random.rand(3,3)

print("Matris:\n", matris)
print("Ortalama:", np.mean(matris))
print("Max:", np.max(matris))


# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

a = np.array([2,4,6,8])
b = np.array([1,3,5,7])

sonuc = a * b
print("Çarpım sonucu:", sonuc)


# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

dizi = np.arange(1,10)
matris = dizi.reshape(3,3)

transpose = matris.T

print("Matris:\n", matris)
print("Transpose:\n", transpose)


# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

sayilar = np.random.randint(1,51,10)

print("Rastgele sayılar:", sayilar)
print("Toplam:", np.sum(sayilar))
print("Ortalama:", np.mean(sayilar))