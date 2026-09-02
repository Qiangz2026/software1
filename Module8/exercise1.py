def get_season(month_number):
    season_tuple = ("winter", "spring", "summer", "autumn")
    if 3 <= month_number <= 5:
        season = season_tuple[1]
    elif 6 <= month_number <= 8:
        season = season_tuple[2]
    elif 9 <= month_number <= 11:
        season = season_tuple[3]
    else:
        season = season_tuple[0]
    return season
    
month_number = int(input("Enter the number of a month (1-12): "))
if 1 <= month_number <= 12:
    season = get_season(month_number)
    print(f"You entered: {month_number}\nThe season is {season}.")
else:
    print(f"You entered: {month_number}\nPlease enter a number between 1 and 12.")