#Wap to demonstrate decorators with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=5)
def greet(name):
    print(f"Hello, {name}!")
greet("Tanisha")

print("\nThis program is written by Tanisha. \nERPID: 0221BCA066")
