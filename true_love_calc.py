# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
true_sum = int(lower_name1.count("t")) + int(lower_name1.count("r")) + int(lower_name1.count("u")) + int(lower_name1.count("e")) + int(lower_name2.count("t")) + int(lower_name2.count("r")) + int(lower_name2.count("u")) + int(lower_name2.count("e"))
#print(f"Total = {true_sum}")

love_sum = int(lower_name1.count("l")) + int(lower_name1.count("o")) + int(lower_name1.count("v") )+ int(lower_name1.count("e")) + int(lower_name2.count("l")) + int(lower_name2.count("o")) + int(lower_name2.count("v")) + int(lower_name2.count("e"))

#print(f"Total = {love_sum}")

coke = "you go together like coke and mentos."
alright = "you are alright together."

love_score = str(true_sum) + str(love_sum)
love_score1 = int(love_score)
if love_score1 <= 10 or love_score1 >= 90:
  print(f"Your score is {love_score1}, {coke}")
elif love_score1 >= 40 and love_score1 <= 50:
  print(f"Your score is {love_score1}, {alright}")
else:
  print(f"Your score is {love_score1}.")
