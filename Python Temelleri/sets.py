fruits = {"apple", "banana", "cherry"}
print(fruits)

# indexleme mümkün değildir
# print(fruits[0])  # Hata verir

# Set'e eleman ekleme
fruits.add("orange")
print(fruits)

# Set'ten eleman çıkarma
fruits.remove("banana")
print(fruits)

# Set'te eleman kontrolü
print("apple" in fruits)  # True

# Set'ler tekrarlanan elemanları içermez
fruits.add("apple")
print(fruits)  # "apple" sadece bir kez görünür

# Set oluşturma
numbers = set([1, 2, 3, 4, 5])
print(numbers)

# Boş set oluşturma
empty_set = set()
print(empty_set)

# Set birleştirme
more_fruits = {"kiwi", "mango"}
all_fruits = fruits.union(more_fruits)
print(all_fruits)

# Set kesişim
common_fruits = fruits.intersection(more_fruits)
print(common_fruits)    

# Set farkı
difference_fruits = fruits.difference(more_fruits)          
print(difference_fruits)
