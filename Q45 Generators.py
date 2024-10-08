print('Simple Generator:'.upper())
def count_up_to(num): 
    count = 1 
    while count <= num: 
        yield count 
        count += 1 
for num in count_up_to(5): 
    print(num, end=' ')

print('\n\nFibonacci Generator:'.upper())
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
a = list(fibonacci(10))
print(', '.join(map(str, a)))

print('\nChain Generator:'.upper())
def square(numbers):
    for number in numbers:
        yield number ** 2
for sq in square(count_up_to(5)):
    print(sq, end=' ')

print('\n\nCountdown Generator:'.upper())
def countdown(start):
    while start >= 0:
        yield start
        start -= 1
print(' -> '.join(str(num) for num in countdown(5)))

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
