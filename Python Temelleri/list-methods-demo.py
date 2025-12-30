names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")

# 2- "Sena" değerini listenin başına ekleyiniz.

names.insert(0, "Sena")

# 3- "Deniz" ismini listeden siliniz.

names.remove("Deniz")

# 4- "Ali" isminin indeksi nedir?

index_ali = names.index("Ali")

# 5- "Deniz" ismi listede var mı?   

is_deniz_in_list = "Deniz" in names

# 6- years listesini küçükten büyüğe sıralayınız.

years.sort()

# 7- names listesini alfabetik olarak sıralayınız.

names.sort()

# 8- years listesini büyükten küçüğe sıralayınız.

years.sort(reverse=True)

# 9- years listesinin en büyük ve en küçük elemanı nedir?

max_year = max(years)
min_year = min(years)

# 10- years listesinin toplamı nedir?

sum_years = sum(years)

# 11- names listesini ters çeviriniz.

names.reverse()

# 12- years listesini siliniz.

years.clear()

# 13- Kullanıcıdan alacağınız 3 tane isim bilgisini bir listede saklayınız.     

user_names = []
for i in range(3):
    name = input("Lütfen bir isim giriniz: ")
    user_names.append(name)
print("Kullanıcı tarafından girilen isimler:", user_names)

# 14- Kullanıcıdan alacağınız 5 tane sayı bilgisini bir listede saklayınız ve bu sayıların toplamını ekrana yazdırınız.

user_numbers = []
for i in range(5):
    number = int(input("Lütfen bir sayı giriniz: "))
    user_numbers.append(number) 
total_sum = sum(user_numbers)
print("Girilen sayıların toplamı:", total_sum)

    