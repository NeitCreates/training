import datetime


def birth_year_calc(name, age):
	if age == 69:
		print(f"{name} is 69, very nice!")
	elif age < 18:
		print(f"{name}, you're {age}! Return back when you're older than 18.")
	else:
		print(f"Henlo, you stjinky {name}, {age}-year old fart!")
	today = datetime.date.today()
	year = today.year
	return year - age

# add returned value?


your_name = input("Input a name, dickhead\n")
your_age = int(input("Now input your age, you inbread\n"))
your_birth_year = birth_year_calc(your_name, your_age)
print(f"{your_name}, you were born in {your_birth_year}")
