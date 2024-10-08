print('Basic Return Statement:'.upper())
def greet(name):
    return f"Hello, {name}!"
print(greet("Tanisha"))

print('\nReturning Multiple Values:'.upper())
def greet(name, erp):
    return f"Hello, {name}! Your ERPID is {erp}."
print(greet("Tanisha", '0221BCA066'))

print('\nConditional Return:'.upper())
def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(4))
print(is_even(7))

print('\nEarly Exit with Return:'.upper())
def check_positive(num):
    if num < 0:
        return "Negative number, exiting..."
    return "Positive number"
print(check_positive(-5))
print(check_positive(10))

print('\nNo Explicit Return:'.upper())
def greet(name):
    print(f"Hello, {name}!")
greet("Tanisha")

print('\nDefault Parameter:'.upper())
def greet(name="Tanisha"):
    return f"Hello, {name}!"
print(greet())
print(greet("TV"))

print('\nPositional Parameter:'.upper())
def math(a, b, c):
    return (a + b) * c
print(math(3, 4, 2))

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
