"""
Matplotlib Nedir?
    - görselleştirme kütüphanesi
    - veriyi anlamak için görselleştiriyoruz

Matplotlib ile neler yapabiliriz?
    - line, sütun, pasta, dağılım 

Matplotlib ve Numpy/Pandas
    - Örnek veri işleme süreci
        - veri okunur (pandas)
        - veri düzenleme (pandas)
        - veri üzerinde işlemler yapılır (Numpy veya pandas)
        - veri grafikler ile gösterilir (matplotlib)

Bu bölüm ne öğreneceğiz?
    - line plot (çizgi): zaman içerisinde değişen verileri görselleştirmek için kullanırız
    - bar chart (sütun): kategorik verileri karşılaştırmak için kullanılır
    - pie chart (pasta): bir bütünün parçalarını görmek için kullanırız
    - scatter plot (dağılım): iki değişken arasında ki ilişkiyi görmek için kullanılır
    - subplots: birden fazla grafiği aynı anda gösterme         
"""

import matplotlib.pyplot as plt 

"""
line plot
"""

# çizgi grafiği oluşturma
gunler = [1, 2, 3, 4, 5]
sicaklik = [22, 24, 23, 25, 27]

# (x = gunler, y = sicaklik)
# color = renk değiştirme
# linestyle = çizgi stilini değiştirme
# marker = noktaları gösterme
plt.plot(gunler, sicaklik, color = "red", linestyle = "--", marker = "o")
plt.title("Günlere Göre Sıcaklık") # grafik başlığı
plt.xlabel("Günler") # x ekseni etiketi
plt.ylabel("Sıcaklık") # y ekseni etiketi
plt.grid(True)
plt.show() # grafiğin ekranda görünmesini sağlar

"""
sütun grafikleri (bar charts)
"""

# sütun grafiği oluştur
isimler = ["ali", "ayse", "mehmet", "zeynep"]
notlar = [70, 85, 60, 90]

# plt.bar = sütun grafiği oluşturmak için
# (x = isimler, y = notlar) 
renkler = ["red", "blue", "green", "orange"]
plt.bar(isimler, notlar, color = renkler)
plt.title("Öğrenci Notları")
plt.xlabel("Öğrenciler")
plt.ylabel("Notlar")
plt.show()

# yatay sütun grafiği
plt.barh(isimler, notlar)
plt.show()

"""
pie chart
"""
etiketler = ["python", "java", "c++", "javascript"]
degerler = [40, 25, 20, 15]

# plt.pie = pasta grafiği
# değerler = pasta dilimlerinin büyüklüğü
# labels = her dilimin etiketi
# %1.1f%% = yüzdeyi 1 basamaklı ondalık ile gösterir
ayrim = [0.1, 0, 0, 0]
renkler = ["red", "blue", "green", "orange"]
plt.pie(degerler, labels = etiketler, explode = ayrim, autopct="%1.1f%%", colors = renkler)
plt.title("Programlama Dili Kullanımı")
plt.show()

"""
dağılım grafiği (scatter plot)
"""

calisma_saatleri = [1, 2, 3, 4, 5, 6]
notlar = [50, 55, 65, 70, 80, 90]

# plt.scatter = dağılım grafiği oluştur
# (x = calisma_saatleri, y = notlar)
# s = nokta boyutunu değiştirme
plt.scatter(calisma_saatleri, notlar, color = "red", s = 100)
plt.title("Çalışma Süresi ve Sınav Notu")
plt.xlabel("Çalışma Saatleri")
plt.ylabel("Notlar")
plt.show()

# birden fazla veri grubu çizdirme

# fen sonuçları
x1 = [1, 2, 3, 4]
y1 = [50, 60, 70, 80]

# mat sonuçları
x2 = [1, 2, 3, 4]
y2 = [55, 65, 75, 85]

plt.scatter(x1, x2, color ="blue", label = "fen")
plt.scatter(x2, y2, color = "red", label = "mat")
plt.legend()
plt.show()

"""
subplots
"""

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2, 1) # plt.subplot(satır, sütun, grafik numarası)
plt.plot(x, y1)
plt.title("Grafik 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Grafik 2")

plt.show()

# farklı grafik türleri kullanarak subplot oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.show()

# 2x2 grafik oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Grafik 1")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Grafik 2")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Grafik 3")

plt.subplot(2, 2, 4)
plt.pie(y)
plt.title("Grafik 4")

plt.show()