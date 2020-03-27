class Place:
	def __init__(self, name, coords):
		self.name = name
		self.coords = coords
		self.days = []

	def getDay(self, date):
		for day in self.days:
			if day.date == date:
				return day
		return None

	def avgCases(self):
		total = 0
		for d in self.days:
			total += d.data
		return total / len(self.days)

	def timeToDouble(self):
		start = self.days[-1].data
		i = 1
		ttd = 0
		try:
			while self.days[-1*(i+1)].data > start/2:
				i += 1
		except IndexError:
			i = -1
		return i

	def rateOverNDays(self, n):
		try:
			return (self.days[-1].data-self.days[-n-1].data)/self.days[-n-1].data
		except ZeroDivisionError:
			return 0

	def newCases(self):
		return self.days[-1].data - self.days[-2].data


class Country(Place):
	def __init__(self, name, coords):
		Place.__init__(self, name, coords)
		self.states = []

	def getState(self, name):
		for s in self.states:
			if s.name == name:
				return s
		return None


class State(Place):
	def __init__(self, name, coords):
		Place.__init__(self, name, coords)
		