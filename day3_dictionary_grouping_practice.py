# Gün 3 hedefi:
# - Dictionary kullanarak veri gruplama
# - Fonksiyon içinde döngü ve koşul kurma
# - Analiz sonucu özet dictionary üretme


def frekans_hesapla(liste):
    frekans = {}

    for eleman in liste:
        if eleman in frekans:
            frekans[eleman] += 1
        else:
            frekans[eleman] = 1

    return frekans


notlar = [70, 85, 90, 45, 60, 90, 85, 70, 70]

not_frekans = frekans_hesapla(notlar)
print("Not Frekansı:", not_frekans)


# Beklenen çıktı:
# {70: 3, 85: 2, 90: 2, 45: 1, 60: 1}

##############################################################################
# Harf frekans analizi
kelime = "verianalizi"

harf_frekans = frekans_hesapla(kelime)
print("Harf Frekansı:", harf_frekans)


#############################################################################
# Notları sınıflandırma ve frekans analizi
def not_siniflandir(notlar):
    siniflar = []

    for not_ in notlar:
        if 0 <= not_ <= 49:
            siniflar.append("Kaldı")
        elif 50 <= not_ <= 69:
            siniflar.append("Geçer")
        elif 70 <= not_ <= 89:
            siniflar.append("İyi")
        else:
            siniflar.append("Pekiyi")

    return siniflar
notlar_2 = [20, 35, 40, 55, 65, 70, 85, 90]

sinif_listesi = not_siniflandir(notlar_2)
sinif_frekans = frekans_hesapla(sinif_listesi)

print("Not Sınıf Frekansı:", sinif_frekans)


#############################################################################
# Kelime uzunluklarına göre frekans analizi
kelimeler = ["veri", "analiz", "python", "sql", "ai"]
kelime_uzunluk_frekans = {}

for i in kelimeler:
    uzunluk = len(i)
    if uzunluk in kelime_uzunluk_frekans:
        kelime_uzunluk_frekans[uzunluk] += 1
    else:
        kelime_uzunluk_frekans[uzunluk] = 1
print(kelime_uzunluk_frekans)

##########################################################################
# Koşullu frekans analizi

def kelime_uzunluklari(kelimeler):
    uzunluklar = []
    return uzunluklar

kelimeler = ["veri", "analiz", "python", "sql", "ai"]

uzunluk_listesi = kelime_uzunluklari(kelimeler)
uzunluk_frekans = frekans_hesapla(uzunluk_listesi)

print("Kelime Uzunluk Frekansı:", uzunluk_frekans)

######################################################################
def elliden_buyukleri_filtrele(liste):
    sonuc = []

    for sayi in liste:
        if sayi > 50:
            sonuc.append(sayi)

    return sonuc
sayilar = [10, 25, 30, 45, 60, 75, 80, 90, 90]

filtrelenmis = elliden_buyukleri_filtrele(sayilar)
kosullu_frekans = frekans_hesapla(filtrelenmis)

print("50'den Büyük Sayı Frekansı:", kosullu_frekans)

def coklu_liste_duzlestir(listeler):
    tum_elemanlar = []

    for alt_liste in listeler:
        for eleman in alt_liste:
            tum_elemanlar.append(eleman)

    return tum_elemanlar
veriler = [
    [1, 2, 2, 3],
    [3, 4, 4, 4],
    [5, 1, 2]
]

duz_liste = coklu_liste_duzlestir(veriler)
toplam_frekans = frekans_hesapla(duz_liste)

print("Toplam Frekans:", toplam_frekans)

