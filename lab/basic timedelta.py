from datetime import datetime
new_year = datetime(2021, 1, 1)
day_of_week = f"New Year's Day is on a {new_year:%A}"
print(new_year)
print(day_of_week)