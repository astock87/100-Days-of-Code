# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#todo: how much based on size selection: Small Pizza: $15, Medium Pizza: $20, Large Pizza: $25

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("You typed the wrong input")

#todo: how much to add if they want pepperoni: #Pepperoni for Small Pizza: +$2, Pepperoni for Medium or Large Pizza: +$3

if add_pepperoni == "Y":
    if size == "S":
       bill += 2
    else:
       bill += 3

#todo: how much to add if they want extra cheese: #Extra cheese for any size pizza: + $1

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

