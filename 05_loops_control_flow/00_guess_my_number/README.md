# 🎮 Guess My Number Game

## 📝 Problem Statement

I am thinking of a number between 1 and 99...

You have to guess the number! After each guess, the program will tell you whether your guess is **too high** or **too low** until you find the correct number.

---

## ✅ Sample Game Play

I am thinking of a number between 1 and 99... Enter a guess: 50 Your guess is too high

Enter a new guess: 25 Your guess is too low

Enter a new guess: 40 Your guess is too low

Enter a new guess: 45 Your guess is too low

Enter a new guess: 48 Congrats! The number was: 48
---

## 🧠 Logic

- The program generates a **random number** between 1 and 99.
- It asks the user to guess the number.
- Based on the guess, it gives hints:
  - If guess < secret number → "too low"
  - If guess > secret number → "too high"
- The loop continues until the guess matches the secret number.

---

## 🧾 Python Code

```python
import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Print an empty line for spacing
        guess = int(input("Enter a new guess: "))
    
    print("Congrats! The number was: " + str(secret_number))

# Required line to run the main function
if __name__ == '__main__':
    main()
