website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'Hello World' ifadesini ekrana yazdırın

print("Hello World")

# 2- 'Hello World' ifadesini büyük harflerle yazdırın

print("Hello World".upper())

# 3- 'Hello World' ifadesini küçük harflerle yazdırın

print("Hello World".lower())

# 4- 'Hello World' ifadesinin ilk karakterini alın

print("Hello World"[0])

# 5- 'Hello World' ifadesinin karakter sayısını öğrenin

print(len("Hello World"))

# 6- 'Hello World' ifadesini tersten yazdırın

print("Hello World"[::-1])

# 7- 'Hello World' ifadesindeki 'World' ifadesini 'There' ile değiştirin

print("Hello World".replace("World", "There"))

# 8- 'Hello World' ifadesini boşluk karakterlerinden ayırın

print("Hello World".split())

# 9- 'website' değişkenindeki 'http://' ifadesini kaldırın  
    
print(website.replace("http://", ""))

# 10- 'course' değişkenindeki karakter sayısını öğrenin

print(len(course))

# 11- 'course' değişkenindeki ilk 15 karakteri alın

print(course[0:15])

# 12- 'course' değişkeninde 'Python' ifadesinin kaç kez geçtiğini öğrenin

print(course.count("Python"))

# 13- 'course' değişkeninde 'Python' ifadesinin başlangıç index bilgisini öğrenin

print(course.find("Python"))

# 14- 'course' değişkeninde 'Java' ifadesinin olup olmadığını kontrol edin

print("Java" in course)

# 15- 'course' değişkenindeki tüm karakterleri küçük harfe çevirin

print(course.lower())

# 16- 'course' değişkenindeki tüm karakterleri büyük harfe çevirin

print(course.upper())

# 17- 'course' değişkenindeki karakterleri boşluk karakterlerinden ayırın

print(course.split())

# 18- 'website' değişkenindeki 'www.' ifadesini kaldırın

print(website.replace("www.", ""))

# 19- 'website' değişkenindeki alan adını alın (örneğin: sadikturan.com)

print(website.replace("http://www.", ""))

# 20- 'course' değişkenindeki boşluk karakterlerini '-' ile değiştirin

print(course.replace(" ", "-")) 

# 21- 'course' değişkenini boşluk karakterlerine göre listeleyin

print(course.split(" "))

# 22- 'website' değişkenindeki karakter sayısını öğrenin

print(len(website))

# 23- 'website' değişkenindeki 'com' ifadesinin başlangıç index bilgisini öğrenin

print(website.find("com"))

# 24- 'website' değişkeninde 'http' ifadesinin olup olmadığını kontrol edin

print("http" in website)

# 25- 'course' değişkenindeki karakterleri tersten yazdırın

print(course[::-1])

# 26- 'course' değişkenindeki ilk 10 karakteri alın ve büyük harfe çevirin

print(course[0:10].upper())

# 27- 'course' değişkenindeki son 10 karakteri alın ve küçük harfe çevirin

print(course[-10:].lower())

# 28- 'website' değişkenindeki 'www' ifadesinin karakter sayısını öğrenin

print(len("www"))

# 29- 'course' değişkeninde 'Rehberiniz' ifadesinin başlangıç index bilgisini öğrenin

print(course.find("Rehberiniz"))

# 30- 'course' değişkenindeki karakter sayısını boşluk karakterleri hariç öğrenin

print(len(course.replace(" ", "")))

# 31- course içindeki karakterlerin hepsi alfabetik mi? 

print(course.replace(" ", "").isalpha())

# 32- course içindeki karakterlerin hepsi sayısal mı?

print(course.replace(" ", "").isnumeric())
