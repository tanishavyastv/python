string = "LuckyGuess"
pos = int(input("Enter the position of the character to print: "))
if 0 <= pos < len(string):
    print(f"The character at the specified position is: {string[pos]}")
else:
    print("Invalid position")

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")