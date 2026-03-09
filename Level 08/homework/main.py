# 2) ყველა შედარების ოპერატორი და მაგალითები

# == ტოლია
print(5 == 5)   # True
print(10 == 3)  # False

# != არ არის ტოლი
print(5 != 3)   # True
print(7 != 7)   # False

# > მეტია
print(10 > 5)   # True
print(2 > 8)    # False

# < ნაკლებია
print(3 < 7)    # True
print(9 < 4)    # False

# >= მეტია ან ტოლია
print(10 >= 10) # True
print(5 >= 8)   # False

# <= ნაკლებია ან ტოლია
print(4 <= 4)   # True
print(9 <= 3)   # False


# 3) ლოგიკური ოპერატორები

# and - აბრუნებს True-ს მხოლოდ მაშინ როცა ორივე პირობა True არის
print(True and True)    # True
print(True and False)   # False

# or - აბრუნებს True-ს თუ ერთ-ერთი პირობა მაინც True არის
print(True or False)    # True
print(False or False)   # False

# not - აბრუნებს მნიშვნელობის საპირისპიროს
print(not True)         # False
print(not False)        # True


# 4) 

my_height = 180  
user_height = int(input("Enter your height in cm: ")) 
print(user_height > my_height)  


# 5) 

num1 = "21"   # სტრინგი (string)
num2 = 21     # მთელი რიცხვი (integer)

print(num1 == num2)  
# შედეგი არის False რადგან ერთი არის ტექსტი ("21") და მეორე რიცხვი (21)
# Python-ში სხვადასხვა ტიპის მონაცემები ერთმანეთს არ უდრის


# 6)

my_surname = "Nikuradze"  
user_surname = input("Enter your surname: ") 
print(my_surname == user_surname)  



# 7) 

print(False or True and True and False)
# ჯერ სრულდება and ოპერაციები
# True and True = True
# True and False = False
# რჩება False or False -> False

print(True and False or False or True)
# True and False = False
# რჩება False or False or True -> True

print(True or True and False or True or False and True or False)
# True and False = False
# False and True = False
# რჩება True or False or True or False or False -> True


# 8) 

temp = int(input("Enter temperature in Celsius: "))  

cooling_system = temp > 30  
print(cooling_system)


# 9) 

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

cooling_system = fahrenheit > 89.6

print(cooling_system)

num = 0
while num <6:
    print(num)