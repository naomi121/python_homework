import csv

with open("../csv/employees.csv", mode="r") as file:
    reader = csv.reader(file)
    raw_data = list(reader)

full_names = [f"{row[0]} {row[1]}" for row in raw_data[1:]]
print(full_names)

e_names = [name for name in full_names if "e" in name.lower()]
print(e_names)