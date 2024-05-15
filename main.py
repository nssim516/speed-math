import random
import time

# CONSTANTS

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

# CREATING THE PROBLEM

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) # .choice chooses a random element from a list

    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Welcome to Speed Math! Press enter to start!")
print("---------------------------------------------")

# START TIMER

startTime = time.time() # returns a time in seconds

# GENERATING PROBLEMS

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
        print("Try Again...")

# END TIMER

endTime = time.time()
totalTime = round(endTime - startTime, 2) # rounds to 2 digits after the decimal point

print("----------------------")
print("Good job! You finished in", totalTime, "seconds!")
