🔁 Doubling Until 100 — Python Program
🧠 Problem Statement
Write a Python program that:

Asks the user to enter a number.

Doubles that number and prints the result.

Continues doubling and printing until the value is 100 or greater.

📌 The current value should be stored in a variable named curr_value.

✅ Use a while loop with the condition:

python
while curr_value < 100:
🧪 Example
If the user enters:

2
The output will be
4
8
16
32
64
128
💻 Python Code

def main():
    # Ask user for a number and convert it to an integer
    curr_value = int(input("Enter a number: "))
    
    # Double the number until it is 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
📌 Notes
This program uses a while loop to repeat the doubling process.

It stops execution as soon as the value becomes 100 or more.

The variable curr_value is updated at each step using:

curr_value = curr_value * 2