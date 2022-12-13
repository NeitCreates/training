print("Welcome to my little game! Do you wanna play? Enter yes or no.\n")
wannaplay = input().lower()

if wannaplay != "yes":
	exit()

print("Ok then! I ask questions, you answer them\n")

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

q1 = input("What was the first Marvel Cinemati Uneverse movie?\n").lower()
if q1 == "iron man":
	print("Correct! You gained an infinity stone point.\n")
	points += 1
else:
	print("Wrong! You gain someone's kidney stone.\n")

print(f"That's it for questions. Your total score is {points} points. Good job!")


'''
add different points comment regarding the number of correct answers
add a table of some type
remake question into function
add high-score system
'''
