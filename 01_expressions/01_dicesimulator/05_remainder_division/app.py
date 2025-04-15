def main():
    try:
        # User se input lena
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        # Zero se divide hone ka error handle karna
        if divisor == 0:
            print("❌ Error: Division by zero is not allowed!")
            return  # Program yahan se exit kar jayega

        # Division ka result aur remainder nikalna
        quotient = dividend // divisor
        remainder = dividend % divisor

        # Output print karna
        print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("❌ Error: Please enter valid integer numbers!")

# Standard method to run the program
if __name__ == '__main__':
    main()
