'''
ogrenciler = {
    '1001': {
    'ad': 'Ali', 
    'soyad': 'Yılmaz', 
    'notlar': [85, 90, 78]
    },
    '1002': {
    'ad': 'Ayşe', 
    'soyad': 'Kara', 
    'notlar': [88, 92, 80]
    },
    '1003': {
    'ad': 'Mehmet', 
    'soyad': 'Demir', 
    'notlar': [70, 75, 68]
    },
}   

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilere göre dictionary yapısında saklama

2- Öğrenci numarasını kullanıcıdan alıp bilgilerini gösterme

'''

# 1- Öğrenci bilgilerini saklama
ogrenciler = {}   

while True:
    ogr_no = input("Öğrenci numarasını girin (çıkmak için 'q'): ")
    if ogr_no.lower() == 'q':
        break
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")
    notlar = input("Öğrencinin notlarını virgülle ayrılmış şekilde girin: ")
    notlar_listesi = [int(not_) for not_ in notlar.split(',')]
    
    ogrenciler[ogr_no] = {
        'ad': ad,
        'soyad': soyad,
        'notlar': notlar_listesi
    }


# 2- Öğrenci numarasına göre bilgileri gösterme
while True: 
    sorgu_no = input("Bilgilerini görmek istediğiniz öğrenci numarasını girin (çıkmak için 'q'): ")
    if sorgu_no.lower() == 'q':
        break
    if sorgu_no in ogrenciler:
        ogrenci = ogrenciler[sorgu_no]
        print(f"Öğrenci Numarası: {sorgu_no}")
        print(f"Ad: {ogrenci['ad']}")
        print(f"Soyad: {ogrenci['soyad']}")
        print(f"Notlar: {ogrenci['notlar']}")
    else:
        print("Bu öğrenci numarası bulunamadı.")    

            



