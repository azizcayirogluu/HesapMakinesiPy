def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Tanımsız"
    return a / b

while True:
    try:
        sayi1 = int(input("1. Sayıyı Giriniz: "))
        sayi2 = int(input("2. Sayıyı Giriniz: "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        continue

    print("Yapılabilecek İşlemler:1-Toplama , 2-Çıkarma , 3-Çarpma , 4-Bölme , 0-Çıkış")
    try:
        secim = int(input("Yapmak İstediğiniz İşlemi Seçiniz: "))
    except ValueError:
        print("Lütfen geçerli bir seçim yapınız!")
        continue

    if secim == 1:
        print(f"Sonuç: {topla(sayi1, sayi2)}")
    elif secim == 2:
        print(f"Sonuç: {cikar(sayi1, sayi2)}")
    elif secim == 3:
        print(f"Sonuç: {carp(sayi1, sayi2)}")
    elif secim == 4:
        print(f"Sonuç: {bol(sayi1, sayi2)}")
    elif secim == 0:
        print("Program sonlandırılıyor...")
        break
    else:
        print("Lütfen geçerli bir değer giriniz (0-4 arasında)")
