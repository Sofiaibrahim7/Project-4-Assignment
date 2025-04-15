def main():
    count = 0  # Counter to keep track of how many even numbers we've printed
    num = 0    # Starting number

    while count < 20:
        print(num, end=' ')
        num += 2       # Move to the next even number
        count += 1     # Increment the counter

if __name__ == '__main__':
    main()
