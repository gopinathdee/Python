import datetime

name = input("Enter your name:")
age = int(input("Enter your age:"))
print("Hello", name)
years = int(100 - age)
now = datetime.date.today()
year = now.year
after100 = int(years+year)
print("You will be 100 years old on:", after100)
