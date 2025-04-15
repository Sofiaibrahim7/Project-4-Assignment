📌 Right Triangle Hypotenuse Calculator
📝 Problem Statement
This program calculates the hypotenuse of a right triangle using the Pythagorean theorem:

𝐵
𝐶
=
(
𝐴
𝐵
2
+
𝐴
𝐶
2
)
BC= 
(AB 
2
 +AC 
2
 )
​
 
Where:

AB and AC are the two perpendicular sides (user input).

BC is the hypotenuse (output).

🎯 Features of the Program
✅ Takes user input for the two sides.
✅ Validates input (ensures positive numbers).
✅ Uses the Pythagorean theorem for calculation.
✅ Formats output for better readability.
✅ Allows multiple calculations (user can enter new values repeatedly).
✅ Exit option (type 'exit' to quit).

🚀 How to Run the Program?
Install Python if not already installed.

Open VS Code / Terminal.

Save the Python file as hypotenuse.py.

Run the following command in the terminal:

bash
Copy
Edit
python hypotenuse.py
🖥 Example Run
bash
Copy
Edit
Enter the length of AB (or type 'exit' to quit): 3
Enter the length of AC: 4

📏 **Triangle Calculation** 📏
🔹 Side AB = 3.00
🔹 Side AC = 4.00
🔹 Hypotenuse BC = 5.00 ✨

Enter the length of AB (or type 'exit' to quit): exit

Exiting the program. Goodbye! 🚀
🛠 Code Implementation
python
Copy
Edit
import math  # Import math library for sqrt function

def main():
    while True:
        try:
            # Get user input
            ab = input("Enter the length of AB (or type 'exit' to quit): ")
            
            # Exit condition
            if ab.lower() == 'exit':
                print("\nExiting the program. Goodbye! 🚀")
                break
            
            ac = input("Enter the length of AC: ")

            # Convert input to float
            ab = float(ab)
            ac = float(ac)

            # Validate input (sides should be positive)
            if ab <= 0 or ac <= 0:
                print("❌ Error: Side lengths must be positive numbers!")
                continue

            # Calculate hypotenuse
            bc = math.sqrt(ab**2 + ac**2)

            # Display output
            print("\n📏 **Triangle Calculation** 📏")
            print(f"🔹 Side AB = {ab:.2f}")
            print(f"🔹 Side AC = {ac:.2f}")
            print(f"🔹 Hypotenuse BC = {bc:.2f} ✨")

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Standard Python entry point
if __name__ == '__main__':
    main()
🎯 Why This README is Best?
✅ Professional structure
✅ Explains the problem & solution clearly
✅ Provides a sample run for clarity
✅ Includes step-by-step execution guide

✨ Created by: Sofia Ibrahim 🚀