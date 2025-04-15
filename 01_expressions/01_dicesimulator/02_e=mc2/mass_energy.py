# Program to calculate energy using Einstein's equation E = m * c^2

# Define the speed of light as a constant (m/s)
C = 299792458  

def main():
    while True:  # Infinite loop for multiple calculations
        try:
            # User input
            mass_in_kg = input("\nEnter mass in kilograms (or type 'exit' to quit): ")

            # Check if user wants to exit
            if mass_in_kg.lower() == 'exit':
                print("\nExiting the program. Goodbye! 🚀")
                break

            # Convert input to float
            mass_in_kg = float(mass_in_kg)

            # Validate input (mass should be positive)
            if mass_in_kg <= 0:
                print("❌ Error: Mass must be a positive number!")
                continue

            # Calculate energy using Einstein's formula
            energy_in_joules = mass_in_kg * (C ** 2)

            # Display output with improved formatting
            print("\n💡 Energy Calculation 💡")
            print("---------------------------------")
            print(f"🔹 Mass (m)          = {mass_in_kg} kg")
            print(f"🔹 Speed of Light (C) = {C} m/s")
            print(f"🔹 Energy (E)        = {energy_in_joules:.2e} joules ⚡")
            print("---------------------------------")

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Standard Python entry point
if __name__ == '__main__':
    main()
