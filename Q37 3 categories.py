'''WAP to print the numbers in 3 categories:-
1) Even 2) Odd 3) Divisible by 5
'''
num1 = int(input("Enter the starting number (number1): "))
num2 = int(input("Enter the ending number (number2): "))
evens = []
odds = []
divisible_by_5 = []
for num in range(num1, num2 + 1):
    if num % 5 == 0:
        divisible_by_5.append(num)
    elif num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(f"Even numbers: {evens}")
print(f"\nOdd numbers: {odds}")
print(f"\nNumbers divisible by 5: {divisible_by_5}")

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
