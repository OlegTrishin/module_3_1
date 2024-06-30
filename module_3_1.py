calls = 0  # Создаём переменную calls вне функций


def count_calls():  # Создаём первую функцию count_calls подсчитывающую вызовы остальных функций
    global calls    # Используем глобальную переменную calls
    calls += 1      # Подсчитываем вызовы


def string_info(string):                                        # Создаём вторую функцию string_info с параметром string
    count_calls()                                               # Вызываем функцию count_calls для подсчета
    return (len(string), string.upper(), string.lower())
    # Принимает аргумент строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре


def is_contains(string, list_to_search):    # Создаём третью функцию is_contains с двумя параметрами string и list_to_search
    count_calls()                           # Вызываем функцию count_calls для подсчета
    string = string.lower()                 # Приводим строку с любым регистром в строку в нижнем регистре
    for item in list_to_search:             # Проверяем есть ли строка в списке с помощью цикла
        if string == item.lower():          # Проверяем есть ли строка в списке
            return True                     # Возвращает True, если строка находится в этом списке
    return False                            # Возвращает False, если строка отсутствует в этом списке


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

