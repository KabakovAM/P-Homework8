import csv
import user_interface
import controller

employee_csv = 'employee.csv'
employee_id_csv = 'employee_id.csv'
timetable_csv = 'timetable.csv'


def employee_data_add():
    timetable=['10:00','11:00','12:00','13:00','14:00','15:00','16:00']
    global_id = 0
    new_data = user_interface.employee_data_add(0)
    with open(employee_id_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            global_id = int(*line)
    with open(employee_csv, 'a', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id, new_data])
    with open(timetable_csv, 'a', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id, *timetable])
    with open(employee_id_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id+1])
    user_interface.employee_data_add(1)
    return controller.click_button_1()


def employee_data_delete():
    old = user_interface.employee_data_delete(0)
    with open(employee_csv, 'r', encoding='utf-8') as inp:
        newrows = []
        data = csv.reader(inp)
        for line in data:
            if line[0] != old:
                newrows.append(line)
    with open(employee_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        for line in newrows:
            data.writerow(line)
    with open(timetable_csv, 'r', encoding='utf-8') as inp:
        newrows = []
        data = csv.reader(inp)
        for line in data:
            if line[0] != old:
                newrows.append(line)
    with open(timetable_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        for line in newrows:
            data.writerow(line)
    user_interface.employee_data_delete(1)
    return controller.click_button_1()


def employee_data_print():
    print_empl()
    data = user_interface.data_print()
    if data == 0:
        return controller.click_button_1()


def print_empl():
    print('\n')
    with open(employee_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp, delimiter=',')
        for line in data:
            print(line[0], line[1])
