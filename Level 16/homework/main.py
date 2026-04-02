# 2) 5 რიცხვი სიაში და საშუალო არითმეტიკული
nums = []

for i in range(5):
    n = float(input("Enter number: "))
    nums.append(n)

average = sum(nums) / len(nums)
print("Average is:", average)


# 3) წინადადების სიგრძე
sentence = input("Enter a sentence: ")
print("Length:", len(sentence))


# 4) პაროლი შეიცავს თუ არა '1'-ს
password = input("Enter your password: ")

if password.find("1") != -1:
    print("Password contains number 1")
else:
    print("Password does NOT contain number 1")


# 5) fruits სია, cherry დამატება, შეცვლა
fruits = ["apple", "banana", "orange", "grape"]

fruits.append("cherry")
fruits[3] = "Blueberry"

print(fruits)


# 6) სიტყვის პირველი ასო დიდი?
word = input("Enter a word: ")

if word[0].isupper():
    print("Perfect")
else:
    print("Your word should be capitalized!")


# 7) სახელი და გვარი Uppercase / Lowercase
name = input("Enter your name: ")
surname = input("Enter your surname: ")

print("Uppercase:", name.upper(), surname.upper())
print("Lowercase:", name.lower(), surname.lower())


# 8) სახელების შედარება (case insensitive)
my_name = "Nika"

user_name = input("Enter your name: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")


# 9) .find() ინდექსის პოვნა
text = "Programming"
index = text.find("g")
print("Index of 'g':", index)


# 10) სტრინგების სია Uppercase for-ით
words = ["hello", "world", "python", "code"]

for w in words:
    print(w.upper())


# 11) ცარიელი სია და 3 მონაცემი
data = []

for i in range(3):
    value = input("Enter something: ")
    data.append(value)

print(data)


# 12) Fruits სია, მეორე ინდექსზე დამატება
fruits = ["apple", "banana", "orange", "grape"]

new_fruit = input("Enter new fruit: ")
fruits.insert(2, new_fruit)

print(fruits)