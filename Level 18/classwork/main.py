#1 
def greet(name):
    return f"Hello {name}"

print(greet("Nika"))
# 2
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 8))
# 3
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd" 
     
print(even_or_odd(10))    
print(even_or_odd(7))  

# 4
def numbers(one, two ):
    return one ** two

print(numbers(2, 3))
print(numbers(5, 2))

# 5
def string_lenght(string):
    return len(string)

print(string_lenght("Hello, World!"))

# 6
def reverse_string(string):
    return string[::-1]

print(reverse_string("JavaScript"))

# 7
def sum_lists(numbers):
    return sum(numbers)
print(sum_lists([2, 4 , 6, 8]))


def check_adult(name, age):
    if age >= 18:
        return f"{name} is adult"
    else:
        return f"{name} is not adult"

print(check_adult("Nika", 16))
print(check_adult("Luka", 20))        





