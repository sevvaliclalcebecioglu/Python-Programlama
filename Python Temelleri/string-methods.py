message = " Hello there. My name is İclal."

# String metodları örnekleri

message = message.upper() # Hepsini büyük harfe çevirir

message = message.lower() # Hepsini küçük harfe çevirir

message = message.replace("İ", "I") # 'İ' harfini 'I' ile değiştirir

message = message.replace("ı", "i") # 'ı' harfini 'i' ile değiştirir

message = message.title() # Her kelimenin ilk harfini büyük yapar

message = message.strip() # Başındaki ve sonundaki boşlukları siler 

message = message.split(".") # Cümleyi noktalardan bölerek liste yapar

message = message.capitalize() # Sadece ilk harfi büyük yapar

message = message.split() # Kelimelere ayırır

message = ' '.join(message) # Kelimeleri ' ' ile birleştirir

message = '-'.join(message) # Kelimeleri '-' ile birleştirir

message = '*'.join(message) # Kelimeleri '*' ile birleştirir

index = message.find("İclal") # 'İclal' kelimesinin başladığı indexi bulur

isFound = message.startswith("H") # Mesajın 'H' ile başlayıp başlamadığını kontrol eder

isFound2 = message.endswith("n") # Mesajın 'n' ile bitip bitmediğini kontrol eder

message = message.replace("İclal", "Şevval") # 'İclal' kelimesini 'Şevval' ile değiştirir

message = message.replace(" ", "*") # Tüm boşlukları '*' ile değiştirir

message = message.center(100) # Mesajı 100 karakter genişliğinde ortalar

message = message.center(50, "*") # Mesajı 50 karakter genişliğinde '*' ile ortalar

# Örnek çıktılar

print(message) # Tüm mesajı yazdırır

print(message[0]) # İlk kelimeyi yazdırır

print(index)   # İndexi yazdırır

print(isFound) # Başlangıç kontrol sonucunu yazdırır

print(isFound2) # Bitiş kontrol sonucunu yazdırır


# Ekstra bilgi: Tüm string metodları için Python belgelerine bakabilirsiniz:
# https://docs.python.org/3/library/stdtypes.html#string-methods

