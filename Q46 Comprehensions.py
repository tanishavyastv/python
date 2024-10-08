print('List Comprehensions:'.upper())
squares = [x**2 for x in range(10)] 
even_squares = [x**2 for x in range(10) if x % 2 == 0] 
print("Squares:", squares)
print("Even squares:", even_squares)

print('\nList Comprehension with Condition:'.upper())
even = [x for x in range(10) if x % 2 == 0]
print('Even Numbers:', even)

print('\nSet Comprehension with Condition:'.upper())
squares = {x**2 for x in range(10)}
print('Squares:',squares)

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
