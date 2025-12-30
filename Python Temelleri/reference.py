# value types 

x = 5
y = 25

x = y

y = 10

print(x,y)  # Çıktı: 25 10   

# reference types

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0] = "grape"

print(a,b)  # Çıktı: ['grape', 'banana'] ['grape', 'banana']

# Not: Python'da listeler mutable (değiştirilebilir) veri tipleridir ve referans tipi olarak davranırlar.