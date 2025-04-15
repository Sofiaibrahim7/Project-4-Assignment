🔁 Message Repeater — Python Program
🧠 Problem Statement
Write a function print_multiple(message, repeats) that takes a string message and an integer repeats as input and prints the message a specified number of times, as defined by the repeats parameter.

🧪 Solution
Function:
print_multiple(message, repeats):

This function takes two parameters:

message: A string to be printed.

repeats: An integer specifying how many times the message should be printed.

The function uses a for loop to print the message the specified number of times.

main():

The main() function prompts the user to input a message and a number of repeats.

Then, it calls the print_multiple(message, repeats) function to print the message the required number of times.

💻 Python Code
python

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
🧪 Example Run:

Please type a message: Hello!
Enter a number of times to repeat your message: 6
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
📌 Key Concepts
Looping: The program uses a for loop to repeat the printing of the message a specified number of times.

User Input: The program uses input() to capture the message and the number of repeats from the user.

