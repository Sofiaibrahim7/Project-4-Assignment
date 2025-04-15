# 🧮 Fibonacci Sequence up to 10,000

## 📘 Problem Statement

Write a Python program that prints the terms of the **Fibonacci sequence** up to a maximum value of `10,000`.

> In the 13th century, Leonardo Fibonacci created a mathematical sequence to describe the growth of a rabbit population. The sequence starts with 0 and 1, and each new term is the sum of the two previous ones.

### 🧠 Formula:

Fib(0) = 0
Fib(1) = 1
Fib(n) = Fib(n-1) + Fib(n-2)


The output should display all Fibonacci numbers **less than or equal to 10,000**.


## ▶️ Sample Output

0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765


## ✅ Python Code

**Copy the following code and paste it into a Python file (e.g., `fibonacci_sequence.py`):**

```python
MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci number
    next_term = 1  # The 1st Fibonacci number
    
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)   # Line to print the current Fibonacci number
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# Required line to call main function
if __name__ == '__main__':   # Paste this line as the last part
    main()   # Call the main function to execute the program
💡 Explanation
How the code works:
Initialize the first two Fibonacci numbers:
The program starts by setting curr_term to 0 (the first Fibonacci number) and next_term to 1 (the second Fibonacci number).

Printing Fibonacci terms:
The while loop keeps running as long as the current Fibonacci number (curr_term) is less than or equal to MAX_TERM_VALUE (which is set to 10,000). Inside the loop, it prints the curr_term.

Calculating the next term:
The next Fibonacci term is calculated by summing curr_term and next_term. This sum is stored in term_after_next. After that, curr_term is updated to be the value of next_term, and next_term is updated to the newly calculated Fibonacci term (term_after_next).

Stopping condition:
Once the curr_term exceeds the MAX_TERM_VALUE, the loop stops, and the program terminates.

Output:
The program will print the Fibonacci numbers starting from 0 and 1, and it will continue printing until the current Fibonacci number is greater than 10,000. The printed numbers will be:

0  
1  
1  
2  
3  
5  
8  
13  
21  
34  
55  
89  
144  
233  
377  
610  
987  
1597  
2584  
4181  
6765
