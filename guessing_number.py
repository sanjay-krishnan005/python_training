def game():
    import random
    guessing_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 3
    print("welcome to the guessing number game")
    print("try to guess the number 1 to 20")
    while attempts < max_attempts:
        guess = int(input("Enter the number: "))
        attempts += 1
        if guessing_number == guess:
            print("You won the game!")
            break
        elif guessing_number > guess:
            print("Too low, try a higher number")
        else:
            print("Too high, try a smaller number")
        if attempts == max_attempts:
            print("You lost the game! The number was",guessing_number)

