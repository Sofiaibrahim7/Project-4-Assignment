# Rollercoaster Height Check Program

## Problem Statement

Write a program that asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks, rollercoasters frequently have minimum height requirements for safety reasons. For this assignment, the minimum height is set to 50 units (you can assume this is in centimeters or inches, based on preference).

### Sample Runs:
1. **User Input:** `100`
    ```
    You're tall enough to ride!
    ```

2. **User Input:** `10`
    ```
    You're not tall enough to ride, but maybe next year!
    ```

### Code

```python
def main():
    MINIMUM_HEIGHT = 50  # Minimum height required for the ride

    while True:
        try:
            height = input("How tall are you? ")

            if height == "":  # Check if the user presses Enter without input
                print("Goodbye!")
                break

            height = float(height)  # Convert the input to a float

            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# Call the main function to run the program
if __name__ == '__main__':
    main()

Explanation of Code
MINIMUM_HEIGHT: This variable defines the minimum height required to go on the rollercoaster. It is set to 50 units in this case.

Input Loop: The program repeatedly asks the user for their height and checks if it's greater than or equal to 50.

Exit Condition: The program stops when the user presses Enter without typing anything.

Error Handling: If the user enters a non-numeric value, the program will prompt them to enter a valid number.

Sample Output
bash
Copy
Edit
How tall are you? 100
You're tall enough to ride!
How tall are you? 10
You're not tall enough to ride, but maybe next year!
How tall are you? 
Goodbye!
Conclusion
This program helps to determine whether a person meets the minimum height requirement for a rollercoaster ride. It also demonstrates input validation and repetitive user interaction.