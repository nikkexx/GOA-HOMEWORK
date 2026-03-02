print(True and True)#True
print(True and False)#False
print(False and True)#False
print(False and False)#False

print(True or True)#True
print(True or False)#True
print(False or True)#True
print(False or False) #False

True and False or False or True and True and False or True
True and False #False
True and True #True
True and True and False #False

False or False or False or True #საბოლოო პასუხი True

family_members = 4
people_in_house = int(input("შეიყვანე სახლში მყოფი ადამიანების რაოდენობა"))
thief_detected = people_in_house > family_members
print("არის სხვა ვინმე სახლში:", thief_detected) 

