def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop
        if user_input == "":
            break
        
        # Convert the input to integer and add to list
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print how many times each number appeared.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    """
    Main function to execute the program flow.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Python boilerplate
if __name__ == '__main__':
    main()
