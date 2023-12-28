# #looping concept

# if else condition 

# ageInput = int(input("Enter your age : "))

# if ageInput>=20:
#     print("User is 18+ or above")
# else:
#     print("User is not adult")


#Elif statement

# scoreInput = int(input("Enter your score : "))

# if scoreInput>=90:
#     print("your grade is A")
# elif scoreInput>=70:
#     print("your grade is B")
# elif scoreInput>=50:
#     print("your grade is C")
# else:
#     print("No grade achived")



#Nested if else statement

userInput_1 = int(input("Enter the first value  : "))
userInput_2 = int(input("Enter the second value : "))

if userInput_1>userInput_2:
    print("userInput_1 is greater than userInput_2")
    if userInput_1>100:
        print("userInput_1 is greater than 100")
    else: 
        print("userInput_1 is lesser than 100")
else:
    print("userInput_2 is greater than userInput_1")


