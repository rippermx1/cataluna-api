from datetime import datetime
from firebase import Calendar


calendar = Calendar()
current_year = datetime.now().year

calendar.create_year(str(current_year))

for month in range(3, 13):
    calendar.create_month(str(current_year), str(month))
    for day in range(1, 32):
        try:
            date = datetime(current_year, month,
                            day).date().strftime('%Y-%m-%d')
            calendar.create_day(str(current_year), str(month), date)

            # Loop through each hour of the day
            for hour in range(8, 20):
                # Create a document with the hour details
                label = f'{str(hour)}:00 AM' if hour < 12 else f'{
                    str(hour)}:00 PM'
                doc = {
                    'label': label,
                    'available': True
                }

                calendar.create_hour(
                    str(current_year), str(month), date, hour, doc)

        except ValueError:
            # Skip invalid dates (e.g., February 30th)
            continue
