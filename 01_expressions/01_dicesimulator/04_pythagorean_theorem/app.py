import math  # Math library ko import karna zaroori hai sqrt function ke liye

def main():
    while True:
        try:
            # User se input lena
            ab = input("Enter the length of AB (or type 'exit' to quit): ")
            
            # Program exit ka option
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

            # Hypotenuse calculate karna
            bc = math.sqrt(ab**2 + ac**2)

            # Output format
            print("\n📏 **Triangle Calculation** 📏")
            print(f"🔹 Side AB = {ab:.2f}")
            print(f"🔹 Side AC = {ac:.2f}")
            print(f"🔹 Hypotenuse BC = {bc:.2f} ✨")

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Program ko run karne ka standard method
if __name__ == '__main__':
    main()
