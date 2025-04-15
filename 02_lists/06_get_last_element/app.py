def get_last_element(lst):
    print(f"\n✅ The last element you entered is: {lst[-1]}")

def get_lst():
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
    get_last_element(lst)

if __name__ == '__main__':
    main()
