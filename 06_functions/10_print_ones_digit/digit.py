def print_ones_digit(num):
    # Using modulo operator to find the ones digit
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))  # Prompt user for input
    print_ones_digit(num)  # Call the function to print the ones digit

if __name__ == '__main__':
    main()  # Execute main function
