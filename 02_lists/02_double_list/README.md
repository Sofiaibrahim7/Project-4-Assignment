🧮 Double Each Number in List - Python Project
This simple Python project demonstrates how to double each element in a list of numbers.

📌 Problem Statement
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

python
Copy
Edit
numbers = [1, 2, 3, 4]
You should end with this list:

python
Copy
Edit
numbers = [2, 4, 6, 8]
📝 How the Code Works
List of Numbers: The program starts with a predefined list of numbers.

Loop through the List: It loops through the list and doubles each element.

Modification: Each element is doubled in place using a for loop and index manipulation.

Output: The program then prints the modified list with the doubled values.

Example Output
plaintext
Copy
Edit
[2, 4, 6, 8]
💻 Code Explanation
python
Copy
Edit
def main():
    # List of numbers
    numbers: list[int] = [1, 2, 3, 4]

    # Loop through the list and double each number
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2  # Double the value at each index

    # Print the modified list
    print(numbers)

# Required line to run the main function
if __name__ == '__main__':
    main()
numbers list: The list of numbers is initialized with values [1, 2, 3, 4].

for loop: It iterates through each element in the list by its index and doubles each value.

Print statement: After modifying the list, it prints the final list, which now contains the doubled values.

Key Concepts Used:
List manipulation: Modifying each element of a list.

For Loop: Iterating through the list using indices.

In-place modification: Modifying the list in place without creating a new one.

🛠 How to Run the Code
Install Python: If you don't have Python installed, download and install it from Python.org.

Save the Code: Save the code into a file named double_numbers.py.

Run the Code:

Open a terminal (Command Prompt or PowerShell).

Navigate to the directory where double_numbers.py is saved.

Run the following command:

bash
Copy
Edit
python double_numbers.py
Expected Output:
plaintext
Copy
Edit
[2, 4, 6, 8]
📌 Additional Notes:
This project can be extended in various ways:

User Input: Modify the program to accept numbers from the user.

Error Handling: Add error handling for invalid inputs (e.g., non-numeric values).

Additional Operations: You can add more functionality like halving numbers, squaring them, etc.








