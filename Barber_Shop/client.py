import csv
import employee
import service
import user_interface
import controller
import timetable

client_id_csv = 'client_id.csv'
client_csv = 'client.csv'
service_csv = 'service.csv'
employee_csv = 'employee.csv'

def client_data_add():
    global_id = 0
    with open(client_id_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            global_id = int(*line)
    new_empl = user_interface.client_data_add (0,0)
    new_time = timetable.tt_data_add(new_empl)
    new_client = user_interface.client_data_add (0,2)
    new_serv = user_interface.client_data_add (0,3)
    with open(employee_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            if line[0] == new_empl:
                new_empl=line[1]
    with open(service_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            if line[0] == new_serv:
                new_serv=line[1:]
    with open(client_csv, 'a', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id, new_empl, new_time, new_client, *new_serv])
    with open(client_id_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        data.writerow([global_id+1])
    user_interface.client_data_add (0,4)
    return controller.click_button_3()


def client_data_delete():
    old = user_interface.client_data_delete(0)
    with open(client_csv, 'r', encoding='utf-8') as inp:
        newrows = []
        data = csv.reader(inp)
        for line in data:
            if line[0]==old:
                timetable.tt_data_delete(line)
            if line[0] != old:
                newrows.append(line)
    with open(client_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        for line in newrows:
            data.writerow(line)
    user_interface.client_data_delete(1)
    return controller.click_button_3()


def client_data_print():
    name = user_interface.client_data_print()
    if name ==0:
        return controller.click_button_3()
    with open(client_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp, delimiter=',')
        for line in data:
            if line[3] == name:
                print(f'{line[0]} {line[1]}|{line[2]}| {line[4]} {line[5]} рублей')
    num = user_interface.data_print()
    if num == 0:
        return controller.click_button_3()

def print_client():
    print('\n')
    with open(client_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp, delimiter=',')
        for line in data:
            print(line[0], line[3])