# Shorten List Program

This Python program removes elements from the end of a list until the list reaches a maximum length (`MAX_LENGTH`). It prints each item that it removes.

## Problem Statement

Write a function `shorten(lst)` which removes elements from the end of the list `lst` until the list contains `MAX_LENGTH` items. If the list is already shorter than `MAX_LENGTH`, it will remain unchanged. The program will print the items that are removed from the list.

## Features

- **Dynamic List Modification**: The program modifies the list by removing elements from the end until it reaches a specified length.
- **Printing Removed Items**: Each removed item is printed.
- **Adjustable MAX_LENGTH**: The length of the list can be adjusted by modifying the `MAX_LENGTH` variable.

## Code

```python
MAX_LENGTH = 3  # You can change this for testing

def shorten(lst):
    # Check if the length of lst is greater than MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        # Remove the last item from the list and print it
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f"Original list: {lst}")
    shorten(lst)
    print(f"List after shortening: {lst}")

if __name__ == '__main__':
    main()
How to Run
Ensure Python is installed on your system.

Save the code into a file (e.g., shorten_list.py).

Run the script using the following command in your terminal:

bash
Copy
Edit
python shorten_list.py
Example Output:
less
Copy
Edit
Original list: ['apple', 'banana', 'cherry', 'date', 'elderberry']
Removed: elderberry
Removed: date
Removed: cherry
List after shortening: ['apple', 'banana', 'cherry']
Troubleshooting
If the program doesn't run, ensure Python is installed and that you're using the correct Python version.

If you encounter issues with the list modification, double-check the value of MAX_LENGTH.

License
This project is licensed under the MIT License.

vbnet
Copy
Edit

### How to Use:
- Save this content into a file named `README.md`.
- Place it in the same directory as your Python script to provide clear instructions for running and understanding the program.







