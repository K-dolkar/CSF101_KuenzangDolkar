number = 20
if number > 0:
    print("The number is positive.")
else:
    print("The number is non-positive.")
number = 10
if number > 10:
    print("The number is positive.")
elif number < 10:
    print("The number is negative.")
else:
    print("The number is zero.")
score = 75
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")
number = 9
result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}.")
num1 = 20
num2 = 15
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")