#TIP CALCULATOR

print("Welcome to the tip calculator.")

tot = float(input("What was the total bill? $"))
perc = int(input(f"What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

sum = tot * perc / 100
sum += tot
sum /= people
sum = "{:.2f}".format(sum)

#Pay attention:
#when the last digit is zero, e.g. 33.60, 
# sum = round(sum,2) 
# will display 33.6 and not 33.60 :(

print(f"Each person should pay: ${sum}")