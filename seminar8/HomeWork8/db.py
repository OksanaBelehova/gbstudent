
def add_data(data_str) -> str:
    '''Добавляем информацию в справочник'''
    with open('book.txt','a',encoding='utf-8') as f:
        f.write(data_str)
    print('Успешно!')

def select_data_person(worker):
    user_lst = []
    a = 1
    with open('book.txt','r',encoding='utf-8') as f:
        full_lst = f.readlines()
        for count, line in enumerate(full_lst):
            if worker in line:
                user_lst.append(line)
                print(f"{count +1} {line}")
    return (user_lst,full_lst)

def delete_person(user_lst,full_lst,num):
    with open('book.txt','w',encoding='utf-8') as f:
        print(user_lst,full_lst,num)
        for line in full_lst:
            if user_lst[num-1]!=line:
                f.write(line)
    print('Успешно!')


def change_data(user_lst,full_lst,num,new_worker) ->str:
    '''Изменяет данные'''
    with open('book.txt','w',encoding='utf-8') as f:
        print(user_lst, full_lst,num)
        for line in full_lst:
            if user_lst[num-1]!=line:
                f.write(line)
            else:
                f.write(new_worker)
    print('Успешно!')
def read_all() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt','r',encoding='utf-8') as f:
        print(f.read())