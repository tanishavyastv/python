num = int(input('Enter a number: '))
Sum = 0
for i in range(1, num):
    if num % i == 0:
        Sum += i
if Sum == num:
    print(num, "is a Perfect number.")
else:
    print(num, "is not Perfect number.")

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print(num, "is a Prime number.")
else:
    print(num, "is not a Prime number.")

total = 0
digits = str(num)
length = len(digits)

for d in digits:
    total += int(d) ** length

if num == total:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
