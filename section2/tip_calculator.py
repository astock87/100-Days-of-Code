#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give? 18, 20 or 22? ")
split = input("How many people to split the bill? ")
tip_percent = int(tip) / 100 + 1
each = round((float(total) / int(split)) * float(tip_percent), 2)
each = "{:.2f}".format(each)
print(f"Each person should pay: ${each}")
