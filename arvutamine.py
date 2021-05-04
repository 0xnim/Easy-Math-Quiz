import random

score = (0)

def quizQuestion():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = int(input("How much is " + str(num1) + " + " + str(num2) + " ? "))

    if answer == num1+num2:
         score = (score+1)

         print("Correct!")
         print("Score:", score)

    else:

        print("Wrong! The correct answer was " + str(num1+num2))


quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
quizQuestion()
