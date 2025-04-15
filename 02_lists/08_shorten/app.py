MAX_LENGTH = 3  # You can change this for testing

def shorten(lst):
    # Check if the length of lst is greater than MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        # Remove the last item from the list and print it
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f"Original list: {lst}")
    shorten(lst)
    print(f"List after shortening: {lst}")

if __name__ == '__main__':
    main()
