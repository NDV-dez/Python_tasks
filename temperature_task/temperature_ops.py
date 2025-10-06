from temperature_data import get_temperatures, set_temperatures

def first_day(target_temp):
    temps = get_temperatures()
    for i, temp in enumerate(temps):
        if temp > target_temp:
            return i
    return -1

def last_day(target_temp):
    temps = get_temperatures()
    for i in range(len(temps)-1, -1, -1):
        if temps[i] <= target_temp:
            return i
    return -1

def count_day(target_temp):
    temps = get_temperatures()
    count = 0
    for temp in temps:
        if temp < target_temp:
            count += 1
    return count

def add_temperatures(new_temps):
    temps = get_temperatures()
    temps.extend(new_temps)
    set_temperatures(temps)
    return temps

def remove_last_day():
    temps = get_temperatures()
    if temps:
        removed = temps.pop()
        set_temperatures(temps)
        return removed
    return None

def merge_months(other_temps):
    temps = get_temperatures()
    merged = temps + other_temps
    set_temperatures(merged)
    return merged

def filter_temps(threshold):
    temps = get_temperatures()
    filtered = [temp for temp in temps if temp > threshold]
    set_temperatures(filtered)
    return filtered

def celsius_to_fahrenheit():
    temps = get_temperatures()
    fahrenheit = [(temp * 9/5) + 32 for temp in temps]
    set_temperatures(fahrenheit)
    return fahrenheit

def has_above_temp(threshold):
    temps = get_temperatures()
    return any(temp > threshold for temp in temps)

def all_above_temp(threshold):
    temps = get_temperatures()
    return all(temp > threshold for temp in temps)

def clear_temps():
    set_temperatures([])
    return []

def sort_temps(ascending=True):
    temps = get_temperatures()
    temps.sort(reverse=not ascending)
    set_temperatures(temps)
    return temps

def count_total_days():
    return len(get_temperatures())