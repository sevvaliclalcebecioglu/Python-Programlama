x, y, z, = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir?

a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
carpim = a * b
fark = carpim - (x + y + z)
print("Çarpım ile x, y, z toplamının farkı:", fark)

# 2- y' nin x'e kalansız bölümünü hesaplayınız.

kalansiz_bolum = y // x
print("y'nin x'e kalansız bölümü:", kalansiz_bolum)

# 3- (x,y,z) toplamının mod 3'ü nedir?

toplam_mod3 = (x + y + z) % 3
print("(x, y, z) toplamının mod 3'ü:", toplam_mod3)

# 4- y'nin x'inci kuvveti nedir?

y_x_kuvveti = y ** x
print("y'nin x'inci kuvveti:", y_x_kuvveti)

# 5- x, *y, z = numbers işlemine göre z'nin küpü nedir?

x, *y, z = numbers
z_kupu = z ** 3
print("z'nin küpü:", z_kupu)

# 6- x, *y, z = numbers işlemine göre y'nin toplamı nedir?

x, *y, z = numbers
y_toplami = sum(y)
print("y'nin toplamı:", y_toplami)

