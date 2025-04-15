# Add Three Copies Program

This Python program demonstrates the difference between immutable and mutable data types. It shows how lists (mutable data types) can be modified directly within functions without needing to return anything.

## Problem Statement

In the lesson about information flow, we discussed how changes made to immutable data types, such as numbers and strings, inside a function don't persist unless they are returned. In contrast, changes to mutable data types like lists and dictionaries persist even without returning them.

This program defines a function `add_three_copies()` that takes a list and some data, and adds three copies of the data to the list.

## Features

- **Mutable Data Types**: The program works with lists, which are mutable, meaning changes made inside a function will persist.
- **User Input**: The program prompts the user to enter a message, which is then added three times to a list.
- **No Return Needed**: The function modifies the list in place, and there’s no need to return the list.

## Code

```python
def add_three_copies(my_list, data):
    # Add three copies of the data to the list
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")  # Get input message from the user
    my_list = []  # Initialize an empty list
    print("List before:", my_list)  # Print the list before adding any data
    add_three_copies(my_list, message)  # Add three copies of the message to the list
    print("List after:", my_list)  # Print the list after adding the data

if __name__ == "__main__":
    main()  # Call the main function to run the program
How to Run
Ensure you have Python installed on your system.

Copy the code into a Python file (e.g., add_three_copies.py).

Run the script by typing the following command in your terminal:

bash
Copy
Edit
python add_three_copies.py
The program will prompt you to input a message, and then it will display the list before and after adding the message three times.

Example Output
pgsql
Copy
Edit
Enter a message to copy: Hello world!
List before: []
List after: ['Hello world!', 'Hello world!', 'Hello world!']
Concept
The program demonstrates mutability in Python. Lists are mutable, so changes made to a list inside a function will persist even if the function doesn’t return the list.

Troubleshooting
If the program doesn’t run, ensure you have Python installed and that you're using the correct Python version.

License
This project is licensed under the MIT License.

vbnet
Copy
Edit

### How to use this file:
- Copy the above content into a file named `README.md` and place it in the same folder as your Python script.

This file explains your program, provides instructions on how to run it, and includes an example output for clarity.







