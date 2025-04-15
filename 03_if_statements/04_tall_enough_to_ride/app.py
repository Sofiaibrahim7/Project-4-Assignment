def main():
    MINIMUM_HEIGHT = 50  # Minimum height required for the ride

    while True:
        try:
            height = input("How tall are you? ")

            if height == "":  # Check if the user presses Enter without input
                print("Goodbye!")
                break

            height = float(height)  # Convert the input to a float

            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# Call the main function to run the program
if __name__ == '__main__':
    main()
