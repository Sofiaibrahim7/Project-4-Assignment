📊 Count Even Numbers — Python Program
🧠 Problem Statement
Create a Python program that:

Asks the user to input integers, one at a time.

The user should press enter without typing a number to stop the input.

After the user stops, the program will print how many even numbers were entered.

🧪 Solution
Functions:
count_even(lst):

This function receives a list of integers and counts how many of them are even.

It iterates through the list, checking if each number is divisible by 2 (num % 2 == 0).

It prints the count of even numbers.

get_list_of_ints():

This function prompts the user for integers, adding them to a list until the user presses enter without entering a number.

It returns the list of integers.

main():

This function calls get_list_of_ints() to get the list of integers and then passes that list to count_even() to count the even numbers.

💻 Python Code
python
Copy
Edit
def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    print(count)  # Print out how many even numbers we counted above

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
    while user_input != "":  # While the user doesn't enter nothing...
        lst.append(int(user_input))  # Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

# This line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
🧪 Example Run:
vbnet
Copy
Edit
Enter an integer or press enter to stop: 2
Enter an integer or press enter to stop: 3
Enter an integer or press enter to stop: 4
Enter an integer or press enter to stop: 
2
📌 Notes
The function count_even(lst) counts and prints the number of even numbers in the provided list lst.

The function get_list_of_ints() collects integer inputs from the user until they press enter without typing anything.

