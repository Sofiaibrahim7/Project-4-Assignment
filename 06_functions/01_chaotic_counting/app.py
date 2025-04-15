import random

# The likelihood that 'done' will return True
DONE_LIKELIHOOD = 0.5  # You can adjust this value to simulate different behaviors

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        # Check if we're done
        if done():
            return  # End the function execution, and we'll go back to main()
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

# This line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
