# Number Frequency Counter

## Problem Statement

This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

### Sample Run


Enter a number: 3
Enter a number: 4
Enter a number: 3
Enter a number: 6
Enter a number: 4
Enter a number: 3
Enter a number: 12
Enter a number: 3 appears 3 times.
4 appears 2 times.
6 appears 1 times.
12 appears 1 times.

pgsql
Copy
Edit

---

## Program Explanation

- **Input Collection**: Users are prompted to enter numbers one by one. A blank entry ends the input.
- **Data Storage**: All numbers are stored in a list.
- **Counting Logic**: A dictionary is used to keep track of how many times each number appears.
- **Display**: Finally, the frequency of each number is printed.

---

## Code Summary

- `get_user_numbers()` — collects input and returns a list of numbers.
- `count_nums(num_lst)` — uses a dictionary to count occurrences.
- `print_counts(num_dict)` — prints results in readable format.

---

## Concepts Used

- Loops  
- Conditional statements  
- Dictionary (hashmap)  
- Type conversion  
- Input validation  