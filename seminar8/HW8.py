# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

# Логика алгоритма для изменения:
# 1. Прочитать в переменную информацию из файла.
# 2. Внести нужные правки в этой информации(для этого можно вызвать поиск, чтобы понять, что конкретно меняем).
# 3. Перезаписать файл через 'w'

# P.s. Для уточнения поиска редактируемого элемента можно воспользоваться функцией enumerate.
# Для нахождения индекса вхождения в массиве можно использовать .index(<вхождение>)
def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt','r',encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляем информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt','a',encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')

def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book.txt','r',encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book,data))

def search(book: str,info: str) -> str:
    '''Находит в строке запии по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def change_data(user_list, ful_list,num) ->str:
    '''Изменяет данные'''
    old_data = input('Что надо изменить?: ')
    new_data = input('Что записать?: ')
    with open('book.txt','w',encoding='utf-8') as f:
        print(user_list, ful_list,num)
        for line in ful_list:
            if user_list[num-1]!=line:
                f.write(line)
            else:


def get_number():
    num = int(input('Выбирите строку для изменения: '))
    return num

def delete_data(user_list, ful_list,num):
    with open('book.txt','w',encoding='utf-8') as f:
        print(user_list, ful_list,num)
        for line in ful_list:
            if user_list[num-1]!=line:
                f.write(line)
    print('Готово')

while True:
    print('1. Вывод, 2. Добавление, 3. Поиск, 4. Изменение, 5. Удаление, 6. Выход')
    mode = int(input())
    if mode == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode == 4:
        change_data()
    elif mode == 5:
        delete_data()
    elif mode == 6:
        print('Выход')
        break