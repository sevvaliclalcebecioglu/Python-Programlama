# 1- "Bmw", "Audi", "Toyota", "Mercedes" elemanlarına sahip bir liste oluşturunuz.

cars = ["Bmw", "Audi", "Toyota", "Mercedes"]

# 2- Liste kaç elemanlıdır?

print(len(cars))

# 3- Listenin ilk ve son elemanı nedir?

print(cars[0])
print(cars[-1])

# 4- "Toyota" değerini "Renault" olarak güncelleyiniz.

cars[2] = "Renault" 
print(cars)

# 5- "Mercedes" listenin bir elemanı mıdır?
print("Mercedes" in cars)

# 6- Listenin -2 indeksindeki değer nedir?
print(cars[-2])

# 7- Listenin ilk 3 elemanını alın.
print(cars[0:3])

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Honda" değerlerini ekleyiniz.
cars[-2:] = ["Toyota", "Honda"]
print(cars)

# 9- Listenin üzerine "Audi" ve "Bmw" değerlerini ekleyiniz.
cars += ["Audi", "Bmw"]
print(cars)

# 10- Listenin son elemanını siliniz.
cars.pop()
print(cars)

# 11- Liste elemanlarını tersten yazdırınız.
print(cars[::-1])

# 12- Liste elemanlarını alfabetik olarak sıralayınız.
cars.sort()
print(cars)

# 13- Liste elemanlarını alfabetik olarak ters sıralayınız.
cars.sort(reverse=True)
print(cars)

# 14- Liste elemanlarını siliniz.
cars.clear()
print(cars)

# 15- Aşağıdaki verileri bir liste içerisinde saklayınız.
#     Ogrenci1: Yiğit Bilgi 2010 (70,60,70)
#     Ogrenci2: Sena Tura 1999 (80,80,70)
#     Ogrenci3: Ahmet Turan 1998 (60,60,70)     

students = [
    ["Yiğit Bilgi", 2010, [70, 60, 70]],
    ["Sena Tura", 1999, [80, 80, 70]],
    ["Ahmet Turan", 1998, [60, 60, 70]]
]       

print(students)

# 16- Öğrencilerin yaşlarını listeleyiniz.
ages = [2024 - student[1] for student in students]
print(ages) 

# 17- Öğrencilerin not ortalamalarını listeleyiniz.
averages = [sum(student[2]) / len(student[2]) for student in students]
print(averages) 

# 18- Öğrenci isimlerini büyük harf yapınız.
upper_names = [student[0].upper() for student in students]
print(upper_names)  

# 19- "Yiğit Bilgi" öğrencisinin not ortalamasını bulunuz.  
yigit_average = sum(students[0][2]) / len(students[0][2])
print(yigit_average)

# 20- "Sena Tura" öğrencisinin yaşını bulunuz.
sena_age = 2024 - students[1][1]    