"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / 2


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / (credits)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost,credits) * CS1430_CREDITS / (CS1430_MEETINGS_PER_SEMESTER)

def cost_per_party(annual_cost,party_count):
    '''Assumes the user only parties and does no class'''
    return annual_cost / party_count


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = float(input("How much does one year cost?: "))
    # Then ask for the credits this semester.
    credits_taking_per_semester = int(input("How many credits are you taking per semester?: "))

    while True:
        # Show your menu here.

        choice = input(f"{"="*30}\nChoose an option:\n[1] Semester Cost\n[2] Month Cost\n[3] Class Day Cost\n[4] Credit Cost\n[5] Cost per CS 1430 Class Session\n[6] Cost per Party\n[Q] Quit Program\nChoice: ")

        if choice == "Q":
            print(f"\nGoodbye!\n{30*"="}")
            break
        elif choice == "1":
            cost = cost_per_semester(annual_cost)
            print(f"One semester costs: ${cost:.2f}")
        elif choice == "2":
            cost = cost_per_month(annual_cost)
            print(f"One month costs: ${cost:.2f}")
        elif choice == "3":
            cost = cost_per_day(annual_cost)
            print(f"One day costs: ${cost:.2f}")
        elif choice == "4":
            cost = cost_per_credit(annual_cost, credits_taking_per_semester)
            print(f"One credit costs: ${cost:.2f}")
        elif choice == "5":
            cost  = cost_per_class(annual_cost, credits_taking_per_semester)
            print(f"One class day costs: ${cost:.2f}")
        elif choice == "6":
            party_count = int(input("[!] How many parties do you attend per year?: "))
            cost = cost_per_party(annual_cost,party_count)
            print(f"One Party costs: ${cost:.2f}")
        else:
            print("Unknown Command")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
