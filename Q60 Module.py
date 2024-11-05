# Creating a Module
def add(x, y): 
    return x + y 
def subtract(x, y): 
    return x - y 

# Using a Module
import math_utils 
result = math_utils.add(5, 3) 
print(result)

# Importing Specific Functions 
from math_utils import add 
result = add(5, 3) 
print(result)

# Importing All Functions 
from math_utils import * 
result = subtract(10, 5) 
print(result)

# Aliasing Modules and Functions 
import math_utils as mu 
result = mu.add(5, 3) 
print(result)

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")