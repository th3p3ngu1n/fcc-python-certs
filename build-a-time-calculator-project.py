** start of main.py **

DAYS_OF_WEEK = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
]

def add_time(start, duration, day_of_week=''):

    start_info = start.split(':')
    start_hours = start_info[0]
    start_mins, start_m = start_info[1].split(' ')

    duration_hours, duration_mins = duration.split(':')
    new_m = start_m
    
    total_mins = (int(start_hours) * 60) + (int(duration_hours) * 60) + int(start_mins) + int(duration_mins)
    
    new_hours = total_mins // 60
    days = new_hours // 24
    new_mins = total_mins % 60

    if new_hours > 12:
        if start_m == 'PM':
            days += 1
        while True:
            diff = new_hours - 12
            new_hours = diff
            if diff <= 12:
                if days % 2 == 0:
                    new_m = get_opposite_m(new_m)
                elif start_m == 'PM':
                    new_m = get_opposite_m(new_m)
                break
    elif days == 0 and start_m == 'AM' and duration != '0:00':
        new_m = get_opposite_m(new_m)
        
    new_time = f'{new_hours}:{new_mins:02} {new_m}'

    if day_of_week:
        day_of_week = get_day_of_week(day_of_week, days)
        new_time += f', {day_of_week}'
    if days == 1:
        new_time += f' (next day)'
    if days > 1:
        days_info = f'({days} days later)'
        new_time += f' {days_info}'
    
    print(new_time)
    return new_time

def get_opposite_m(m):
    if m == 'PM':
        return 'AM'
    return 'PM'

def get_day_of_week(day, days):
    if not day or day == '':
        return ''
    if days == 0:
        return day.lower().title()
    
    index = DAYS_OF_WEEK.index(day.lower())
    
    new_index = (index + days) % 7
    
    return DAYS_OF_WEEK[new_index].title()


** end of main.py **

