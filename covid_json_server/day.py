from datetime import date as dtdate

class Day:
	def __init__(self, date, data):
		date = date.split('/')
		self.date = dtdate(int("20" + date[2]), int(date[0]), int(date[1]))
		self.data = data

	def add(self, num):
		self.data += num