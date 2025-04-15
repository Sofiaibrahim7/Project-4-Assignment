from colorama import Fore, Style, init

# Enable colorama auto-reset for Windows
init(autoreset=True)  

INCHES_IN_FOOT = 12  

def main():
    while True:
        try:
            feet = input(Fore.CYAN + "\nEnter number of feet (or type 'exit' to quit): " + Style.RESET_ALL)

            if feet.lower() == 'exit':
                print(Fore.GREEN + "\nExiting the program. Goodbye! 🚀" + Style.RESET_ALL)
                break

            feet = float(feet)

            if feet < 0:
                print(Fore.RED + "❌ Error: Feet value must be a non-negative number!" + Style.RESET_ALL)
                continue

            inches = feet * INCHES_IN_FOOT

            print(Fore.YELLOW + "\n📏 **Conversion Result** 📏" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"🔹 Feet = {feet:.2f} ft" + Style.RESET_ALL)
            print(Fore.BLUE + f"🔹 Inches = {inches:.2f} inches ✨" + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "❌ Invalid input! Please enter a valid number." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
