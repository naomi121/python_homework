import traceback

# Task 1
try:
    with open("diary.txt", "a") as file:
        line = input("What happened today? ")
        while line != "done for now":
            file.write(line + "\n")
            line = input("What else? ")
        file.write("done for now\n")

except Exception as e:
    print(f"An exception occurred. Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")