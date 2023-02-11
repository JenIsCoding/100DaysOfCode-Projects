# PyPassword Generator

import random

####################letters, numbers and symbols
lowCase =  [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
uppCase =  [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
letters = lowCase + uppCase

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['/','=','?','^',')','(','*','$','£','%','&',':',',',';','_','-','>','<']
####################

print("Welcome to the PyPassword Generator!")

len_lett = len(letters)
len_symb = len(symbols)
len_numb = len(numbers)

num_tot_lett = int(input("How many letters would you like in your password? "))
num_symb = int(input("How many symbols would you like? "))
num_numb = int(input("How many numbers would you like? "))

# choose random symbols
for symb in symbols:
    rand_symb = random.sample(symbols,num_symb)
# print(rand_symb)

# remove the choosen symbols
for symb in rand_symb:
    symbols.remove(symb)
# print(symbols)

# choose random numbers
for num in numbers:
    rand_numb = random.sample(numbers, num_numb)
# print(rand_numb)

# remove the choosen numbers
for num in rand_numb:
    numbers.remove(num)
# print(numbers)

left_choices = num_tot_lett - num_symb - num_numb
# print(left_choices)

for let in letters:
    rand_choices = random.sample(letters, left_choices)
# print(rand_choices)

selection = rand_choices + rand_numb + rand_symb

for item in selection: #instead of use random, we can use shuffle() to mix up the characters
    passw = random.sample(selection, num_tot_lett)
    passw= ''.join(passw)

print(f"Here is your {len(passw)} letter password: {passw}")