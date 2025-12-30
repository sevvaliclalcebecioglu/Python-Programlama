message = 'Hello There!. My name is Şevval İclal.'.split()
print(message)  # ['Hello', 'There!.', 'My', 'name', 'is', 'Şevval', 'İclal.']

# List 

my_list = [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]

my_list2 = ['a', 'b', 'c', 'd']
print(my_list2)  # ['a', 'b', 'c', 'd']

my_list3 = [1, 'a', 2, 'b', 3, 'c']
print(my_list3)  # [1, 'a', 2, 'b', 3, 'c'] # Mixed Data Types

my_list4 = [1, 2, 3, [4, 5, 6], 7]
print(my_list4)  # [1, 2, 3, [4, 5, 6], 7] Operations on Lists  

print(len(my_list4))  # 5   # Length of the list

print(my_list4[3])  # [4, 5, 6]  # Accessing elements

my_list4[3][0] = 'Changed'
print(my_list4)  # [1, 2, 3, ['Changed', 5, 6], 7]  # Modifying elements    

my_list4.append(8)
print(my_list4)  # [1, 2, 3, ['Changed', 5, 6], 7, 8]  # Adding elements    

my_list4.remove(2)
print(my_list4)  # [1, 3, ['Changed', 5, 6], 7, 8]  # Removing elements 

popped_element = my_list4.pop()
print(popped_element)  # 8  # Popped element