from art import logo

def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def subtract(n1, n2):
    return n1 - n2

#can add method calls to a dictionary
functions = {
    "+":add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def continue_game(result):
    response = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if response == "n":
        return False
    else:
        return True

def run_math(first):
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    next = float(input("What's the next number?: "))
    result = functions[operation](first, next)
    print(f"{first} {operation} {next} = {result}")
    return result

#can practice recursion also by calling calculator function within itself
while(True):
    print(logo)
    first = float(input("What's the first number?: "))
    play_game = True
    while(play_game):
        result = run_math(first)
        play_game = continue_game(result)
        first = result
    print("\n"*20)

