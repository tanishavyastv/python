print('Pattern I')
for i in range(1,6):
    print('* ' * i)

print('\nPattern II')
for i in range(5,0,-1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

print('\nPattern III')
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

print('\nPattern IV')
for i in range(1, 6):
    print(" " * (5 - i) * 2, end="")
    print("* " * i)

print('\nPattern V')
for i in range(1,6):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()

print('\nPattern VI')
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

print('\nPattern VII')
for i in range(5,0,-1):
    for j in range(5,5-i,-1):
        print(j, end=' ')
    print()

print('\nPattern VIII')
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

print('\nPattern IX')
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)
    
print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")