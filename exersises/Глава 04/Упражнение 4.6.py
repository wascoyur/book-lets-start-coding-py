# Упражнение по программированию 4.6

# Таблица соответствия между градусами Цельсия и градусами Фаренгейта

# Объявить переменную для температуры в градусах 
# по шкале Фаренгейта.
fahrenheit = 0.0

# Вычислить и напечатать величину для каждой температуры.
print ('Цельсий\t\t\tФаренгейт')
print ('-------------------------')

for celsiusDegree in range(21):
    fahrenheit = ((9 * celsiusDegree) / 5) + 32
    print (celsiusDegree, '\t\t\t', fahrenheit)