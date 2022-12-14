import random


def check_input(input_prompt):
	'''Function to input a value and check if it's int and > 0'''

	global stpd_counter
	while True:
		try:
			value = int(input(input_prompt))
		except ValueError:
			print("Input a number, not words, you asshole!")
			stpd_counter += 1
			continue
		if value < 0:
			print("The value should be > 0! Input a correct one!")
			continue
		else:
			break
	return value


stpd_counter = 0

print("Input the interval you want the number to be in")

min_number = check_input("Input min number: ")
while True:
	max_number = check_input("Input max number: ")
	if min_number > max_number:
		print("Your min number cannot be greater than your max. Did you even attend school, idiot?")
		stpd_counter += 3
		continue
	else:
		break

secret_numb = random.randint(min_number, max_number)
print(f"secret number is {secret_numb}. shhhhh!")

while True:
	guess_num = check_input("Input your guess: ")
	if not min_number <= guess_num <= max_number:
		print("Are you retarded or what? You've just specified the range and now you're guessing out of it?!")
		stpd_counter += 3
		continue
	elif guess_num != secret_numb:
		if guess_num < secret_numb:
			print("Not quite, go higher!")
		elif guess_num > secret_numb:
			print("Not quite, go lower!")
		continue
	elif guess_num == secret_numb:
		if stpd_counter <= 4:
			print(f"Great, you got it, the number is {secret_numb}")
			break
		elif 5 <= stpd_counter <= 10:
			print(f"You did it, the number is {secret_numb}. However you're rather dumb and fucked up a lot.")
			break
		elif stpd_counter > 10:
			print(f"The number is {secret_numb} and it's sheer luck you got it. I've never seen such a stupid and useless humanbeing. I advise you to go and die right away.")
			break


'''
different functions for input checks
'''
