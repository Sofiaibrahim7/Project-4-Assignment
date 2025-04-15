First 20 Even Numbers Program
This Python program prints the first 20 even numbers using a loop. It starts from 0 and prints every second number (i.e., even numbers) up to the 20th one.

Problem Statement
Write a program that prints the first 20 even numbers. Do not write 20 print statements — use a loop to generate the values.

Note: The first even number is 0.

Sample Output
Copy
Edit
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
Features
Efficient Looping: Uses a loop to generate even numbers without hardcoding each one.

Clean Output: All numbers are printed on the same line, separated by spaces.

Scalable: Can easily be adjusted to print more or fewer even numbers.

Code
python
Copy
Edit
def main():
    count = 0  # Counter to keep track of how many even numbers we've printed
    num = 0    # Starting number

    while count < 20:
        print(num, end=' ')
        num += 2       # Move to the next even number
        count += 1     # Increment the counter

if __name__ == '__main__':
    main()
How to Run
Make sure Python is installed on your system.

Save the code into a file named even_numbers.py.

Run the script using the terminal or command prompt:

bash
Copy
Edit
python even_numbers.py
Troubleshooting
If the program doesn’t run, ensure that Python is correctly installed.

Make sure you're using the correct command to run the file.

License
This project is licensed under the MIT License.











