📝 .md FILE (Markdown Description):

# ✨ Affirmation Typing Program

## 📘 Problem Statement

Write a Python program that prompts the user to type an affirmation **exactly as written** until they get it right.

This program helps remind users of their strength and resilience by repeating an encouraging message.

### 🔤 Affirmation Text:
I am capable of doing anything I put my mind to.

## 🧪 Sample Run

Please type the following affirmation: I am capable of doing anything I put my mind to.

That was not the affirmation.
Please type the following affirmation: I am capable of doing anything I put my mind to.
I am capable of doing anything I put my mind to.
That's right! :)
✅ Python Code
Copy and paste this into a .py file and run it:

AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)"

# Required to call main
if __name__ == '__main__':
    main()
