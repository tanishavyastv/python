roll_no = input('Enter your Roll Number: ')
name = input('Enter your Name: ')
Class = input('Enter your Class: ')

print('\nEnter your Marks out of 100')
eng = int(input('English: '))
math = int(input('Mathematics: '))
sci = int(input('Science: '))
ssc = int(input('Social Science: '))
comp = int(input('Computer: '))

print(f'\nRoll no.: {roll_no}')
print(f'Name: {name}')
print(f'Class: {Class}')

print('\n-----------------------------------------------')
print('Subject \t Full Marks \t Obtained Marks')
print(f'English \t 100 \t\t {eng}')
print(f'Mathematics \t 100 \t\t {math}')
print(f'Science \t 100 \t\t {sci}')
print(f'Social Science \t 100 \t\t {ssc}')
print(f'Computer \t 100 \t\t {comp}')
print('-----------------------------------------------')
total = eng + math + sci + ssc + comp
print(f'Total \t\t 500 \t\t {total}\n')

marks = total/5

if marks >= 80:
    print('Your Grade is O.')
elif marks >= 70:
    print('Your Grade is A+.')
elif marks >= 60:
    print('Your Grade is A.')
elif marks >= 50:
    print('Your Grade is B+.')
elif marks >= 40:
    print('Your Grade is B.')
else:
    print('Your Grade is D.\nYou are fail!\nSTUPID LOSER!!!')

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
