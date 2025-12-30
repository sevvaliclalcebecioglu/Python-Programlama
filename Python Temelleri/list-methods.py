numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e'] 

val = min(numbers)
print("Min value in numbers:", val) # Min value in numbers: 1

val = max(letters)
print("Max value in letters:", val) # Max value in letters: e   

val = sum(numbers)
print("Sum of numbers:", val) # Sum of numbers: 15

val = sorted(letters)
print("Sorted letters:", val) # Sorted letters: ['a', 'b', 'c', 'd', 'e']

val = sorted(numbers, reverse=True)
print("Sorted numbers in descending order:", val) # Sorted numbers in descending order: [5, 4, 3, 2, 1]

val = list(reversed(letters))
print("Reversed letters:", val) # Reversed letters: ['e', 'd', 'c', 'b', 'a']

val = numbers[3:6] 
print("Sliced numbers (index 3 to 5):", val) # Sliced numbers (index 3 to 5): [4, 5]

numbers.append(6)
print("Numbers after append:", numbers) # Numbers after append: [1, 2, 3, 4, 5, 6]

letters.insert(2, 'z')
print("Letters after insert:", letters) # Letters after insert: ['a', 'b', 'z', 'c', 'd', 'e']

numbers.remove(3)
print("Numbers after remove 3:", numbers) # Numbers after remove 3: [1, 2, 4, 5, 6] 

letters.pop()
print("Letters after pop:", letters) # Letters after pop: ['a', 'b', 'z', 'c', 'd'] 

letters.pop(0)
print("Letters after pop index 0:", letters) # Letters after pop index 0: ['b', 'z', 'c', 'd']

letters.pop(-1)
print("Letters after pop last element:", letters) # Letters after pop last element: ['b', 'z', 'c']

# daha fazla liste metodu için:
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists


