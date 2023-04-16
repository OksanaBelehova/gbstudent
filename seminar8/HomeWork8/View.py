def get_op():
    print('1. Добавление, 2. Посмотреть конкретного, 3. Удалить, 4. Изменить, 5. Вывести все, 6. Выход')
    mode = int(input())
    return mode

def get_data():
    print('Введите новые данные')
    fio = input('Введите ФИО: ')
    telephone = input('Введите номер телефона: ')
    data_str = fio + ' ' + telephone + '\n'
    return data_str

def find_person(data_str) -> str:
    '''Осуществляет поиск по справочнику'''
    with open('book.txt','r',encoding='utf-8') as f:
        lst_str = f.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker)

def get_data_worker():
    data = input('Введите данные о пользователе, которые хотите посмотреть: ')
    return data

def get_number():
    num = int(input('Выбирите строку для изменения: '))
    return num