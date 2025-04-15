📊 Average Finder — Python Program
🧠 Problem Statement
Write a function that takes two numbers and finds the average between the two.

💡 Logic
The average between two numbers a and b is calculated using:

(a + b) / 2
💻 Python Code
python
def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
🧪 Output

avg_1 5.0
avg_2 9.0
final 7.0
