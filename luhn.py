# Given a number, determine whether or not it is valid per Luhn formula
# Need at least two numbers, doubles every other digit from the right
# adds the two numbers of the double together to make new single digit
import numpy as np
print("Please enter a valid  16 digit CC#")
array = input()
counter = 0
max = 4
while array.isdigit() is False:
	print("Please enter valid numbers")	
	array = input()
	counter += 1
	if counter == max:
		print("You aren't cooperating, Goodbye...")
		break
while len(array) < 15:
	print("Please enter a valid 16 digit CC#")
	array = input()
	counter += 1
	if counter == max:
		print("You aren't cooperating, Goodbye...")
		break
while len(array) > 16:	
	print("That's too many numbers, please enter a valid  16 digit CC#")
	array = input()
	counter += 1
	if counter == max:
		print("You aren't cooperating, Goodbye...")
		break
# Give you 5 tries, then terminates the program
# Reverse array combined with turning strings to integers
array_rev = list(map(int, array[::-1]))
# print(array_rev)
# checks for AMEX 15 digit
if len(array_rev) == 15:
	array_plucky = array_rev[1::2]
else:
# Takes every other for 16 digit 
	array_plucky = array_rev[::2]
# checks for AMEX 15 digit
if len(array_rev) == 15:
	array_pluck = array_rev[::2]
else:
# Takes first and every other for 16 digit
	array_pluck = array_rev[1::2]
# print(array_pluck)

# multiply removed numbers by 2
pluck_new = [2 * x for x in array_pluck]
# print(pluck_new)

# turn the double into single digits
pluck_minus = pluck_new.copy()
for i, v in enumerate(pluck_new):
	if v >= 10:
		pluck_minus[i] = v - 9
# WORKS but not necessary pluck_minus = [x - 9 for x in pluck_new]
# print(pluck_minus)

# interlace two arrays, zip() puts into tuples, then hstack joins them
pluck_joined = np.hstack(zip(array_plucky,pluck_minus))
#print(pluck_joined)
pj_rev = pluck_joined[::-1]
# print(pj_rev)

# find the sum of pluck_joined 
sum = sum(pluck_joined)
# print(sum)

# check digit is sum * 9 mod 10
check_digit = (sum) % 10
# print(check_digit)

if check_digit == 0:
	print("Your CC# is valid, please spend your savings.")
else:
	print("That isn't a real CC#, we need cash from you.")


