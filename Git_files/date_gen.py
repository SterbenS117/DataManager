from datetime import datetime, timedelta

# Start and end years
start_year = 2012
end_year = 2015

# List to hold the dates
mondays = []

# Iterate over the years and months
current_date = datetime(start_year, 1, 1)
end_date = datetime(end_year + 1, 1, 1)

# Adjust the start date if the first day is not a Monday
if current_date.weekday() != 0:
    current_date += timedelta(days=(7 - current_date.weekday()))

while current_date < end_date:
    # Exclude months of September to December and January to March
    if 4 <= current_date.month <= 8:
        mondays.append(current_date.strftime('%m/%d/%Y'))

    # Move to the next Monday
    current_date += timedelta(weeks=1)

# Writing the dates to a file
file_path = 'mondays_2012_2015.txt'
with open(file_path, 'w') as file:
    for date in mondays:
        file.write(date + '\n')