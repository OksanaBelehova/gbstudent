import View
import db


def main():
    while True:
        mode = View.get_op()
        if mode == 1:
            data_worker = View.get_data()
            db.add_data(data_worker)
        if mode == 2:
            data_str = View.get_data_worker()
            View.find_person(data_str)
        if mode == 3:
            data_str = View.get_data_worker() 
            user_lst,full_lst = db.select_data_person(data_str) 
            num = View.get_number()
            db.delete_person(user_lst,full_lst,num)
        if mode == 4:
            data_str = View.get_data_worker() 
            user_lst,full_lst = db.select_data_person(data_str) 
            num = View.get_number()
            new_worker = View.get_data()
            db.change_data(user_lst,full_lst,num,new_worker)
        if mode == 5:
            db.read_all()
        if mode == 6:
            print('Выход')
            break