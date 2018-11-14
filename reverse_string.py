# reverse a string

print("Please enter your favorite string!")

reversal = input()

reversal_seperate = (list(reversed(reversal)))
print("".join(reversal_seperate))

print("Let's try this one more way. Please enter the same string!")

reversal = input()

reversal_seperate = ("".join(reversed(reversal)))
print(reversal_seperate)

print("Ok, let's try it with a loop. Please enter the same string!")

# no understanding of this one yet
str = input()
for i in str:
	str = i + str
	print(str)	
