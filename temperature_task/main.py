from temperature_data import show_temp
from temperature_ops import *

def menu():
    print("\n=========МЕНЮ==========")
    print("1. Найти индекс первого дня, когда температура превысила заданное значение.")
    print("2. Найти индекс последнего дня, когда температура не превышала заданное значение.")
    print("3. Подсчитать количество дней, когда температура была ниже заданного значения.")
    print("4. Добавить в список температур еще один список температур за последние несколько дней месяца.")
    print("5. Удалить температуру последнего дня из списка.")
    print("6. Объединить два списка температур, представляющих собой данные двух разных месяцев.")
    print("7. Отфильтровать список, оставив только температуры, превышающие заданное значение.")
    print("8. Преобразовать список температур из Цельсия в Фаренгейты.")
    print("9. Проверить, был ли хотя бы один день с температурой выше заданного значения.")
    print("10. Проверить, были ли все дни с температурой выше заданного значения.")
    print("11. Очистить список температур.")
    print("12. Отсортировать список температур по возрастанию или убыванию.")
    print("13. Подсчитать общее количество дней (элементов) в списке температур.")
    print("0. Выход")
    print()

def main():
    while True:
        menu()
        choice = input("Введите номер задачи для выполнения: ")

        if choice == '1':
            show_temp()
            t = float(input("Температура: "))
            day = first_day(t)
            if day != -1:
                print(f"День {day+1}")
            else:
                print("Не найдено")
                
        elif choice == '2':
            show_temp()
            t = float(input("Температура: "))
            day = last_day(t)
            if day != -1:
                print(f"День {day+1}")
            else:
                print("Не найдено")

        elif choice == '3':
            show_temp()
            t = float(input("Температура: "))
            count = count_day(t)
            print(f"Кол-во дней: {count}")

        elif choice == '4':
            show_temp()
            new_temps = list(map(float, input("Введите новые температуры через пробел: ").split()))
            result = add_temperatures(new_temps)
            print("Новый список:", result)

        elif choice == '5':
            removed = remove_last_day()
            if removed is not None:
                print(f"Удалена температура: {removed}")
                show_temp()
            else:
                print("Список пуст")

        elif choice == '6':
            show_temp()
            other_temps = list(map(float, input("Введите температуры второго месяца через пробел: ").split()))
            result = merge_months(other_temps)
            print("Объединенный список:", result)

        elif choice == '7':
            show_temp()
            t = float(input("Пороговая температура: "))
            result = filter_temps(t)
            print("Отфильтрованный список:", result)

        elif choice == '8':
            result = celsius_to_fahrenheit()
            print("Температуры в Фаренгейтах:", result)

        elif choice == '9':
            t = float(input("Температура: "))
            result = has_above_temp(t)
            print(f"Есть дни выше {t}°C: {'Да' if result else 'Нет'}")

        elif choice == '10':
            t = float(input("Температура: "))
            result = all_above_temp(t)
            print(f"Все дни выше {t}°C: {'Да' if result else 'Нет'}")

        elif choice == '11':
            clear_temps()
            print("Список очищен")
            show_temp()

        elif choice == '12':
            order = input("Сортировать по возрастанию? (да/нет): ").lower()
            ascending = order in ['да', 'д', 'yes', 'y']
            result = sort_temps(ascending)
            print("Отсортированный список:", result)

        elif choice == '13':
            count = count_total_days()
            print(f"Общее количество дней: {count}")

        elif choice == '0':
            print("Выход из программы")
            break

        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()