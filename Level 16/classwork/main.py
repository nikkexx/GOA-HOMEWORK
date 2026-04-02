word = input("შეიყვანეთ სიტყვა: ")

if word == word.upper():
    print("სიყვა დიდი ასოებშია")
else:
    print("პატარა ასოებშია")


word = input("შეიყვანეთ სიტყვა: ")
letter = input("შეიყვანეთ ასო:")

latter2 = word.find(letter)
print(f"ასოს მდებარეობა ინდექსი {latter2}")

fruits = ['apple','banana','peach','pineapple'] 

fruits.append('pinaapple')
fruits.append('orange')
fruits.append('kiwi')

print("სიის სიგრძეა:", len(fruits))
