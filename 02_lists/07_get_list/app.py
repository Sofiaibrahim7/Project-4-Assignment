def main():
    lst = []  # Create an empty list to store the values

    # Ask the user to input values
    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input is not empty
        lst.append(val)  # Add the input value to the list
        val = input("Enter a value: ")  # Get the next value to add

    # Print the list after the user stops entering values
    print("Here's the list:", lst)


if __name__ == '__main__':
    main()  # Call the main function to execute the program
