# username, password => database

# 'sadikturan' , '123456'

a, b, c, d = 5, 5, 10, 4

password = '123456'
username = 'sadikturan'

result = (a == b) # true
print("a eşit b'ye:", result)

result = (a == c) # false
print("a eşit c'ye:", result)

result = (('sdktrn') == username)  # false
print("username eşit sdktrn'ye:", result)

result = (a != b) # false
print("a eşit değil b'ye:", result)

result = (a != c) # true
print("a eşit değil c'ye:", result)

result = (a > b) # false
print("a büyük mü b'den:", result)

result = (c > a) # true
print("c büyük mü a'dan:", result)

result = (a >= c) # false
print("a büyük eşit mi c'den:", result)

result = (True == 1) # true
print("True eşit mi 1'e:", result)

result = (False == 0) # true
print("False eşit mi 0'a:", result)

result = False+ True+40 # 41
print("False + True + 40 sonucu:", result)


