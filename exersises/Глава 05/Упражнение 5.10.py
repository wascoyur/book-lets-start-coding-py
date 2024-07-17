# Упражнение по программированию 5.10

# Футы в дюймы

# Главная функция
def main():
    
    # Локальные переменные
    feet = 0.0
    inches = 0.0

    # Получить от пользователя количество футов.
    feet = float(input('Введите количество футов: '))

    # Показать соответствующее количество дюймов.
    inches = feet_to_inches(feet)
    print (feet, 'футов =', inches, 'дюймов')
    
# Функция feet_to_inches принимает в качестве аргументов 
# количество футов и возвращает количество дюймов для
# этого количество футов.
def feet_to_inches(feet):
    return 12 * feet

# Вызвать главную функцию.
main()