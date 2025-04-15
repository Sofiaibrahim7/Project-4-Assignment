# 📝 Get First Element from User-Input List

This Python script allows the user to create a list by entering one element at a time, and then prints the **first element** of that list.

## 🚀 Features

- Interactive element-by-element input.
- Friendly prompts and clean output.
- Handles user-defined list of any length (minimum 1).
- Ensures the list is non-empty as per problem requirements.

## 📌 Problem Statement

Write a function `get_first_element(lst)` that takes a list `lst` as input and prints the first element. The list is **guaranteed to be non-empty**.

## 📂 How It Works

1. The user is prompted to enter list elements one at a time.
2. Pressing ENTER with no input ends the list.
3. The complete list is displayed.
4. The **first element** of the list is printed.

## 🧠 Code Explanation

```python
def get_first_element(lst):
    print(f"\n✅ The first element you entered is: {lst[0]}")

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
    get_first_element(lst)

if __name__ == '__main__':
    main()

🔢 Let's build your list!
👉 Enter one element at a time. Press ENTER without typing anything to finish.

Enter element #1: apple
Enter element #2: banana
Enter element #3: cherry
Enter element #4: 

📋 You entered this list: ['apple', 'banana', 'cherry']

✅ The first element you entered is: apple

## ✅ Requirements

- Python 3.x

## 📎 Note

Make sure you enter at least one element.  
An empty list will cause an error since the problem assumes the list is non-empty.
