DAY_IN_MINUTES, MINUTE, TOTAL_DAYS_IN_WEEK, TWELVE_HOURS = (24 * 60), 60, 7, 12
DAYS_OF_WEEK = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')


def convert_12h_to_24h(time:str):
    import re

    hours, minutes, period = re.match(r'^(.+):(.+)\s(.+)$', time).groups()
    hours = int(hours)
    hours = hours == TWELVE_HOURS and period == 'AM' and '0' or \
        period == 'PM' and hours != TWELVE_HOURS and f'{hours + TWELVE_HOURS}' or hours
    
    return f'{hours}:{minutes}'


def convert_time_to_min(time:str):
    hours, minutes = time.split(':')
    return int(hours) * MINUTE + int(minutes)
   

def add_time(start:str, duration:str, start_day:str = ''):
    total_minutes = convert_time_to_min(convert_12h_to_24h(start)) + convert_time_to_min(duration)
    days, residual_minutes = divmod(total_minutes, DAY_IN_MINUTES)

    hours, minutes = divmod(residual_minutes, MINUTE)
    hours, period = hours % TWELVE_HOURS or TWELVE_HOURS, 'PM' if 24 > hours > 11 else 'AM'
    
    details = {0: '', 1: ' (next day)', 'many': f' ({days} days later)'}[days and (days == 1 or 'many')]
    final_day = start_day and f', {DAYS_OF_WEEK[(DAYS_OF_WEEK.index(start_day.capitalize()) + days) % TOTAL_DAYS_IN_WEEK]}'
    
    return f'{hours}:{minutes:02d} {period}{final_day}{details}'
