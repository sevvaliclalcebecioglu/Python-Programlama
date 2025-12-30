name = 'İclal'
surname = 'Cebecioğlu'
age = 22

print('My name is {}'.format(name)) # My name is İclal  
print('My name is {} {}'.format(name, surname)) # My name is İclal Cebecioğlu
print('My name is {1} {0}'.format(name, surname)) # My name is Cebecioğlu İclal
print('My name is {n} {s}'.format(n=name, s=surname)) # My name is İclal Cebecioğlu 
print("My name is {} {} and I'm {} years old.".format(name, surname, '22')) # My name is İclal Cebecioğlu and I'm 22 years old.

# -------------------------------------------------------

result = 200 / 500

print('The result is {}'.format(result)) # The result is 0.4
print('The result is {r:1.3}'.format(r=result)) # The result is 0.400

# -------------------------------------------------------

print(f"My name is {name} {surname} and I'm {age} years old.") # My name is İclal Cebecioğlu and I'm 22 years old.
# Bu f-string yöntemi Python 3.6 ve üzeri sürümlerde kullanılabilir.

