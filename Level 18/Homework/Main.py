# 2) საშუალო მნიშვნელობა
def average(numbers):
    return sum(numbers) / len(numbers)


# 3) ლუწი რიცხვების რაოდენობა
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# 4) კენტი რიცხვების რაოდენობა
def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count


# 5) თითოეული ელემენტის გაორმაგება
def double_values(lst):
    new_list = []
    for num in lst:
        new_list.append(num * 2)
    return new_list


# 6) თითოეული ელემენტის კვადრატში აყვანა
def square_values(lst):
    new_list = []
    for num in lst:
        new_list.append(num ** 2)
    return new_list


# 7) სამი რიცხვის ჯამი
def sum_three(a, b, c):
    return a + b + c


# 8) ორი რიცხვის სხვაობა
def substract(a, b):
    return a - b


# 9) ორი რიცხვის ნამრავლი
def multiply(a, b):
    return a * b


# 10) ასაკის შემოწმება
def check_age(age):
    if age >= 18:
        print("Access Granted")
    else:
        print("Access Denied")


# 11) სახელების დაბეჭდვა
def print_names(names):
    for name in names:
        print(name)


# 12) ლუწი თუ კენტი
def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 13) მოსწავლის შეფასება
def student_grade(score):
    if 90 <= score <= 100:
        print("A")
    elif 70 <= score <= 89:
        print("B")
    elif 50 <= score <= 69:
        print("C")
    else:
        print("F")


# 14) მომხმარებლის ინფორმაცია წინადადების სახით
def user_info(name, surname, age):
    return f"User: {name} {surname}, Age: {age}"