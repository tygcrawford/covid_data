import csv

from place import Place, Country, State
from day import Day


class CovidData:
	def __init__(self, path):
		self.countries = []
		self.path = path
		self.readfile()

	def getCountry(self, name):
		for c in self.countries:
			if c.name == name:
				return c
		return None

	def getDict(self):
		dct = {}
		dct['countries'] = {}
		for c in self.countries:
			dct['countries'][c.name] = {}
			dct['countries'][c.name]['lat'] = c.coords[0]
			dct['countries'][c.name]['lng'] = c.coords[1]
			dct['countries'][c.name]['days'] = []
			for d in c.days:
				dct['countries'][c.name]['days'].append({})
				dct['countries'][c.name]['days'][-1]['date'] = str(d.date)
				dct['countries'][c.name]['days'][-1]['cases'] = d.data

		return dct

	def readfile(self):
		with open(self.path, "r") as f:
			reader = csv.reader(f, delimiter=',', quotechar='"')
			key = reader.__next__()
			for row in reader:
				if self.getCountry(row[1]) != None:
					country = self.getCountry(row[1])
				else:
					country = Country(row[1], (float(row[2]),float(row[3])))
					self.countries.append(country)
				if(row[0] != ""):
					state = State(row[0], (float(row[2]),float(row[3])))
					country.states.append(state)
				else:
					country.coords = (float(row[2]),float(row[3]))
				end = False
				col = 4
				while(not end):
					try:
						day = Day(key[col],int(row[col]))
						if(row[0] != ""):
							state.days.append(day)
						test = country.getDay(day.date)
						if test == None:
							country.days.append(Day(key[col],int(row[col])))
						else:
							test.add(int(row[col]))
					except IndexError:
						end = True
					col += 1
