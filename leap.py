# Given a year, report if it is a leap year

print("What year is it?")

year = int(input())

if year %  4 == 0 and year % 100 != 0 and year % 400 != 0:
	print(f"{year} is a leap year")
else:
	print(f"{year} is not a leap year")

# Whoo Hoo I did one from scratch!!!
