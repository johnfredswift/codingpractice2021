print("Hello World")
numberRange = 100
high = numberRange
low = 0
guessNumber = int(numberRange/2)
guesses = 0
correctGuess = False


while correctGuess == False:
    print(f'Is your number {guessNumber}?')
    reply = input("Is youre number higher or lower or correct(h/l/c)")
    if reply == "h":
        print("My guess was too high")
        low = guessNumber
    elif reply == "l":
        print("My guess was too low")
        high = guessNumber
    elif reply == "c":
        print(f"My guess was correct at: {guessNumber}")
        correctGuess = True
    else:
        print("Try typing an actual input please")

    guessNumber = int(round((low + high)/2))
    print()