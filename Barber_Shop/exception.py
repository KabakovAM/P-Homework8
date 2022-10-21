import csv
employee_csv = 'employee.csv'
service_csv = 'service.csv'
timetable_csv = 'timetable.csv'
client_csv = 'client.csv'

def data_menu(num, n):
    if num.isdigit() and 0 <= int(num) <= n:
        return True
    return False


def data_emp(num):
    with open(employee_csv, 'r', encoding='utf-8') as inp:
        check = []
        data = csv.reader(inp)
        for line in data:
            check.append(line[0])
    if num.isdigit() and num in check:
        return True
    return False

def data_ser(num):
    with open(service_csv, 'r', encoding='utf-8') as inp:
        check = []
        data = csv.reader(inp)
        for line in data:
            check.append(line[0])
    if num.isdigit() and num in check:
        return True
    return False


def data_tt(new_empl,num):
    with open(timetable_csv, 'r', encoding='utf-8') as inp:
        check = []
        data = csv.reader(inp)
        for line in data:
            if line[0]==new_empl:
                for row in line[1:]:
                    check.append(row)
    if num in check:
        return True
    return False

def data_client(num):
    with open(client_csv , 'r', encoding='utf-8') as inp:
        check = []
        data = csv.reader(inp)
        for line in data:
            check.append(line[0])
    if num.isdigit() and num in check:
        return True
    return False

def data_client_show(num):
    with open(client_csv , 'r', encoding='utf-8') as inp:
        check = []
        data = csv.reader(inp)
        for line in data:
            check.append(line[3])
    if num in check:
        return True
    return False
