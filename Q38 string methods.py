text = "    tAnIsHa VyAs      "
print('Changing case:'.upper())
print(text.lower())
print(text.upper())
print(text.title())
print('\nRemoving white space:'.upper())
txt = text.strip()
print(txt)
print("-".join(txt))

print('\nReplace and finding:'.upper())
txt = txt.replace(txt, "Tanisha Vyas")
print(txt)
print(txt.find("s"))
print(txt.count("a"))

print("\nTraversing the string:".upper())
for char in txt:
    print(char, end=' ')

print("\n\nThis program is written by Tanisha. \nERPID: 0221BCA066")
