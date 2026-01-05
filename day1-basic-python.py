"""
1. Gün - Python Temelleri Tekrarı

Bu betik temel Python alıştırmalarını içerir:
- Listeler ve döngüler
- Koşullu mantık
- Yinelenenleri kaldırma
- Basit istatistikler


Belki çok temel olabilir ama temelleri sağlamlaştırmak iyidir! Minik gözüken ama benim için büyük bir adım...
"""


# Gerekli kütüphaneleri içe aktar

import random
import numpy as np
list_ = []
for number in range(10):
    list_.append(random.randint(1, 100))
print("Random List:", list_)

####### Alıştırma 1 : Sadece 50’den büyük olan sayıların ortalamasını hesaplayan bir kod yaz. #######
## Bunun için bir liste oluşturdum. ## 

sum_greater_50 = 0
count_greater_50 = 0
average_greater_50 = 0

for number in list_:
    if number > 50:
        sum_greater_50 += number
        count_greater_50 += 1

if count_greater_50 > 0:
    average_greater_50 = sum_greater_50 / count_greater_50
else:
    average_greater_50 = 0

print("50'den büyük sayıların ortalaması:", average_greater_50)

## Alıştırma 1.1 : Ortalamanın altında kalan değerleri yeni bir listeye alma ##
liste = [10, 20, 30, 40, 50]

ortalama = sum(liste) / len(liste)

ortalama_alti = []

for sayi in liste:
    if sayi < ortalama:
        ortalama_alti.append(sayi)

print("Liste:", liste)
print("Ortalama:", ortalama)
print("Ortalama altı değerler:", ortalama_alti)
        
####### Alıştırma 2 : Listedeki her sayının tek mi çift mi olduğunu belirleyen bir kod yaz. #######
for number in list_:
    if number % 2 == 0:
        print(f"{number} çift sayıdır.")
    else:
        print(f"{number} tek sayıdır.")

### Alıştırma 3 : Bir liste içinde tekrar eden elemanları bul ve tekrarları temizleyerek yeni bir liste oluştur. ###
## YÖNTEM 1 ('set' ile) : Ben bunu basitten zora doğru yapacağım. Önce basit bir yöntemle yapalım. ##
liste = [ 1, 2, 2, 3, 4, 4, 5, 5, 5 ]

tekrarsiz_liste = list(set(liste))
print("Orijinal Liste (Yöntem 1):", liste)
print("Benzersiz Liste (Yöntem 1):", tekrarsiz_liste)

## YÖNTEM 2 ('for döngüsü' ile) :  ##
# import numpy as np (başta yapıldı, yine de hatırlatayım)
list_1 = []  # tekrar eden elemanları içeren liste
unique_list = []  # sadece benzersiz elemanları tutacak yeni liste
for number in range(30):
    list_1.append(random.randint(1, 10)) # Listedeki eleman sayısını arttırdım ve aralığı azalttım ki tekrar eden elemanlar olsun.
print("Random List:", list_1)

for eleman in list_1:
    if eleman not in unique_list:
        unique_list.append(eleman)

print("Orijinal Liste (Yöntem 2):", list_1)
print("Benzersiz Liste (Yöntem 2):", unique_list)

## YÖNTEM 3 ( 'list compherension' ile ) : ##

liste_1 = [ 1, 2, 2, 3, 4, 4, 5, 5, 5 ]

[tekrarsiz_liste.append(x) for x in liste if x not in tekrarsiz_liste]
print("Orijinal Liste (Yöntem 3):", liste)
print("Benzersiz Liste (Yöntem 3):", tekrarsiz_liste)

## YÖNTEM 4 ( 'numpy' ile ) : ##

# import numpy as np (başta yapıldı, yine de hatırlatayım)
liste_1 = [ 1, 2, 2, 3, 4, 4, 5, 5, 5 ]
tekrarsiz_liste = np.unique(liste)
print("Orijinal Liste (Yöntem 4):", liste)
print("Benzersiz Liste (Yöntem 4):", tekrarsiz_liste)

