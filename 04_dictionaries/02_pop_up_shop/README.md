# 🛒 Fruit Shop Cost Calculator

This Python program helps you calculate the total cost of fruits you want to buy from a shop. It uses a dictionary of fruits with their prices, takes user input for how many of each fruit they want, and calculates the total.

## 💻 Code

```python
def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0
    for fruit_name in fruits:
        try:
            amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
            total_cost += fruits[fruit_name] * amount_bought
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Your total is ${total_cost}")

if __name__ == '__main__':
    main()

How many (apple) do you want?: 2  
How many (durian) do you want?: 0  
How many (jackfruit) do you want?: 1  
How many (kiwi) do you want?: 0  
How many (rambutan) do you want?: 1  
How many (mango) do you want?: 3  
Your total is $99.5

✅ Features
Takes input for multiple fruits.

Calculates the total based on quantity and price.

Handles invalid input with error checking.