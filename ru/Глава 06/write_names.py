# Эта программа получает от пользователя три имени
# и пишет их в файл.

def main():
    # Получить три имени.
    print('Введите имена трех друзей.')
    name1 = input('Друг #1: ')
    name2 = input('Друг #2: ')
    name3 = input('Друг #3: ')

    # Открыть файл с именем friends.txt.
    myfile = open('friends.txt', 'w')

    # Записать имена в файл.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # Закрыть файл.
    myfile.close()
    print('Имена были записаны в friends.txt.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()