"""
Kullanıcıdan vize notu ve final notu alalım
- Ortalama hesaplaması
- harf notu belirleme
- sonucu ekrana yazdırma
"""

# not hesaplama sistemi
def ortalama_hesapla(vize: float, final: float) -> float:
    """
    Vize %40, Final  %60 olacak şekilde ortalama hesaplar.
    """
    ortalama = vize * 0.4 + final * 0.6
    return ortalama

def harf_notu_belirle(ortalama: float) -> str:
    """
    Ortalama değerine göre harf notu döndürür
    """
    if ortalama >= 85:
        return "A"
    elif ortalama >= 70:
        return "B"
    elif ortalama >= 50:
        return "C"
    else:
        return "F"

def sonucu_yazdir(isim: str, ortalama: float, harf: str):
    """
    sonucu ekrana yazdirir
    """
    print("-------SONUÇ-------")
    print(f"Öğrenci: {isim}")
    print(f"Ortalama: {ortalama}")
    print(f"Harf Notu: {harf}")


# program akışı
isim = input("öğrenci adı: ")
vize = float(input("Vize notu: "))
final = float(input("Final notu: "))

ortalama = ortalama_hesapla(vize = vize, final = final)
harf = harf_notu_belirle(ortalama = ortalama)

sonucu_yazdir(isim = isim, ortalama = ortalama, harf = harf)