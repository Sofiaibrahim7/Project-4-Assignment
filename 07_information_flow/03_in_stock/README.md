## Problem Statement

Sophia has a fruit store. She has written a function `num_in_stock` which takes a string `fruit` as a parameter and returns how many of that fruit are in her inventory.

Write code in `main()` which will:

1. Prompt the user to enter a fruit (`"Enter a fruit: "`)
2. Call `num_in_stock(fruit)` to get the number of that fruit that Sophia has in stock
3. Print the number which are in stock if Sophia has that fruit in her inventory (more than 0 in stock)
4. Print `"This fruit is not in stock."` if Sophia has none of that fruit in her inventory.

---

## Sample Runs

**Run 1:**

## Problem Statement

Sophia has a fruit store. She has written a function `num_in_stock` which takes a string `fruit` as a parameter and returns how many of that fruit are in her inventory.

Write code in `main()` which will:

1. Prompt the user to enter a fruit (`"Enter a fruit: "`)
2. Call `num_in_stock(fruit)` to get the number of that fruit that Sophia has in stock
3. Print the number which are in stock if Sophia has that fruit in her inventory (more than 0 in stock)
4. Print `"This fruit is not in stock."` if Sophia has none of that fruit in her inventory.

---

## Sample Runs

**Run 1:**

## Problem Statement

Sophia has a fruit store. She has written a function `num_in_stock` which takes a string `fruit` as a parameter and returns how many of that fruit are in her inventory.

Write code in `main()` which will:

1. Prompt the user to enter a fruit (`"Enter a fruit: "`)
2. Call `num_in_stock(fruit)` to get the number of that fruit that Sophia has in stock
3. Print the number which are in stock if Sophia has that fruit in her inventory (more than 0 in stock)
4. Print `"This fruit is not in stock."` if Sophia has none of that fruit in her inventory.

---

## Sample Runs

**Run 1:**

Enter a fruit: pear This fruit is in stock! Here is how many: 1000
**Run 2:**

Enter a fruit: lychee This fruit is not in stock.
---

## Solution

```python
def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # this fruit is not in stock.
        return 0

def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == '__main__':
    main()
