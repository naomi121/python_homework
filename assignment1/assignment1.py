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



#Task 6: Use a For loop with a Range

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result



#Task 7: Student Scores, using **Kwargs

def student_scores(metric, **kwargs):
    if not kwargs:
        return None
        
    if metric == "best":
        best_student = None
        highest_score = -1
        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
        return best_student
        
    elif metric == "mean":
        total_score = sum(kwargs.values())
        return total_score / len(kwargs)


#Task 8: Titleize, wuth string and list operations

def titleize(string):
    words = string.split()
    if not words:
        return ""
        
    lowercase_exceptions = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result_words = []
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result_words.append(word.capitalize())
        elif word.lower() in lowercase_exceptions:
            result_words.append(word.lower())
        else:
            result_words.append(word.capitalize())
            
    return " ".join(result_words)



#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    words = text.split()
    vowels = "aeiou"
    result_words = []
    
    for word in words:
        if word[0] in vowels:
            result_words.append(word + "ay")
        else:
            consonants = ""
            for letter in word:
                if letter not in vowels:
                    consonants += letter
                else:
                    break
            
            remaining_word = word[len(consonants):]
            if remaining_word.startswith("qu"):
                consonants += "qu"
                remaining_word = remaining_word[2:]
                
            result_words.append(remaining_word + consonants + "ay")
            
    return " ".join(result_words)