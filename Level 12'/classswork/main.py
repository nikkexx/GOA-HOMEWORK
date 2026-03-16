num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("zero")    
    
password = "python123"
while True:
    user_input = input("Enter password: ")

    if user_input == password:
           print("Access gnated. ")
    else:
         print("Wrong password, try again")   


fruits=["banana" , "apple" , "orange" , "mango" , "cherry"] 
print(fruits[1])

print(fruits[2])

print(fruits[4])