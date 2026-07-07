# Write your code here.


#Task 1: Hello

def hello():
    return "Hello!"




#Task 2:

def greet(name):
    return f'Hello, {name}!'


#Task 3: Calculator 

def calc(val1, val2, operation="multiply"):
    try:
        match operation:
            case "add":
                return val1 + val2
            case "subtract":
                return val1 - val2
            case "multiply":
                return val1 * val2
            case "divide":
                return val1 / val2
            case "modulo":
                return val1 % val2
            case "int_divide":
                return val1 // val2
            case "power":
                return val1 ** val2
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


#Task 4: Data Type Conversion

def data_type_conversion(value, type_requested):
    try:
        match type_requested:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return "Unknown type requested"
    except ValueError:
        return f"You can't convert {value} into a {type_requested}."
    


    #Task 5: Grade

    def grade(*args):
        try:
            average = sum(args) / len(args)
            
            if average >= 90:
                return "A"
            elif average >= 80:
                return "B"
            elif average >= 70:
                return "C"
            elif average >= 60:
                return "D"
            else:
                return "F"
                
        except Exception:
         return "Invalid data was provided."
