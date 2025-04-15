def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(f"\n✅ The first element you entered is: {lst[0]}")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    print("🔢 Let's build your list!")
    print("👉 Enter one element at a time. Press ENTER without typing anything to finish.\n")
    
    lst = []
    count = 1
    while True:
        elem = input(f"Enter element #{count}: ")
        if elem == "":
            break
        lst.append(elem)
        count += 1

    return lst

def main():
    lst = get_lst()
    print("\n📋 You entered this list:", lst)
    get_first_element(lst)

if __name__ == '__main__':
    main()
