# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# x = days
# y = weeks
# z = months
# dead = 90

x = int(age) * 365
y = int(age) * 52
z = int(age) * 12

days = (90 * 365) - x
weeks = (90 * 52) - y
months = (90 * 12) - z

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
