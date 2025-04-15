# Constants
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Step 1: Print individual constants
    print(f"Days in a year: {DAYS_PER_YEAR}")
    input("Press Enter to continue...")  # User input to proceed

    print(f"Hours in a day: {HOURS_PER_DAY}")
    input("Press Enter to continue...")

    print(f"Minutes in an hour: {MIN_PER_HOUR}")
    input("Press Enter to continue...")

    print(f"Seconds in a minute: {SEC_PER_MIN}")
    input("Press Enter to continue...")

    # Step 2: Calculate total hours in a year
    total_hours = DAYS_PER_YEAR * HOURS_PER_DAY
    print(f"Total hours in a year: {total_hours}")
    input("Press Enter to continue...")

    # Step 3: Calculate total minutes in a year
    total_minutes = total_hours * MIN_PER_HOUR
    print(f"Total minutes in a year: {total_minutes}")
    input("Press Enter to continue...")

    # Step 4: Calculate total seconds in a year
    total_seconds = total_minutes * SEC_PER_MIN
    print(f"Total seconds in a year: {total_seconds}")
    input("Press Enter to continue...")

    # Final Output
    print(f"\nThere are {total_seconds} seconds in a year!")

if __name__ == '__main__':
    main()
