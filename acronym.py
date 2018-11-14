# Convert a long phrase to its acronym

print("Enter your long phrase, and I'll convert it to an acronym.")
str = input()
# str = str.split()
str_len = len(str)
output = ''
for i in str.upper().split():
	output += i[0]

print(f"Your acronym is", output)
