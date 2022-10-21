import exception
import employee
import service
import timetable
import client

def main_menu():
    print('\nИнформационная система БарберШоп')
    print('\nВыберите опцию:')
    print('1 - Сотрудники\n2 - Услуги\n3 - Запись на приём\n4 - Расписание\n5 - Провести счёт\n0 - Выйти из программы')
    data = input()
    if exception.data_menu(data, 5):
        return int(data)
    print('\nОшибка ввода!')
    return main_menu()


def sub_menu_1_2():
    print('\nВыберите опцию:')
    print('1 - Добавить\n2 - Удалить\n3 - Вывести на экран\n0 - Выйти в главное меню')
    data = input()
    if exception.data_menu(data, 3):
        return int(data)
    print('\nОшибка ввода!')
    return main_menu()


def data_print():
    print('\n0 - Выйти в предыдущее меню')
    data = input()
    if exception.data_menu(data, 0):
        return int(data)
    print('\nОшибка ввода!')
    return main_menu()


def employee_data_add(num):
    if num == 0:
        return input('\nВведите ФИО: ')
    if num == 1:
        return print('\nСотрудник успешно добавлен.')


def employee_data_delete(num):
    if num == 0:
        employee.print_empl()
        print('\nВыберите сотрудника: ')
        data = input()
        if exception.data_emp(data):
            return data
        print('\nОшибка ввода!')
        return employee_data_delete(num)
    if num == 1:
        return print('\nСотрудник успешно удалён.')


def service_data_add(num):
    if num == 0:
        return input('\nВведите название услуги: ')
    if num == 1:
        return input('\nВведите стоимость услуги: ')
    if num == 2:
        return print('\nУслуга успешно добавлена.')


def service_data_delete(num):
    if num == 0:
        service.print_ser()
        print('\nВыберите услугу: ')
        data = input()
        if exception.data_ser(data):
            return data
        print('\nОшибка ввода!')
        return service_data_delete(num)
    if num == 1:
        return print('\nУслуга успешно удалёна.')


def client_data_add(new_empl, num):
    if num == 0:
        employee.print_empl()
        print('\nВыберите сотрудника: ')
        data = input()
        if exception.data_emp(data):
            return data
        print('\nОшибка ввода!')
        return client_data_add(new_empl, num)
    if num == 1:
        timetable.print_tt(new_empl)
        print('\nВыберите время (чч:мм): ')
        data = input()
        if exception.data_tt(new_empl,data):
            return data
        print('\nОшибка ввода!')
        return client_data_add(new_empl, num)
    if num == 2:
        return input('\nВведите имя клиента: ')
    if num == 3:
        service.print_ser()
        print('\nВыберите услугу: ')
        data = input()
        if exception.data_ser(data):
            return data
        print('\nОшибка ввода!')
        return client_data_add(new_empl, num)
    if num == 4:
        return print('\nЗапись успешно добавлена.')


def client_data_delete(num):
    if num == 0:
        client.print_client()
        print('\nВыберите клиента: ')
        data = input()
        if exception.data_client(data):
            return data
        print('\nОшибка ввода!')
        return client_data_delete(num)
    if num == 1:
        return print('\nЗапись успешно удалёна.')


def client_data_print():
    print('\nВведите имя клиента: ')
    data = input()
    if exception.data_client_show(data):
        return data
    print('\nКлиент не найден.')
    return 0

def receipt_data(line, num):
    if num ==0:
        client.print_client()
        print('\nВыберите клиента: ')
        data = input()
        if exception.data_client(data):
            return data
        print('\nОшибка ввода!')
        return receipt_data(line, num)
    if num == 1:
        print(f'\n{line[3]} - {line[5]} рублей.')
    if num == 2:
        print('\nПровести? (да - 1, нет - 0): ')
        data = input()
        if exception.data_menu(data, 1):
            return int(data)
        print('\nОшибка ввода!')
        return receipt_data(line, num)
    if num == 3:
        return print('\nСчёт успешно проведён.')
