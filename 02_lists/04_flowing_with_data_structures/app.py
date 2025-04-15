def add_three_copies(my_list, data1, data2, data3):
    # Add three different data inputs to the list
    my_list.append(data1)
    my_list.append(data2)
    my_list.append(data3)

def main():
    # Input three different messages from the user
    message1 = input("Enter the first message: ")
    message2 = input("Enter the second message: ")
    message3 = input("Enter the third message: ")
    
    # Initialize an empty list
    my_list = []
    
    # Print the list before adding the messages
    print("List before:", my_list)
    
    # Add the three messages to the list
    add_three_copies(my_list, message1, message2, message3)
    
    # Print the list after adding the messages
    print("List after:", my_list)

# Call main function to run the program
if __name__ == "__main__":
    main()
