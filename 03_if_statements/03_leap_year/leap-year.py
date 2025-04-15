# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check for leap year using the given conditions
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    else:
        print("That's a leap year!")
else:
    print("That's not a leap year.")
