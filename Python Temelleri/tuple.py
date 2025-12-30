list = [1, 2, 3] # Değiştirilebilir (mutable)

tuple = (1, 'iki', 3) # Değiştirilemez (immutable)

print(type(list))  # <class 'list'> 
print(type(tuple)) # <class 'tuple'>

print(list[0])   # 1
print(tuple[1])  # 'iki'

# Liste elemanlarını değiştirme

list[0] = 10
print(list)  # [10, 2, 3]

# Tuple elemanlarını değiştirme (hata verir)
# tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Tuple'lar genellikle sabit veri koleksiyonları için kullanılır
print(tuple)  # (1, 'iki', 3)   

# Tuple'ları unpacking yaparak değişkenlere atama
a, b, c = tuple
print(a)  # 1
print(b)  # 'iki'
print(c)  # 3

# Tuple'ların uzunluğunu bulma
print(len(tuple))  # 3

# Tuple'ların elemanlarına erişim
for item in tuple:
    print(item) 

# Tuple'ların iç içe kullanımı
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])      # (2, 3)    
print(nested_tuple[1][0])   # 2 

# Tuple'ların birleştirilmesi
tuple2 = (4, 5, 6)
combined_tuple = tuple + tuple2
print(combined_tuple)  # (1, 'iki', 3, 4, 5, 6)

print(tuple.count(1))  # 1
print(tuple.index('iki'))  # 1
