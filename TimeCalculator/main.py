def add_time(start, duration, start_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM':
        start_hour += 12
    
    # Add duration
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    
    # Handle overflow of minutes
    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60
    
    # Calculate days later
    days_later = new_hour // 24
    new_hour %= 24
    
    # Determine period (AM/PM)
    new_period = 'AM' if new_hour < 12 else 'PM'
    
    # Convert hour to 12-hour format
    new_hour_12 = new_hour % 12
    if new_hour_12 == 0:
        new_hour_12 = 12
    
    # Format time string
    new_time = f'{new_hour_12}:{new_minute:02d} {new_period}'
    
    # Determine day of the week
    if start_day:
        start_day = start_day.lower().capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        if days_later == 1:
            days_later_str = ' (next day)'
        elif days_later > 1:
            days_later_str = f' ({days_later} days later)'
        else:
            days_later_str = ''
        new_time += f', {new_day}{days_later_str}'
    else:
        if days_later == 1:
            new_time += ' (next day)'
        elif days_later > 1:
            new_time += f' ({days_later} days later)'
    
    return new_time

# Test cases
print(add_time('3:30 PM', '2:12', 'Monday'))  # Should return '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))  # Should return '2:59 AM, Sunday (next day)'
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # Should return '12:04 AM, Friday (2 days later)'
print(add_time('8:16 PM', '466:02', 'tuesday'))  # Should return '6:18 AM, Monday (20 days later)'
