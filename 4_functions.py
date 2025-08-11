#functions.py using type hints, defining various functions and their return types

#defining a function
def function_name():
    print("this is the body of the function")

function_name()


#function with default parameter or value
def add(x, y=3):
    return x + y

print(add(2))  # Output: 5
print(add(2, 5))  # Output: 7


#function with type hints
def multiply(x: int, y: int) -> int:
    return x * y

print(multiply(2, 3))  # Output: 6

#function with multiple return values
def divide(x: int, y: int) -> tuple[int, float]:
    quotient = x // y
    remainder = x % y
    return quotient, remainder
print(divide(10, 3))  # Output: (3, 1.0)
a = divide(10, 3)
print(type(a))  # Output: <class 'tuple'> since comma separeated values are returned as a tuple in Python by default

#function with variable number of arguments
def concatenate(*args: str) -> str:
    return ' '.join(args)
print(concatenate("Hello", "world!"))  # Output: Hello world!

#function with keyword arguments
def print_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age="30")  # Output: name: Alice, age
# 30

#functions with positional arguments
def add(x: int, y: int, z: int) -> int:
    return x + y * z
print(add(2, 3, 4))  # Output: 14