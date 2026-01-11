import pandas as pd

data = {
    "isim": ["Ali", "Veli", "Ayşe", "Ali", "Ayşe", "Veli", "Ali"],
    "departman": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance"],
    "yas": [30, 28, 35, 32, 29, 40, 45],
    "maas": [30000, 25000, 35000, 40000, 27000, 45000, 50000]
}

df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df[df["departman"] == "IT"])
print(df[df["maas"] > 35000])
print(df.sort_values(by="maas", ascending=False))

print(df.groupby("departman")["maas"].mean())
print(df.groupby("departman")["yas"].mean())


print(
    df.groupby("departman")
      .agg(
          ortalama_maas=("maas", "mean"),
          max_maas=("maas", "max"),
          calisan_sayisi=("isim", "count")
      )
)
df["kidem"] = df["yas"].apply(lambda x: "Kıdemli" if x >= 35 else "Genç")
print(df)

# Bu çalışma ile Pandas'ta temel EDA,
# filtreleme, sıralama ve groupby operasyonları
# pratik edilmiştir.

