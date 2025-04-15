def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    return sum(numbers)  # Use Python's built-in sum() function to calculate the sum

def main() -> None:
    # List of numbers for testing
    numbers: list[int] = [1, 2, 3, 4, 5]  
    sum_of_numbers: int = add_many_numbers(numbers)  # Get the sum of the numbers
    print(f"The sum of the numbers is: {sum_of_numbers}")  # Print the sum

if __name__ == '__main__':
    main()
