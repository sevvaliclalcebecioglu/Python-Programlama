# key - value çiftlerinden oluşan bir veri yapısıdır
# sözlükler mutable (değiştirilebilir) veri tipleridir
# süslü parantez {} ile tanımlanır
# anahtarlar (keys) benzersiz olmalıdır, değerler (values) ise tekrar edebilir

# boş bir sözlük oluşturma

my_dict = {}

# anahtar - değer çiftleri ekleme

my_dict["isim"] = "Ali"
my_dict["yaş"] = 25
my_dict["şehir"] = "İstanbul"
print(my_dict)  # {'isim': 'Ali', 'yaş': 25, 'şehir': 'İstanbul'}

# bir anahtarın değerine erişme

print(my_dict["isim"])  # Ali

# bir anahtarın değerini güncelleme

my_dict["yaş"] = 26
print(my_dict)  # {'isim': 'Ali', 'yaş': 26, 'şehir': 'İstanbul'}

# --------------*------------------

users = {

    'sadikturan': 36,
    'cınarturan': 32
}

print(users['sadikturan'])  # 36
print(users['cınarturan'])  # 32    
print(users)  # {'sadikturan': 36, 'cınarturan': 32}

users2 = {

    'sadikturan': {
        'age': 36,              
        'email': 'sadik@gmail.com', 
        'address': 'İstanbul',
    },
    'cınarturan': {
        'age': 32,
        'email': 'cınar@gmail.com',
        'address': 'Ankara',
    }
}

print(users2['sadikturan'])
# {'age': 36, 'email': 'sadik@gmail.com', 'address': 'İstanbul'}

print(users2['sadikturan']['email'])  # 'sadik@gmail.com'  
 
print(users2['cınarturan']['address'])  # 'Ankara'

print(users2)
# {'sadikturan': {'age': 36, 'email': 'sadik@gmail.com', 'address': 'İstanbul'}, 'cınarturan': {'age': 32, 'email': 'cınar@gmail.com    , 'address': 'Ankara'}} 


#   ----------------*------------------    