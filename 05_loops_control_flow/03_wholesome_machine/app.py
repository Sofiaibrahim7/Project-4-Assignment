AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

# Required to call main
if __name__ == '__main__':
    main()