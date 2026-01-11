# Day 4 goal:
# Compare pure Python data analysis logic with Pandas operations

import random
import pandas as pd

# Rastgele notlar oluşturma
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 60))

print("Notlar:", numbers)

# Series oluşturma
s = pd.Series(numbers)
print("\nSeries:")
print(s)

# Frekans analizi
print("\nNot Frekansı:")
print(s.value_counts())

# Python fonksiyonu ile Pandas apply
def not_sinifi(not_):
    if not_ < 50:
        return "Kaldı"
    elif not_ < 70:
        return "Geçer"
    elif not_ < 90:
        return "İyi"
    else:
        return "Pekiyi"

siniflar = s.apply(not_sinifi)
print("\nSınıf Frekansı:")
print(siniflar.value_counts())

# DataFrame + groupby
df = pd.DataFrame({"notlar": numbers})
df["sinif"] = df["notlar"].apply(not_sinifi)

print("\nGroupBy Sonucu:")
print(df.groupby("sinif").size())

# Metin verisi analizi
kelime = "verianalizi"
harfler = pd.Series(list(kelime))
print("\nHarf Frekansı:")
print(harfler.value_counts())

# Pandas, Python'da manuel yazdığım döngü ve dictionary işlemlerini
# arka planda daha optimize şekilde yapmaktadır.
# 1. Rastgele notlar üretildi
# 2. Series oluşturuldu
# 3. Frekans analizi yapıldı
# 4. Kategorik sınıflandırma uygulandı

