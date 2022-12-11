secret_word = "dick"
guess = ""
guess_count = 5

while guess != secret_word and guess_count > 0:
	guess = input("Guess the word\n")
	guess_count -= 1
	if guess == secret_word:
		print("Correct, you won!")
	elif guess_count == 0:
		print(f"You're wrong and out of guesses! Go fuck yourself or something.")
	else:
		print(f"You're wrong, try again! You have {guess_count} tries left")

# might add working with files and more interactivity?
