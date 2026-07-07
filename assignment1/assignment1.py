# Write your code here.


#Task 1: Hello

def hello():
    return "Hello!"




#Task 2:

def name():
    return 'Hello, Name!'



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

