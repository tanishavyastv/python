string = "LuckyGuess"
char_to_find = input("Enter the character you want to find: ")
pos = [i for i, char in enumerate(string) if char == char_to_find]
if pos:
    print(f"The character '{char_to_find}' is found at positions: {pos}")
else:
    print(f"The character '{char_to_find}' is not found in the string.")

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")