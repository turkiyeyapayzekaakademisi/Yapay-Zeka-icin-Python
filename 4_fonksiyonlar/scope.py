"""
Scope (local ve global)
    - bir değişkenin nerede erişilebilir olduğunu ifade eder
    - bir değişken nerede tanımlıysa orada geçerlidir.
"""

# local (yerel) değişken: fonksiyon içerisinde tanımlanan değişken

def test():
    x = 10
    print(f"Fonksiyon içi: {x}")

test()

# print(x) # NameError: name 'x' is not defined

# global (genel) değişken: fonksiyon dışında tanımlanan değişken

x = 15

def test():
    print(f"Fonksiyon içi: {x}")

test()

# aynı isimli değişkenler

x = 11
def test():
    x = 5
    print(f"Fonksiyon içi: {x}")

test()
print(f"Fonksiyon dışı: {x}")

# global anahtar kelimesi

x = 9
def test():
    global x
    x = 5 # lokal -> global

test()
print(x)