import datetime


class one_ugly_motherfucker:
	def __init__(self, name, spicies, age, sex, hostility, horny):
		self.name = name
		self.spicies = spicies
		self.sex = sex
		self.age = age
		self.hostility = hostility
		self.horny = horny

	def get_hostility(self):
		return self.hostility

	def get_age_of_birth(self):
		today = datetime.date.today().year
		birth_year = today - self.age
		print(f"{self.name}, the {self.spicies}, was born in {birth_year}")
		if 1900 < birth_year < 1999:
			return "XX century"
		elif 1800 < birth_year < 1899:
			return "XIX century"
		elif 1700 < birth_year < 1799:
			return "XVIII century"
		elif 1400 < birth_year < 1699:
			return "middle ages"
		elif birth_year < 1399:
			return "fucking ancient"


class director:
	def __init__(self, name, genres):  # how to pass an array to class object?
		self.name = name
		self.genres = genres
		# self.has_oscar = False


class movie:
	def __init__(self, title, director, max_mfers):
		self.title = title
		self.director = director
		self.max_mfers = max_mfers
		self.movie_mfers = []
		self.movie_type = None
		print(f"You've created a movie {title}, directed by {director}")

	def invite_motherfucker(self, mfer):
		if len(self.movie_mfers) < self.max_mfers:
			self.movie_mfers.append(mfer)


	def get_movie_type(self):



mfer1_predator = one_ugly_motherfucker("Alex", "Predator", 200, "male", True, False)
mfer2_Arnie = one_ugly_motherfucker("Arnold", "Human", 75, "male", False, False)
mfer3_alien = 
mfer4_? = 
mfer5_bondgirl = 
mfer6_arthur =
print(f"{mfer1.name}, the {mfer1.spicies}, came to Earth to copulate with our women")
print(f"{mfer2.name}, the {mfer2.spicies}, is here to protect. He's {mfer2.age} years old though...")
print(mfer1.get_age_of_birth())

'''
do somethinh with that class, like manual unput, then sorting the ones that are 'hostile', write into file maybe
determine max heroes, has to be at least one monster and hero
add check for type - how many heroes, types, sex, time - compound one
list of another class? add heroes to list, print info
evolve program into smth with db or http requests
some directors would not direct certaim genres - add directoe class, message chose another director from the list - print appropriate list
add movie year?
roger corman would take anything - create one style to forcibly change to him
create mfers reading info from a document
check for input data type

add horny to class
genre cases(horny, hero-monster, age):
hero+monster (+lady)

1st - monster or not
2nd - time
2rd - horny or not, if horny then sex decides the type
'''

# I'm adding some comments to test git branching.