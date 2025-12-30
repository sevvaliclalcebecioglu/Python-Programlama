## Variables

maasAli = 5000
maasVeli = 4000
vergiOrani = 0.27

print(maasAli - (maasAli * vergiOrani))
print(maasVeli - (maasVeli * vergiOrani))

# Değiken Tanımlama Kuralları;

# 1. Değişken isimleri harf (a-z, A-Z) veya alt çizgi (_) ile başlamalıdır.
# 2. Değişken isimleri rakam (0-9) ile başlayamaz.
# 3. Değişken isimlerinde boşluk kullanılamaz, alt çizgi (_) kullanılabilir.
# 4. Değişken isimleri büyük/küçük harf duyarlıdır (maasAli ve MaasAli farklı değişkenlerdir).
# 5. Değişken isimleri Python'un rezervli kelimeleri (if, for, while, vs.) olamaz.
# 6. Değişken isimleri anlamlı ve açıklayıcı olmalıdır.
# 7. Değişken isimlerinde Türkçe karakter (ç, ğ, ü, ş, ö, ı) kullanmaktan kaçınılmalıdır.
# 8. Değişken isimleri kısa ve öz olmalıdır, ancak çok kısa olmamalıdır (örneğin, "x" yerine "maasAli" gibi).
# 9. Değişken isimlerinde özel karakterler (!, @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /) kullanılmamalıdır.
# 10. Değişken isimleri anlamlı kelimelerden oluşabilir ve kelimeler alt çizgi (_) ile ayrılabilir (örneğin, "maas_Ali" gibi).
# 11. Değişken isimleri tek bir kelime olabilir (örneğin, "maas" gibi).
# 12. Değişken isimleri uzunluk sınırı yoktur, ancak okunabilirlik için makul uzunlukta tutulmalıdır.
# 13. Değişken isimleri sayılarla başlayamaz, ancak sayılar değişken isminin içinde veya sonunda kullanılabilir (örneğin, "maas2024" gibi).


x = 10 # integer
y = 3.14 # float
name = "Ali" # string
is_student = True # boolean

x, y, name, is_student = 10, 3.14, "Ali", True

a = '10'
b = '20'
print(a + b)  # Çıktı: '1020' (string birleştirme)