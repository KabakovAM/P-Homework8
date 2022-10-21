import csv
import user_interface
import controller

service_csv = 'service.csv'
service_id_csv = 'service_id.csv'


def service_data_add():
    global_id = 0
    new_1 = user_interface.service_data_add(0)
    new_2 = user_interface.service_data_add(1)
    with open(service_id_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            global_id = int(*line)
    with open(service_csv, 'a', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id, new_1, new_2])
    with open(service_id_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id+1])
    user_interface.service_data_add(2)
    return controller.click_button_2()


def service_data_delete():
    old = user_interface.service_data_delete(0)
    with open(service_csv, 'r', encoding='utf-8') as inp:
        newrows = []
        data = csv.reader(inp)
        for line in data:
            if line[0] != old:
                newrows.append(line)
    with open(service_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        for line in newrows:
            data.writerow(line)
    user_interface.service_data_delete(1)
    return controller.click_button_2()


def service_data_print():
    print_ser()
    num = user_interface.data_print()
    if num == 0:
        return controller.click_button_2()


def print_ser():
    print('\n')
    with open(service_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp, delimiter=',')
        for line in data:
            print(f'{line[0]} {line[1]}: {line[2]} рублей')
