# type() ფუნქცია გვიჩვენებს რა ტიპის მონაცემია მოცემული მნიშვნელობა.
# მაგალითად: int, float, str, bool და ა.შ.

print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type([1, 2, 3]))   # <class 'list'>

#3)
name = "Nika"
surname = "Nikuradze"
age = 15

# age არის int და ტექსტთან პირდაპირ ვერ დავაკავშირებთ ამიტომ უნდა გადავიყვანოთ str ტიპში
sentence = "I am " + name + " " + surname + " and I am " + str(age) + " years old"

print(sentence)

# 4)
num1 = float(input("Enter first decimal number: "))
num2 = float(input("Enter second decimal number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# 5)
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

sum_numbers = num1 + num2 + num3 + num4 + num5
average = sum_numbers / 5

print("Average is:", average)

# 6)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# 7)
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius:", celsius)