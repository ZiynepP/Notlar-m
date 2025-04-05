
# NumPy ve Pandas Kapsamlı Özet
# Ödev1 için hazırlanmıştır.

# NumPy - Sayısal Hesaplamalar için

import numpy as np

# 1. NumPy Array (Dizi) Oluşturma
array1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", array1)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array2)

# 2. Özel Diziler
zeros_array = np.zeros((2, 3))
print("Zeros Array:\n", zeros_array)

ones_array = np.ones((3, 2))
print("Ones Array:\n", ones_array)

identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# 3. Rastgele Sayılar
random_array = np.random.rand(2, 2)
print("Random Array:\n", random_array)

# 4. Array Özellikleri
print("Shape:", array2.shape)
print("Data Type:", array2.dtype)

# 5. Temel İşlemler
array3 = np.array([10, 20, 30, 40, 50])
print("Toplam:", np.sum(array3))
print("Ortalama:", np.mean(array3))
print("Maksimum:", np.max(array3))
print("Minimum:", np.min(array3))

# 6. Array Indexleme ve Dilimleme
print("İlk Eleman:", array1[0])
print("İlk Üç Eleman:", array1[:3])
print("Son İki Eleman:", array1[-2:])

# 7. Matematiksel İşlemler
print("Array + 5:", array1 + 5)
print("Array * 2:", array1 * 2)
print("Array karekök:", np.sqrt(array1))

# --------------------------------------------------------------------------------------

# Pandas - Veri Analizi için

import pandas as pd

# 8. Seri (Series) Oluşturma
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Pandas Series:\n", s)

# 9. DataFrame Oluşturma
data = {
    "İsim": ["Ali", "Ayşe", "Mehmet"],
    "Yaş": [25, 30, 22],
    "Şehir": ["İstanbul", "Ankara", "İzmir"]
}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)

# 10. DataFrame Özellikleri
print("Kolon İsimleri:", df.columns)
print("İlk Satırlar:\n", df.head())

# 11. Satır ve Sütunlara Erişim
print("İsim Kolonu:\n", df["İsim"])
print("İlk Satır:\n", df.iloc[0])

# 12. Filtreleme
print("Yaşı 25'ten büyük olanlar:\n", df[df["Yaş"] > 25])

# 13. Yeni Kolon Ekleme
df["Maaş"] = [5000, 6000, 5500]
print("Maaş Eklenmiş DataFrame:\n", df)

# 14. Eksik Veri
df2 = pd.DataFrame({
    "A": [1, 2, None],
    "B": [4, None, 6]
})
print("Eksik Verili DataFrame:\n", df2)

print("Eksik veriler temizlenmiş:\n", df2.dropna())
print("Eksik veriler doldurulmuş:\n", df2.fillna(0))

# 15. Gruplama
df_group = df.groupby("Şehir").mean()
print("Şehirlere göre Ortalama Yaş ve Maaş:\n", df_group)
