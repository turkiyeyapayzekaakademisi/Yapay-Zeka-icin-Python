"""
Dosya işlemleri: 
    - dosyadan veri okuma
    - okunan verinin işlenmesi
    - dosyaya veri yazma veya keydetme
    - with yapısı

Neden dosya işlemleri yapıyoruz?
    - yapay zeka veriden öğrenir, veriyi python ortamına yüklememiz ve işlememiz lazım bu nedenle dosya işlemlerinin mantığını öğrenicez

Dosya: verinin kalıcı olarak saklandığı yapılar.
    - kullanıcı listeleri
    - not kayıtları
    - log dosyaları
    - csv veri dosyaları
"""
# dosya açma ve okuma
# ornek.txt: dosya
# "r" read okumna modu
dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read() # tüm dosyayı okur
print(icerik)
dosya.close() # dosyayı kapatır

# satır satır okuma
dosya = open("ornek.txt", "r", encoding="utf-8")

for satir in dosya:
    print(satir.strip())

dosya.close()

# dosya içeriğinin işlenmesi
# okuduğumuz veri üzerinde işlem yapıcaz

dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()

print(icerik)
yeni_icerik = icerik.upper()
print(f"yeni_icerik: \n{yeni_icerik}")

# satır sayısını bulma
dosya = open("ornek.txt", "r", encoding="utf-8")
satirlar = dosya.readlines()
dosya.close()

print(f"Toplam satır: {len(satirlar)}")

# dosyaya yazma
dosya = open("yeni_dosya.txt", "w", encoding="utf-8")
dosya.write("Merhaba Dünya\n")
dosya.write("Python öğreniyoruz")
dosya.close()

# oku -> işle -> kaydet
dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()

yeni_icerik = icerik.upper()

dosya = open("islenmis_ornek.txt", "w", encoding="utf-8")
dosya.write(yeni_icerik)
dosya.close()

# with yapısı: dosya otomatik kapanır, hata olsa bile kapanır, daha temiz bir kod yazılmış olur
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("with yapısı:")
    print(icerik)
    # otomatik bir şekilde kendi kendine kapanıyor

# with ile yazma
with open("with_dosya_yazma.txt", "w", encoding="utf-8") as dosya:
    dosya.write("with ile yazma işlemi gerçekleştirildi.")