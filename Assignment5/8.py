
month_to_season = {
    1: 'Winter',   # January
    2: 'Winter',   # February
    3: 'Spring',   # March
    4: 'Spring',   # April
    5: 'Spring',   # May
    6: 'Summer',   # June
    7: 'Summer',   # July
    8: 'Summer',   # August
    9: 'Fall',     # September
    10: 'Fall',    # October
    11: 'Fall',    # November
    12: 'Winter'   # December
}


def print_season(month_number):
    season = month_to_season.get(month_number, 'Invalid month number')
    print(f"Month {month_number} corresponds to {season}.")


month_number = int(input("Enter the month number (1-12): "))
print_season(month_number)
