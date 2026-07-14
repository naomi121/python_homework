import csv
import os
import traceback
from datetime import datetime
import custom_module

# Task 2
def read_employees():
    employee_dict_data = {}
    rows_list = []
    try:
        with open("../csv/employees.csv", mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)
            employee_dict_data["fields"] = header
            for row in reader:
                rows_list.append(row)
            employee_dict_data["rows"] = rows_list
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)
        
    return employee_dict_data

employees = read_employees()
print("Loaded Employees:", employees)

# Task 3
def column_index(column_name):
    global employee_id_column
    idx = employees["fields"].index(column_name)
    return idx

employee_id_column = column_index("employee_id")

# Task 4
def first_name(row_index):
    first_name_idx = column_index("first_name")
    return employees["rows"][row_index][first_name_idx]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    last_name_idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_idx])
    return employees["rows"]

# Task 8
def employee_dict(employee_row):
    zipped = zip(employees["fields"], employee_row)
    result = {key: val for key, val in zipped if key != "employee_id"}
    return result

# Task 9
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11
def set_that_secret(secret_val):
    custom_module.set_secret(secret_val)

# Task 12
def _read_minutes_helper(filepath):
    data_dict = {}
    rows_list = []
    with open(filepath, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data_dict["fields"] = header
        for row in reader:
            rows_list.append(tuple(row))
    return data_dict

def read_minutes():
    global minutes1, minutes2
    minutes1 = _read_minutes_helper("../csv/minutes1.csv")
    minutes2 = _read_minutes_helper("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

# Task 13
def create_minutes_set():
    global minutes_set
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    minutes_set = set1.union(set2)
    return minutes_set

# Task 14
def create_minutes_list():
    global minutes_list
    temp_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), temp_list))
    return minutes_list

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    formatted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    
    with open("./minutes.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(formatted_list)
        
    return formatted_list