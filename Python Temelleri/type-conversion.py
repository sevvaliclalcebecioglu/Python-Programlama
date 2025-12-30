x = input('1.sayı: ')
y = input('2.sayı: ')

toplam = x + y
print('Toplam: ', toplam)

# Yukarıdaki kodda kullanıcıdan alınan iki sayının toplamı yerine string birleştirme işlemi yapılır. Bunu düzeltmek için tip dönüşümü yapmalıyız.

print('Doğru Toplam: ', int(x) + int(y))  
# int() fonksiyonu ile string ifadeleri tamsayıya dönüştürdük.

# ----------------------------------------------------------

x = 5 # tamsayı
y = 2.5 # ondalıklı sayı
name = 'Ali' # string
isOnline = True # boolean

print(type(x))        # <class 'int'>
print(type(y))        # <class 'float'>
print(type(name))     # <class 'str'>
print(type(isOnline)) # <class 'bool'>

# Type conversion (Tip Dönüşümü)

x = float(x)  # tamsayıyı ondalıklı sayıya dönüştürme
print(x)      # 5.0
print(type(x)) # <class 'float'>

y = int(y)    # ondalıklı sayıyı tamsayıya dönüştürme
print(y)      # 2
print(type(y)) # <class 'int'>

isOnline = str(isOnline)  # boolean'ı string'e dönüştürme
print(isOnline)           # 'True'
print(type(isOnline))     # <class 'str'>

name = int('123')  # string'i tamsayıya dönüştürme
print(name)        # 123
print(type(name))  # <class 'int'>