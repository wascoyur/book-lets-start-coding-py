# Эта программа использует цикл для вывода
# таблицы чисел и их квадратов.

# Получить начальное значение.
print('Эта программа выводит список чисел')
print('и их квадратов.')
start = int(input('Введите начальное число: '))

# Получить конечный предел.
end = int(input('Насколько далеко мне заходить? '))
 
# Напечатать заголовки таблицы.
print()
print('Число\tКвадрат числа')
print('---------------------')

# Напечатать числа и их квадраты.
for number in range(start, end + 1):
    square = number**2
    print(f'{number}\t{square}')