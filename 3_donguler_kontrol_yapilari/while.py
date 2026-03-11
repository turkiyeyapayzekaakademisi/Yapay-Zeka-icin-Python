"""
While döngüsü nedir?
    - koşul doğru olduğu sürece çalışan bir döngüdür.
    - if yapısı koşulu sadece 1 KERE kontrol eder, while yapısı ise koşulu her iterasyonda kontrol eder.
    - koşul doğru (True) olduğu sürece döngü devam eder.

while kosul:
    yapilacak_islem
"""

i = 0 
while i < 5: # i küçüktür 5 ten koşulu doğru olduğu sürece print işlemini yaptır.
    print(i)
    i = i + 1

print(f"i: {i}")
"""
                  i       print()
1. iterasyon      1            0
2. iterasyon      2            1
3. iterasyon      3            2
4. iterasyon      4            3
5. iterasyon      5            4  
6. iterasyon ????
"""

# sayaç mantığı
sayac = 1
while sayac <= 3:
    print("merhaba")
    sayac += 1

# while + if kullanımı
i = 0
while i < 10:

    if i % 2 == 0:
        print(f"çift: {i}")
    
    i += 1

# kullanıcı kontrollü while
giris = ""
while giris != "q": 
    giris = input("Çıkmak için q yazın: ")
    print(f"Kullanıcı mesajı: {giris}")

# chatbot örneği
giris = ""
while giris != "q": 

    giris = input("Çıkmak için q yazın: ")
    print(f"Kullanıcı mesajı: {giris}")

    # chatbota soruyu gönder
    # chatbot bize cevaı return eder
    # chatbotun cevabını ekrana yazdırıyoruz
    print("chatbot: merhaba")