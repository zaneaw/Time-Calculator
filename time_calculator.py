def add_time(start, duration, *day):
    # Variables
    new_time = ""
    new_hour = ""
    new_minute = ""
    new_meridiem = ""
    new_day = 0
    day_of_week = ""
    day_statement = ""
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # Breaking the sections of the start time into hours, minutes & AM/PM
    start = start.rstrip()
    start = start.split()
    meridiem = start[1]
    meridiem = meridiem.upper()
    time = start[0]
    time = time.split(":")
    start_hour = time[0]
    start_hour = int(start_hour)
    start_minute = time[1]
    start_minute = int(start_minute)

    # Breaking the duration into sections of hours & minutes
    duration = duration.rstrip()
    duration = duration.split(":")
    dur_hour = duration[0]
    dur_hour = int(dur_hour)
    dur_minute = duration[1]
    dur_minute = int(dur_minute)

    # Change PM to 12-24
    if meridiem == "PM":
        start_hour += 12
        
    # Math for minutes to hours
    new_hour = start_hour + dur_hour
    new_minute = start_minute + dur_minute
    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    # Change dur_hour into days and hours
    if new_hour > 24:
        new_day = int(new_hour / 24)  # Return a whole number
        new_hour = new_hour % 24  # ex: 241 % 24 = 1
        if new_day == 1:
            day_statement = "(next day)"
        if new_day > 1:
            day_statement = f"({new_day} days later)"

    # If new_hour from the above remainder = 0, change new_hour to 12:-- AM
    # else, if the remainder is greater than or equal to 12, new_meridiem = PM
    # and if the remainder is 1 to 11, new_meridiem = AM
    if new_hour == 0:
        new_hour = 12
        new_meridiem = "AM"
    elif new_hour >= 12:
        new_meridiem = "PM"
        if new_hour > 12:
            new_hour -= 12  # Change  back to 1-12 for return statement
    else:
        new_meridiem = "AM"

    # Turn new_minute into a 2 digit integer if it's only a 1 digit int
    new_minute = str(new_minute)
    new_minute = new_minute.zfill(2)

    # Optional Argument, only run if it's included
    if day:
        # Take the day of the week out of the optional argument and capitalize
        day = day[0]
        day = day.capitalize()
        # Match the day to list of days_of_week and pull out the index
        day_index = days_of_week.index(day)
        # Total # of days is calulcated above and added into day_statement
        # This allows us to cut down on loop or forgo loop while period
        new_day = new_day % 7
        # Return statement with optional arg and same day
        if new_day == 0:
            new_time = f"{new_hour}:{new_minute} {new_meridiem}, {day}"
        # Return statement with optional arg and next day
        elif new_day == 1:
            day_index += 1
            day = days_of_week[day_index]
            new_time = f"{new_hour}:{new_minute} {new_meridiem}, {day} {day_statement}"
        # Logic / Return statement if more than next day and cutting to the next week
        elif new_day > 1:
            if new_day + day_index >= 7:
                new_day = day_index - new_day
                day_index = 0
            while new_day > 0:
                new_day -= 1
                day_index += 1
            day = days_of_week[day_index]
            new_time = f"{new_hour}:{new_minute} {new_meridiem}, {day} {day_statement}"

    # Return statement, if it progresses by a day, add the day_statement
    # If *day is included, everything dont above, else complete below
    if day:
        return new_time
    else:
        if day_statement == "":
            new_time = f"{new_hour}:{new_minute} {new_meridiem}"
        else:
            new_time = (
                f"{new_hour}:{new_minute} {new_meridiem} {day_statement}"
            )

    return new_time