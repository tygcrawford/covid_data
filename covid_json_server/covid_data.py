import wget, os, csv
from datetime import date as dtdate
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json

from place import Place, Country, State
from day import Day

curr_path = os.path.dirname(os.path.abspath(__file__))
filename = "data.csv"
data_path = f"{curr_path}/{filename}"

data_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"


def downloadUrl(url, path):
	os.system(f"wget -q {url} -O {data_path}")

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
			dct['countries'][c.name]['lat'] = str(c.coords[0])
			dct['countries'][c.name]['lng'] = str(c.coords[1])
			dct['countries'][c.name]['days'] = {}
			for d in c.days:
				dct['countries'][c.name]['days'][str(d.date)] = {}
				dct['countries'][c.name]['days'][str(d.date)]['cases'] = d.data

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


def main():

	## ask for update
	# while True:
	# 	ans = input("Do you want to update the data? (y/n)\n>>> ")
	# 	if ans == "y":
	# 		try:
	# 			downloadUrl(data_url, data_path)
	# 			print("Data updated.")
	# 		except Exception as e:
	# 			print("Error updating.")
	# 		break
	# 	elif ans == "n":
	# 		break
	# 	else:
	# 		print(f"\n{ans}\n is not an answer")
	d = CovidData(data_path)

	print(d.getDict())
	
	#### use examples

	## Case History Search
	# exited = False
	# while True:
	# 	print("Type Country Name for Case History")
	# 	print("Type \"exit\" to quit searching")
	# 	search = input(">>> ")
	# 	c = d.getCountry(search)
	# 	if search == "exit":
	# 		break
	# 	if c == None:
	# 		print(f"\"{search}\" is not a country or does not have cases.")
	# 	else:
	# 		print(f"{c.name} Cases")
	# 		for day in c.days:
	# 			print(f"{str(day.date)} => {day.data}")
	# 	print("-"*20)
	# print("-"*20)

	## summary of country cases
	# print("Country Summary")
	# for c in d.countries:
	# 	if c.days[-1].data > 100:
	# 		print(f"{c.name[0:17]:<17} | {c.days[-1].data:<6} | {c.rateOverNDays(1)*100:>8.2f}% | {c.newCases():<5}")
	
	## graph time to double of country
	# mapimg = plt.imread(f"{curr_path}/map.png")
	# fig, ax = plt.subplots(figsize = (8,7))
	# BBox = ((-180, 180, -150, 150))
	# data = [[c.coords[1] for c in d.countries],
	# 		[c.coords[0] for c in d.countries]]
	# size = [c.newCases()/5 for c in d.countries]
	# ax.scatter(data[0], data[1], zorder=1, alpha= 0.35, c='r', s=size)
	# data = [c.timeToDouble() for c in d.countries]
	# for i in range(len(data)):
	# 	ax.text(d.countries[i].coords[1], d.countries[i].coords[0], str(data[i]), ha='center', va='center', color='black')
	# ax.set_title('COVID-19 Active Cases')
	# ax.set_xlim(BBox[0],BBox[1])
	# ax.set_ylim(BBox[2],BBox[3])
	# ax.imshow(mapimg, zorder=0, extent=BBox, aspect='equal')
	# plt.show()



if __name__ == "__main__":
	main()