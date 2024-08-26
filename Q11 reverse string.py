string = "live stressed"
#alternative method to print the reverse-print(string[::-1])
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("original string: ", string)
print("Reversed  string: ", reversed_string)

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")