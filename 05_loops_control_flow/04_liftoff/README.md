## Liftoff Countdown Problem - Solution Explanation

### Problem
Write a program that performs a countdown from 10 to 1, and then prints `"Liftoff!"`.

### Approach
We can use a `for` loop with Python's `range()` function to count down from 10. The `range(10)` gives values from `0` to `9`. We can subtract `i` from `10` to count backward.

### Python Code

```python
def main():
    for i in range(10):
        print(10 - i)
    print("Liftoff!")

if __name__ == '__main__':
    main()
### sample output
10
9
8
7
6
5
4
3
2
1
Liftoff!
