🔢 Double a Number — Python Program
🧠 Problem Statement
Create a function double(num) that multiplies a given number by 2 and returns the result. The program should ask the user to input a number, then call double(num) to calculate the result and print it.

🧪 Solution
Function:
double(num):

This function takes an integer num as input.

It returns the result of num * 2, which is simply doubling the number.

main():

This function prompts the user to input a number.

It calls double(num) with the user's input and prints the doubled result.

💻 Python Code
python

def double(num: int):
    return num * 2

# There is no need to edit code beyond this point

def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()
🧪 Example Run:
kotlin

Enter a number: 2
Double that is 4
📌 Key Concepts
Multiplication: The function double(num) performs a basic multiplication to double the number.











