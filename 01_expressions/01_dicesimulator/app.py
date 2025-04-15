

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)  # First die roll
    die2 = random.randint(1, NUM_SIDES)  # Second die roll
    total = die1 + die2  # Total sum of dice
    print(f"Rolled: {die1} and {die2} - Total: {total}")

def main():
    die1 = 10  # Local variable in main()
    print("die1 in main() starts as:", die1)  # Showing the value of die1 in main()
    
    # Call roll_dice three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("die1 in main() is still:", die1)  # Showing that die1 in main() remains unchanged

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
