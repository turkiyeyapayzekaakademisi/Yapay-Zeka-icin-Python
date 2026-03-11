"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""

class VeriAnalizAraci:

    def __init__(self, veriler):
        self.veriler = veriler # liste

    def verileri_goster(self):
        print(f"Veriler: {self.veriler}")

    def toplam_hesapla(self):
        toplam = sum(self.veriler)
        print(f"Toplam: {toplam}")

    def ortalama_hesapla(self):
        ortalama = sum(self.veriler)/len(self.veriler)
        print(f"Ortalama: {ortalama}")

    def maksimum_bul(self):
        maksimum = max(self.veriler)
        print(f"Maksimum değer: {maksimum}")

    def minimum_bul(self):
        minimum = min(self.veriler)
        print(f"Minimum değer: {minimum}")
    
analiz1 = VeriAnalizAraci([10, 20, 30, 40, 50])

analiz1.verileri_goster()
analiz1.toplam_hesapla()
analiz1.ortalama_hesapla()
analiz1.maksimum_bul()
analiz1.minimum_bul()

"""
Veriler: [10, 20, 30, 40, 50]
Toplam: 150
Ortalama: 30.0
Maksimum değer: 50
Minimum değer: 10
"""