import random


def getRandint(min, max):
    """
    Generate random integer in given range.

    Args:
    min (int): start of the range(included).
    max (int): end of the range(included).
    
    Returns:
    int: a random integer.
    
    """
    return random.randint(min, max)


def getRandoperation():
    """
    Choose a random operation from given choice array.

    Args:
    none
    
    Returns:
    string: a random operation.
    
    """
    return random.choice(['+', '-', '*'])

def function_C(num1, num2, operation):
    
    """
    Performs a basic arithmetic operation between two numbers.

    Args:
        num1 (int): The first number in the operation.
        num2 (int): The second number in the operation.
        operation (str): The arithmetic operation to perform. 
                         It should be one of the following:
                         '+' for addition, '-' for subtraction, '*' for multiplication.

    Returns:
        tuple: A tuple containing:
            - str: A string representing the problem (e.g., "3 + 4").
            - int: The result of the operation.

    """
    
    problem = f"{num1} {operation} {num2}"
    if operation == '+': answer = num1 + num2
    elif operation == '-': answer = num1 - num2
    else: answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0 #set inital score 0
    rounds = 3 # defining number of rounds of game

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(rounds):
        n1 = getRandint(1, 10); n2 = getRandint(1, 10); operation = getRandoperation()

        PROBLEM, ANSWER = function_C(n1, n2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        
        # try-except block for validating user input
        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid input, you lose a point \nbe careful next time!")
        
        
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1 #incrementing score on each correct answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{rounds}")

if __name__ == "__main__":
    math_quiz()
