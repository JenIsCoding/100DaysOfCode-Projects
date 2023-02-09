#Pizza order practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")



tot = 0

if size == "S":
    tot = 15
    if add_pepperoni == "Y":
        tot += 2 
elif size == "M":
    tot = 20
    if add_pepperoni == "Y":
        tot += 3 
else: 
    tot = 25
    if add_pepperoni == "Y":
        tot += 3

if extra_cheese == "Y":
        tot += 1 

print(f"Your final bill is: ${tot}.")