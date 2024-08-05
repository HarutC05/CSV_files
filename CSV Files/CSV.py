# BAD!
with open("fighters.csv") as file:
	data = file.read()


# using reader
from csv import reader
with open("fighters.csv") as file:
	csv_reader = reader(file)
	next(csv_reader)
	for fighter in csv_reader:
		print(f"{fighter[0]} is from {fighter[1]}")


from csv import reader 
with open("fighters.csv") as file:
	csv_reader = list(csv_reader)
	print(data)


from csv import DictReader
with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		print(row['Name'])