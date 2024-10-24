# Function to add two numbers
def add(a, b):
    return a + b
sum_result = add(10, 5)
print("Sum of 10 and 5 is:", sum_result)
print()
# Function with a default parameter
def greet(name="Guest"):
    print("Hello", name)
greet("Tanisha")
greet()
print()
# Function that demonstrates multiple returns
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val
sum_val, diff_val = calculate(10, 5)
print("Sum is:", sum_val)
print("Difference is:", diff_val)
print()
# Function that returns a list
def get_numbers():
    return [1, 2, 3, 4, 5]
numbers = get_numbers()
print("List returned by function:", numbers)

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
