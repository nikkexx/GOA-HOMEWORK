# 3) ლუწია თუ კენტი
num = int(input(" Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 4) ტემპერატურის შემოწმება
temp = int(input(" Enter temperature: "))
if temp > 30:
    print("It's Hot")
elif temp >= 15:
    print("It's Warm")
else:
    print("It's Cold")


# 5) Positive even / odd / Negative
num = int(input(" Enter number: "))
if num < 0:
    print("Negative")
elif num % 2 == 0:
    print("Positive even")
else:
    print("Positive odd")


# 6) 0-დან რიცხვამდე Even/Odd
num = int(input(" Enter number: "))
for i in range(num + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")


# 7) 10 რიცხვი (დადებითი, უარყოფითი, ნული)
positive = 0
negative = 0
zero = 0

print(" Enter 10 numbers:")
for i in range(10):
    num = int(input())
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)


# 8) სიის შეცვლა
print(" Fruits list change:")
fruits = ["apple", "banana", "orange", "grape"]
fruits[1] = "kiwi"
print(fruits)


# 9) პირველი + ბოლო ელემენტი
print(" Sum of first and last element:")
nums = [4, 8, 12, 16, 20]
result = nums[0] + nums[-1]
print(result)


# 10) სიის თითოეული წევრი
print(" Print each element:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)


# 11) მხოლოდ ლუწი რიცხვები
print(") Even numbers:")
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    if num % 2 == 0:
        print(num)


# 12) ლუწი რიცხვების ჯამი
print(") Sum of even numbers:")
nums = [1, 2, 3, 4, 5, 6]
total = 0
for num in nums:
    if num % 2 == 0:
        total += num
print(total)


# 13) 6-ზე მეტი რიცხვები
print(" Numbers greater than 6:")
nums = [2, 5, 7, 10, 3, 8]
for num in nums:
    if num > 6:
        print(num)


# 14) სიტყვის ასოები
print(" Letters in word:")
word = "hello"
for letter in word:
    print(letter)


# 15) პირველი სამი წევრი
print(" First three elements:")
my_list = [10, 20, 30, 40, 50]
print(my_list[:3])