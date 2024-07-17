import random

# Класс Coin имитирует монету, которую
# можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных sideup значением 'Орел'.

    def __init__(self):
        self.sideup = 'Орел'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то sideup получает значение 'Орел'.
    # В противном случае sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Орел'
        else:
            self.sideup = 'Решка'

    # Метод get_sideup возвращает значение,
    # на которое ссылается sideup.

    def get_sideup(self):
        return self.sideup

# Главная функция.
def main():
    # Создать объект на основе класса Coin.
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Подбрасываю монету...')
    my_coin.toss()

    # Но теперь я обману! В этом объекте 
    # я собираюсь напрямую поменять  
    # значение атрибута sideup на 'Орел'.
    my_coin.sideup = 'Орел'

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

# Вызвать главную функцию.
if __name__ == '__main__':
    main()