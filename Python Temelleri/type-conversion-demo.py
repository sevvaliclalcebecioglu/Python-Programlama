'''
    Daire alanını hesaplayan bir program yazın.
    Kullanıcıdan yarıçapı alın ve alanı hesaplayın. (r: 3.14)

    Alan formülü: π * r^2
    Daire çevresi formülü: 2 * π * r
'''

pi = 3.14

r = float(input("Dairenin yarıçapını girin: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Dairenin alanı:", alan)
print("Dairenin çevresi:", cevre)