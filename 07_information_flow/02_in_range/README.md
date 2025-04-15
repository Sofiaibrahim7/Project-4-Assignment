## Problem Statement

Implement the following function which takes in 3 integers as parameters:

```python
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
Enter a number to check: 5
Enter the lower bound: 1
Enter the upper bound: 10
In range? True
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    n = int(input("Enter a number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    result = in_range(n, low, high)
    print("In range?" , result)

if __name__ == '__main__':
    main()
