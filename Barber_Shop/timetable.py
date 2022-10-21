import csv
import user_interface
import controller


timetable_csv = 'timetable.csv'
employee_csv = 'employee.csv'
client_csv = 'client.csv'


def tt_data_add(new_empl):
    newrows = []
    with open(timetable_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            newrows.append(line)
    tt = user_interface.client_data_add(new_empl, 1)
    for line in newrows:
        if line[0] == new_empl:
            line.remove(tt)
    with open(timetable_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        for line in newrows:
            data.writerow(line)
    return tt


def tt_data_delete(old_line):
    old_id = 0
    newrows = []
    with open(employee_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            if line[1] == old_line[1]:
                old_id = line[0]
    with open(timetable_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            newrows.append(line)
    for line in newrows:
        if line[0] == old_id:
            line.append(old_line[2])
            line[1:] = sorted(line[1:])
    with open(timetable_csv, 'w', encoding='utf-8') as out:
        data = csv.writer(out, lineterminator='\n')
        for line in newrows:
            data.writerow(line)


def show():
    newrows = []
    with open(client_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            newrows.append(line[1:5])
    newrows.sort()
    temp = newrows[0][0]
    print('\n')
    print(temp)
    for line in newrows:
        if line[0] == temp:
            print(f'{line[1]} {line[2]}: {line[3]}')
        else:
            temp = line[0]
            print(line[0])
            print(f'{line[1]} {line[2]}: {line[3]}')
    num = user_interface.data_print()
    if num == 0:
        return controller.click_button_main()

def print_tt(new_empl):
    print('\n')
    with open(timetable_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            if line[0] == new_empl:
                for row in line[1:]:
                    print(row)