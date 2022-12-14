import random


def check_input(input_prompt):
	'''Function to input a value and check if it's int and > 0'''

	while True:
		try:
			value = int(input(input_prompt))
		except ValueError:
			print("Input a number, not words, you asshole!")
			continue
		if value < 0:
			print("The value should be > 0! Input a correct one!")
			continue
		else:
			break
	return value


print("Input the interval you want the number to be in")

min_number = check_input("Input min number: ")
while True:
	max_number = check_input("Input max number: ")
	if min_number > max_number:
		print("Your min number cannot be greater than your max. Did you even attend school, idiot?")
		continue
	else:
		break

secret_numb = random.randint(min_number, max_number)
print(f"secret number is {secret_numb}. shhhhh!")

while True:
	guess_num = check_input("Input your guess: ")
	if not min_number <= guess_num <= max_number:
		print("Are you retarded or what? You've just specified the range and now you're guessing out of it?!")
		continue
	elif guess_num != secret_numb:
		if guess_num < secret_numb:
			print("Not quite, go higher!")
		elif guess_num > secret_numb:
			print("Not quite, go lower!")
		continue
	elif guess_num == secret_numb:
		print(f"Great, you got it, the number is {secret_numb}")
		break

'''
add stupidity counter - diff message depending on the number of fuckups
different functions for input checks
'''
