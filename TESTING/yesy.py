names = []
surname = []
ages = []
passwords = []
user_courses = []
available_courses = ["Robotics", "Web-Development", "Game-Development", "Graphic-Design"]
prices = [300, 250,  200]



print("======================================================")
print("||                                                  ||")
print("||    WELCOME TO GOA - GENERATION OF CHADS          ||")
print("||     'BECOME A REAL CHAD AND PROGRAMMER'          ||")
print("||                       |                          ||")
print("||                       |                          ||")
print("||                       |                          ||")
print("||======================∨∨∨=========================||")

run = True

while run:
    print( "\n" + "📌" +  "___" * 5 + " GOA აკადემია " + "___" * 5)
    print("1 | [JOIN] - გახდი ნამდვილი CHAD (Registration)")
    print("2 | [EXPLORE] - GOA-ს კურსები & ფასები")
    print("3 | [CHOOSE] - კურსის არჩევა")
    print("4 | [MY STATUS] - ჩემი მონაცემები")
    print("5 | [EXIT] - გასვლა")
    print("-" * 43)

    choice = input("\n👉 აირჩიე (1-5): ")

    if choice == "1":
        print("\n🔥 >>> REGISTRATION  <<< 🔥")
        new_name = input("თქვენი სახელი: ")
        new_surname = input("თქვენი გვარი: ")
        new_age = int(input("თქვენი ასაკი: "))
        new_pass = input("შექმენით პაროლი: ")





