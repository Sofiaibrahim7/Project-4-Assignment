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
