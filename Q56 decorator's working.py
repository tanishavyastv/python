#WAP to demonstrate how decorators work

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
