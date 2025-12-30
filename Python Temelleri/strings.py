name = 'İclal'
surname = 'Cebecioğlu'
age = 22

greeting = 'My name is ' + name + ' ' + surname + ' and \n I am ' + str(age) + ' years old.'

print(greeting)

# \n yeni satır
# \t tab boşluk bırakır

print(greeting[0]) # ilk karakter
print(greeting[3:7]) # 3. indexten 7. indexe kadar
print(greeting[:10]) # baştan 10. indexe kadar
print(greeting[5:]) # 5. indexten sona kadar
print(greeting[-1]) # sondan ilk karakter
print(greeting[-5:-1]) # sondan 5. karakterden sondan 1. karaktere kadar

print(len(greeting)) # karakter sayısı

print(greeting.lower()) # tüm karakterleri küçük yapar
print(greeting.upper()) # tüm karakterleri büyük yapar
print(greeting.replace('İclal', 'Ahmet')) # karakter değiştirme
print('Cebecioğlu' in greeting) # karakter arama
print('Ali' in greeting) # karakter arama
print(greeting.split()) # karakterleri boşluklardan ayırarak liste yapma
print(greeting.split('a')) # karakterleri 'a' harfinden ayırarak liste yapma
print(greeting.strip()) # baştaki ve sondaki boşlukları siler
print(greeting.startswith('My')) # cümlenin 'My' ile başlayıp başlamadığını kontrol etme
print(greeting.endswith('old.')) # cümlenin 'old.' ile bitip bitmediğini kontrol etme
print(greeting.count('a')) # cümledeki 'a' harfi sayısı
print(greeting.find('Cebecioğlu')) # 'Cebecioğlu' ifadesinin başladığı indexi bulma
print(greeting.index('Cebecioğlu')) # 'Cebecioğlu' ifadesinin başladığı indexi bulma
print(greeting.capitalize()) # cümlenin ilk harfini büyük yapma
print(greeting.title()) # cümlenin her kelimesinin ilk harfini büyük yapma
print(greeting.center(100)) # cümleyi 100 karakterlik alanda ortalama
print(greeting.ljust(100)) # cümleyi 100 karakterlik alanda sola yaslama
print(greeting.rjust(100)) # cümleyi 100 karakterlik alanda sağa yaslama
print(greeting.encode()) # cümleyi byte formatına çevirme
print(greeting.replace('\n', ' ')) # yeni satır karakterini boşlukla değiştirme
print(greeting.replace('\t', ' ')) # tab karakterini boşlukla değiştirme
print(greeting.isalpha()) # cümlenin sadece harflerden oluşup oluşmadığını kontrol etme
print(greeting.isdigit()) # cümlenin sadece rakamlardan oluşup oluşmadığını kontrol etme
print(greeting.islower()) # cümlenin tüm harflerinin küçük olup olmadığını kontrol etme
print(greeting.isupper()) # cümlenin tüm harflerinin büyük olup olmadığını kontrol etme
print(greeting.isspace()) # cümlenin sadece boşluk karakterlerinden oluşup oluşmadığını kontrol etme
print(greeting.zfill(100)) # cümleyi 100 karakterlik alanda başına sıfır ekleyerek doldurma
print(f"My name is {name} {surname} and \n I am {age} years old.")  # f-string kullanımı
surname_upper = surname.upper()
print(f"My name is {name} {surname_upper} and \n I am {age} years old.")  # f-string ile değişken işlemi
