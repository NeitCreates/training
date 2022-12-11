import requests


class APICall():
	'''A class to make a basic API call request'''

	def call(self, method, api_url):
		if method.lower() == "get":
			r = requests.get(api_url)

		match r.status_code:
			case 200 | 201 | 202:
				return r.json()["value"]
			case _:
				raise TypeError("API error")


class NorrisAPI(APICall):
	'''Chuck Norris API'''

	url = "https://api.chucknorris.io/jokes/random?category="
	categories = ["animal", "dev", "explicit"]

	def __init__(self, category):
		self.category = category
		if self.category not in self.categories:
			raise TypeError("wrong category")

	def get(self):
		api_url = f'{self.url}{self.category}'
		return self.call("get", api_url)


c = NorrisAPI("animal")
print(c.get())

# make interactive, print categorise, add randomization option
