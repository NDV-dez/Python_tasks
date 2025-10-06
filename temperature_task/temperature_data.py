temperatures = [15.5, 16.2, 14.8, 18.3, 20.1, 22.5, 19.8, 17.6, 16.9, 18.7,
                21.3, 23.1, 24.5, 22.8, 20.4, 19.1, 18.2, 17.8, 16.5, 15.9,
                17.3, 19.6, 21.8, 23.5, 24.9, 22.3, 20.7, 19.4, 18.9, 17.5]

def show_temp():
    print("Текущие температуры:", temperatures)
    return temperatures

def get_temperatures():
    return temperatures.copy()

def set_temperatures(new_temp):
    global temperatures
    temperatures = new_temp.copy()