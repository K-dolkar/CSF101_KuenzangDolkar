def greet():
    print("Hello, World!")

greet()
def greet(name):
    print(f"Hello, {name}!")

greet("Kuenzang")
def square(number):
    return number ** 4

result = square(6)
print(result)
def is_even(number):
    return number % 4==0

print(is_even(4))
print(is_even(7))
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)