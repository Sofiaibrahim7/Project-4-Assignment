# Continuous Input List Program

This Python program asks the user to enter values one by one, which are added to a list. When the user presses enter without typing anything, it prints the list of entered values.

## Problem Statement

Write a program that continuously asks the user to enter values. Each value entered by the user is added to a list. When the user presses enter without typing anything, the program will print the list.

### Sample Run (user input in blue):

Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

pgsql
Copy
Edit

## Features

- **Continuous Input**: The program keeps asking for input until the user presses enter without typing anything.
- **Dynamic List**: The list grows as the user adds more values.
- **No Return**: The list is printed when the user stops entering values.

## Code

```python
def main():
    lst = []  # Create an empty list to store the values

    # Ask the user to input values
    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input is not empty
        lst.append(val)  # Add the input value to the list
        val = input("Enter a value: ")  # Get the next value to add

    # Print the list after the user stops entering values
    print("Here's the list:", lst)


if __name__ == '__main__':
    main()  # Call the main function to execute the program
How to Run
Ensure Python is installed on your system.

Save the code into a file (e.g., input_list.py).

Run the script using the following command:

bash
Copy
Edit
python input_list.py
The program will prompt you to input values and will print the list when you press enter without typing anything.

Example Output
yaml
Copy
Edit
Enter a value: 1
Enter a value: 2
Enter a value: 3
Enter a value:
Here's the list: ['1', '2', '3']
Troubleshooting
If the program doesn't run, make sure Python is installed and properly set up.

Ensure you're using the correct Python version.

If you encounter issues with storing input as a string, consider converting the input to an integer with int().

License
This project is licensed under the MIT License.

vbnet
Copy
Edit

### How to Use:
- Save this content in a file named `README.md`.
- Place it in the same directory as your Python script to provide clear instructions for running and understanding the program.

Let me know if you need any adjustments or further explanations!







