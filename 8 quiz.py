print("Welcome to my little game! Do you wanna play? Enter yes or no.\n")
wannaplay = input().lower()

if wannaplay != "yes":
	exit()

print("Ok then! I ask questions, you answer them\n")
# num_of_questions = input("Enter the number of questions you'd like to answer")

points = 0

q1 = input("In The Matrix, does Neo take the blue pill or the red pill?\n").lower()
if q1 in ("red", "red pill"):
	print("Correct! You gained a point.\n")
	points += 1
else:
	print("Wrong! You gain nothing.\n")

q1 = input("Who is the director of The Lord of the Rings and The Hobbit trilogies?\n").lower()
if q1 == "peter jackson":
	print("Correct! You gained another point.\n")
	points += 1
else:
	print("Wrong! You gain nothing again.\n")

q1 = input("Who was spider-man's archnemesis in the first Sam Raimi's spider-man movie?\n").lower()
if q1 in ("goblin", "green goblin", "norman osborn"):
	print("Correct again! Take your point.\n")
	points += 1
else:
	print("Wrong! You gain misery.\n")

q1 = input("What movie does the line \"You're one ugly motherfucker!\" come from?\n").lower()
if q1 == "predator":
	print("Right answer! One more point for you.\n")
	points += 1
else:
	print("Wrong! You gain only eternal shame.\n")

q1 = input("What was the first Marvel Cinematic Uneverse movie?\n").lower()
if q1 == "iron man":
	print("Correct! You gained an infinity stone point.\n")
	points += 1
else:
	print("Wrong! You gain someone's kidney stone.\n")


score = points / 5

if score == 1:
	print(f"That's it for questions. Your total score is {points} points. Good job, you're a movie nerd!")
elif 0.4 <= score <= 0.8:
	print(f"That's it for questions. Your total score is {points} points. Not bad, train more, you'll be the best there ever was!")
elif score <= 0.4:
	print(f"That's it for questions. Your total score is {points} points. Pretty pathetic honestly. Go watch a movie or something.")


'''
add a table of some type
remake question into function
add high-score system
'''
