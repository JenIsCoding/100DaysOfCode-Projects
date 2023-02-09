# Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 =  name1.lower()
name2 =  name2.lower()

name = name1 + name2

tot1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
#print(tot1)
tot2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")
#print(tot2)

tot = str(tot1) + str(tot2)
tot = int(tot)

if tot < 10 or tot > 90:
    print(f"Your score is {tot}, you go together like coke and mentos.") 
elif tot > 40 and tot < 50:
    print(f"Your score is {tot}, you are alright together.")
else:
    print(f"Your score is {tot}.")
