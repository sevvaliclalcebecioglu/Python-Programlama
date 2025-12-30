website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- course karakter dizisindeki kaç karakter olduğunu gösterin.

print(len(course))

# 2- website içinden www karakterlerini alın.

print(website[7:10])

# 3- website içinden com karakterlerini alın.

print(website[-3:])

# 4- course içinden ilk 15 ve son 15 karakterini alın.

print(course[:15])
print(course[-15:])

# 5- course içindeki karakterleri tersten yazdırın.

print(course[::-1])

# 6- course içindeki 'Python' kelimesinin kaç kere geçtiğini gösterin.

print(course.count("Python"))

# 7- course içindeki karakter dizisinin 'Programlama' ile başlayıp başlamadığını gösterin.

print(course.startswith("Programlama"))

# 8- course içindeki karakter dizisinin 'Rehberiniz' ile bitip bitmediğini gösterin.

print(course.endswith("Rehberiniz"))

# 9- course içindeki karakter dizisinde 'a' karakterinin kaçıncı indexde olduğunu gösterin.

print(course.find("a"))

# 10- course içindeki karakter dizisinde 'Python' kelimesinin kaçıncı indexde olduğunu gösterin.

print(course.find("Python"))

# --------------------------------------------------------

name, surname, age, job = "İclal", "Cebecioğlu", 22, "Mühendis"

# 11- Yukarıdaki değişkenleri kullanarak ekrana şu şekilde bir çıktı verin: Benim adım İclal Cebecioğlu, yaşım 22 ve mesleğim Mühendis.

print("Benim adım {} {}, yaşım {} ve mesleğim {}.".format(name, surname, age, job))

# 12- Yukarıdaki değişkenleri kullanarak f-string ile ekrana şu şekilde bir çıktı verin: Benim adım İclal Cebecioğlu, yaşım 22 ve mesleğim Mühendis.

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

# 13- 'Hello World' karakter dizisinin tüm harflerini büyük harf yapın.

print("Hello World".upper())

# 14- 'Hello World' karakter dizisinin tüm harflerini küçük harf yapın.

print("Hello World".lower())

# 15- 'Hello World' karakter dizisinin ilk harfini büyük harf yapın.

print("Hello World".capitalize())

# 16- 'hello world' karakter dizisinin ilk harflerini büyük harf yapın.

print("hello world".title())

# 17- 'Hello World' karakter dizisindeki 'World' ifadesini 'There' olarak değiştirin.

print("Hello World".replace("World", "There"))

# 18- 'Hello World' karakter dizisini boşluk karakterlerinden ayırın.

print("Hello World".split())

# 19- abc ifadesini yan yana 3 kere yazdırın.

print("abc" * 3)

# 20- 'Hello World' karakter dizisindeki boşluk karakterinin indexini bulun.

print("Hello World".find(" "))