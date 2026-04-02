names = []
surnames = []
ages = []
passwords = []
user_courses = []
available_courses = ["Python", "JavaScript", "Data Science", "Web Development"]
prices = [300, 250, 200, 150]

run = True 

while run:
    print("\n" + "✨" + "═══" * 15 + "✨")
    print("       💎 GOA ACADEMY - MAIN MENU 💎")
    print("  1 | 🏆 [JOIN]    - Register")
    print("  2 | 🔍 [EXPLORE] - Explore Courses & Prices")
    print("  3 | ⚡ [CHOOSE]  - Choose a Course")
    print("  4 | 👤 [STATUS]  - My Data")
    print("  5 | 🚪 [EXIT]    - Exit")
    print("✨" + "═══" * 15 + "✨")

    choice = input("\n👉 Choose (1-5): ")

    if choice == '1':
        print("\n🔥 " + "═" * 10 + " REGISTRATION " + "═" * 10 + " 🔥")
        new_name = input("✍️ Your Name: ")
        new_surname = input("✍️ Your Surname: ")
        new_age = int(input("🎂 Your Age: "))
        new_pass = input("🔐 Create a Password: ")
        if new_age >= 8 and new_age <= 60:
            names.append(new_name)
            surnames.append(new_surname)
            ages.append(new_age)
            passwords.append(new_pass)
            user_courses.append("")
            print(f"✅ {new_name} successfully registered! 💪")
        else:
            print('Age is not acceptable, please leave this page!❌') 

    if choice == '2':
        print("\n🔥 " + "═" * 10 + " AVAILABLE COURSES " + "═" * 10 + " 🔥")
        for i in range(len(available_courses)):
            print(f"{i + 1} | {available_courses[i]} - ${prices[i]}")


    if choice == '3':
        print("\n🔥 " + "═" * 10 + " CHOOSE A COURSE " + "═" * 10 + " 🔥")
        for i in range(len(available_courses)):
            print(f"{i + 1} | {available_courses[i]} - ${prices[i]}")
            course_choice = int(input("\n👉 Choose a course (1-4): "))
            if course_choice >= 1 and course_choice <= len(available_courses):
                user_courses[- 1] = available_courses[course_choice - 1]
                print(f"✅ You have chosen {available_courses[course_choice - 1]}! 💪")       


 