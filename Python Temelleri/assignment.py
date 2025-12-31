x = 5
y = 10
z = 20 

x, y, z = 5, 10, 20 # "Değişkenleri tek satırda atama"

print(x, y, z)

a, b, c = z, y, x # "Değişkenlerin değerlerini birbirleriyle değiştirme"

print(a, b, c)

x = x + 2  # "x'in değerini 2 artırma"
y = y - 3  # "y'nin değerini 3 azaltma"
z = z * 2  # "z'nin değerini 2 ile çarpma"
print(x, y, z)  #"Yeni değerleri yazdırma"

x += 2  # "x'in değerini 2 artırma"
y -= 3  # "y'nin değerini 3 azaltma"
z *= 2  # "z'nin değerini 2 ile çarpma"
print(x, y, z)  #"Yeni değerleri yazdırma"

x, y, z = 5, 10, 20  # "Değişkenleri başlangıç değerlerine sıfırlama"

x /= 5  # "x'in değerini 5'e bölme"
x %= 3  # "x'in değerini 3 ile mod alma"
print(x)  #"Yeni değeri yazdırma"

values = 1, 2, 3
print(values)  # "values değişkenini yazdırma"
print(type(values))  # "values değişkeninin türünü yazdırma"
print(values[0])  # "values değişkeninin ilk elemanını yazdırma"


