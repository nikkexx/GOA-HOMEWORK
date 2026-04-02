import turtle 

names = []
surname = []
ages = []
passwords = []
user_courses = []
available_courses = ["Robotics 🤖", "Web-Development 🌐", "Game-Development 🎮", "Graphic-Design 🎨"]
prices = [300, 250, 200, 150]

run = True


print("""
======================================================
||                                                  ||
||      🚀 WELCOME TO GOA - GENERATION OF CHADS     ||
||         BECOME A REAL CHAD & PROGRAMMER          ||
||                                                  ||
||             _______  _______   ________          ||
||            |  _____||  ___  | |  ____  |         ||
||            | |  ___ | |   | | | |____| |         ||
||            | | |_  || |   | | |________|         ||
||            | |___| || |___| | | |    | |         ||
||            |_______||_______| |_|    |_|         ||
||                                                  ||
||======================∨∨∨=========================||
""")


while run:
    print("\n" + "✨" + "═══" * 15 + "✨")
    print("       💎 GOA ACADEMY - MAIN MENU 💎")
    print("  1 | 🏆 [JOIN]    - გახდი ნამდვილი CHAD (Registration)")
    print("  2 | 🔍 [EXPLORE] - GOA-ს კურსები & ფასები")
    print("  3 | ⚡ [CHOOSE]  - კურსის არჩევა")
    print("  4 | 👤 [STATUS]  - ჩემი მონაცემები")
    print("  5 | 🚪 [EXIT]    - გასვლა")
    print("✨" + "═══" * 15 + "✨")

    choice = input("\n👉 აირჩიე (1-5): ")
    # რეგისტრაცია
    if choice == "1":
        print("\n🔥 " + "═" * 10 + " REGISTRATION " + "═" * 10 + " 🔥")
        new_name = input("✍️ თქვენი სახელი: ")
        new_surname = input("✍️ თქვენი გვარი: ")
        new_age = int(input("🎂 თქვენი ასაკი: "))
        new_pass = input("🔐 შექმენით პაროლი: ")


        if new_age >= 8 and new_age <=60:
            names += [new_name]
            surname += [new_surname]
            ages += [new_age]
            passwords += [new_pass]
            user_courses += [""]

            print(f"✅ {new_name} წარმატებით დარეგისტრიტდი! 💪")

        elif new_age <= 8 or new_age >= 60:
            print('ასაკი მიუღებელია, გთხოვთ დატოვეთ ეს გვერდი!❌')

     # 2. კურსების დათვალიერება
    elif choice == "2":
        print("\n🚀 " + "═" * 10 + " GOA COURSE CATALOG " + "═" * 10)
        # ვიყენებთ len()-ს სიის სიგრძის გასაგებად
        for i in range(len(available_courses)):
            print(f"🔹 {i + 1}. {available_courses[i]} | 💰 ფასი: {prices[i]} ლარი")
        print("═" * 45)

     #. კურსის არჩევა
    elif choice == "3":
        #  შემოწმება არის თუ არა მომხმარებელი დარეგისტრირებული
         if names == []:
             print("\n❌ ჯერ გაიარეთ რეგისტრაცია (დააჭირეთ 1-ს)!")
         else:
             print("\n" + "---" * 5 + "აირჩიე შენი საყვარელი კურსი" + "---" * 5)   

             index_show = 0

             for course in available_courses:
              print(f"{index_show + 1}. {course}")
              index_show = index_show + 1

            
             course_num = int(input("შეიყვანეთ კურსის ნომერი (1-4): "))    

             if course_num >= 1 and course_num <= 4:
                selected_course = available_courses[course_num - 1]
                
                user_courses[-1] = selected_course

                print(f"გილოცავთ! თქვენ აირჩიეთ {selected_course}")
                import turtle


                t = turtle.Turtle()
                t.speed(5)
                t.width(4)
                t.color("black")
                t.hideturtle()
                t.penup()
                # 1. გარე ჩარჩო
                t.goto(-320, 220)
                t.pendown()
                i = 0

                while i < 2:
                    t.forward(640)
                    t.right(90)
                    t.forward(440)
                    t.right(90)
                    i = i + 1
                t.penup()
                # 2. შიდა ჩარჩო (ვიყენებთ ისევ i-ს, ოღონდ თავიდან ვანიჭებთ 0-ს)
                t.goto(-310, 210)
                t.width(2)
                t.pendown()
                i = 0 # აქ i ისევ გავანულეთ

                while i < 2:
                    t.forward(620)
                    t.right(90)
                    t.forward(420)
                    t.right(90)
                    i = i + 1          

                t.penup()
                # 3. ტექსტები (უბრალოდ goto და write)
                t.goto(-100, 160)
                t.write("=== GOA ACADEMY ===")
                t.goto(-100, 130)
                t.write("GENERATION OF CHADS")

               # ხაზი
                t.goto(-150, 110)
                t.pendown()
                t.forward(300)
                t.penup()
                t.goto(-120, 50)
                t.write("Certificate for Real Chad:")  
                t.goto(-120, 10)
                t.write(">>> " + names[-1] + " " + surname[-1] + " <<<")            
                t.goto(-120, -50)
                t.write("Course: " + selected_course)            
                t.goto(-120, -120)
                t.write("BECOME A REAL PROGRAMMER!")
                t.goto(-120, -140)
                t.write("**************************")

             else:
                 if course_num <= 0 or course_num >= 5:
                     print('არასწორი კურსი არის მითითებული!')

                     
    

           
           
    elif choice == "4":
        if len(names) == 0:
            print("\n📭 ბაზა ცარიელია!")
        else:
            print("\n" + "👤 " + "═" * 10 + " PROFILE INFO " + "═" * 10)
            # ბოლო დარეგისტრირებული მომხმარებლის ნახვა
            print(f"🆔 სახელი: {names[-1]}")
            print(f"🆔 გვარი: {surname[-1]}")
            print(f"🎂 ასაკი: {ages[-1]}")
            print(f"📚 კურსი: {user_courses[-1]}")
            print("═" * 35)
                
           
                         
    # 5. გასვლა
    elif choice == "5":
        print("\n👋 ნახვამდის! არ დაგავიწყდეს - სირბილით სახლში! 🏃‍♂️💨")
        run = False
        
    else:
        print("\n❌ არასწორი არჩევანი!")