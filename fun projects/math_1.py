import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 3

def getProblem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


input("Press Enter to start the quiz")
print("------------------------------")


start_time = time.time()

wrong = 0

for i in range(TOTAL_PROBLEMS):
    expr, answer = getProblem()
    while True:
        guess = input("Problem #" + str(i + 1) + ":   " + expr + " = ")
        if guess == str(answer):
            print("Correct!")
            break
        elif guess != str(answer):
            print("WRONG!")
            wrong += 1
            break


end_time = time.time()
total_time = round(end_time - start_time, 2)

print("------------------------------")
print("Quiz completed in",total_time, "seconds and out of,", TOTAL_PROBLEMS, "questions", wrong, "mistake(s) were made!")

#I want to have a time limit.
#I want to count the number of correct answers.
# If there is a wrong answer, I want a new problem to be generated.



