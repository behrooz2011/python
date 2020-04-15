import csv
with open("software111.csv") as File:
	f=csv.reader(File)
	for index,row in enumerate(f):
		if index % 2==0:
			print(row)
		