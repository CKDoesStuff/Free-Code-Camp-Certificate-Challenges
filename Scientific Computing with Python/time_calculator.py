def split_time(time):
    time_array = time.split(':')
    time_array[0] = int(time_array[0])

    if len(time_array[1]) > 2:
        split_minutes = time_array[1].split()

        if time_array[0] < 12 and split_minutes[1] == 'PM':
            # convert to 24h format for easier math
            time_array[0] = time_array[0] + 12
            time_array[1] = int(split_minutes[0])

        else:
            time_array[1] = int(split_minutes[0])

            if time_array[0] == 12 and split_minutes[1] == 'AM':
                time_array[0] = 0

    else:
        time_array[1] = int(time_array[1])

    return time_array

def add_time(start, duration, weekday = ''):
    DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_check = [day.upper() for day in DAYS]

    start_hours_minutes = split_time(start)
    duration_hours_minutes = split_time(duration)

    new_time = [
        start_hours_minutes[i] + duration_hours_minutes[i] 
        for i in range(2)
        ]

    if new_time[1] >= 60:
        new_time[0] += 1
        new_time[1] -= 60

    days_later = new_time[0] // 24
    if days_later > 0:
        new_time[0] -= 24 * days_later

        new_time.append(
            '(next day)'
            if days_later == 1 else
            f'({days_later} days later)'
        )

    if weekday:
            day_index = (days_check.index(weekday.upper()) + days_later) % 7
            new_time.insert(2, DAYS[day_index])

    # format minutes with leading zeroes for <10 values
    new_time[1] = f'{new_time[1]:02d} {"PM" if new_time[0] >= 12 else "AM"}'

    if new_time[0] == 0:
        new_time[0] = 12

    elif new_time[0] > 12:
        new_time[0] -= 12
    

    # this looks fucked but it just checks if each conditional element exists and then appends it to the end of the string if it does
    new_time = f"{':'.join([str(new_time[0]), new_time[1]])}{',' if len(new_time) > 2 and new_time[2] in DAYS else ''}{f' {new_time[2]}' if len(new_time) > 2 else ''}{f' {new_time[3]}' if len(new_time) > 3 else ''}"

    return new_time

if __name__ == '__main__':
    start_time = '3:30 PM'
    duration = '2:12'
    print(add_time(start_time, duration))
