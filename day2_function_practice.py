# FONKSİYON ALIŞTIRMASI 1 : 50'den büyük sayıları bulan ve bu sayıların toplamını ve adedini döndüren bir fonksiyon. 
import random
yeni_list = []

for i in range(15):
    yeni_list.append(random.randint(1, 100))
print("Yeni Liste:", yeni_list)

def elliden_buyukler(sayilar):
    toplam = 0
    sayac = 0
    for sayi in sayilar :
        if sayi > 50:
            toplam += sayi
            sayac += 1
    return toplam, sayac


get_toplam, get_sayac = elliden_buyukler(yeni_list)
print("50'den büyük sayıların toplamı:", get_toplam)
print("50'den büyük sayıların adedi:", get_sayac)

################################################################################
# FONKSİYON ALIŞTIRMASI 2 : Koşullu Ortalama + Filtreleme
""""
Parametre olarak:
liste 
alt sınır
üst sınır

Bu aralıkta kalan sayıların:
adedini
toplamını
ortalamasını
tek bir fonksiyonla döndür. 
""" 
import random

def aralik_analizi(liste, alt_sinir, ust_sinir):
    sayac = 0
    toplam = 0

    for sayi in liste:
        if alt_sinir <= sayi <= ust_sinir:
            sayac += 1
            toplam += sayi

    if sayac > 0:
        ortalama = toplam / sayac
    else:
        ortalama = 0

    return sayac, toplam, ortalama


# Rastgele liste oluşturma
liste = []
for i in range(10):
    liste.append(random.randint(1, 100))

print("Liste:", liste)

# Fonksiyonu çağır
adet, toplam, ortalama = aralik_analizi(liste, 30, 70)

print("30-70 arası sayı adedi:", adet)
print("30-70 arası sayı toplamı:", toplam)
print("30-70 arası sayı ortalaması:", ortalama)


#########################################################################
# FONKSİYON ALIŞTIRMA 3 : 
"""
Bir sayı listesi veriliyor.
Listenin ortalamasını hesapla
Ortalamaya en yakın sayıyı

Eğer birden fazla varsa hepsini bir fonksiyonla döndür.

"""


def ortalamaya_en_yakin(liste):
    ortalama = sum(liste) / len(liste)

    min_fark = min(abs(sayi - ortalama) for sayi in liste)

    en_yakinlar = []
    for sayi in liste:
        if abs(sayi - ortalama) == min_fark:
            en_yakinlar.append(sayi)

    return ortalama, en_yakinlar

liste = [10, 20, 30, 40, 50]

ortalama, yakinlar = ortalamaya_en_yakin(liste)

print("Liste:", liste)
print("Ortalama:", ortalama)
print("Ortalamaya en yakın değer(ler):", yakinlar)

########################################################
#FONKSİYON ALIŞTIRMASI 4 : 

"""
İç içe listelerden oluşan bir yapı var:
Bir fonksiyon yaz:
Tüm elemanları tek liste haline getir
Genel ortalamayı hesapla
Ortalamanın:
altında kalanlar
üstünde kalanlar
ayrı ayrı döndür.

"""

def coklu_liste_analizi(listeler):
    tum_sayilar = []

    for alt_liste in listeler:
        for sayi in alt_liste:
            tum_sayilar.append(sayi)

    ortalama = sum(tum_sayilar) / len(tum_sayilar)

    altinda = []
    ustunde = []

    for sayi in tum_sayilar:
        if sayi < ortalama:
            altinda.append(sayi)
        elif sayi > ortalama:
            ustunde.append(sayi)

    return ortalama, altinda, ustunde


# Örnek kullanım
listeler = [
    [10, 20, 30],
    [5, 50, 75],
    [60, 70, 80]
]

ortalama, alt, ust = coklu_liste_analizi(listeler)

print("Genel Ortalama:", ortalama)
print("Ortalamanın Altında:", alt)
print("Ortalamanın Üstünde:", ust)
