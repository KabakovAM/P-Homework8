import user_interface
import employee
import service
import client
import timetable
import receipt


def click_button_main():
    num_1 = user_interface.main_menu()
    if num_1 == 0:
        return
    if num_1 == 1:
        return click_button_1()
    if num_1 == 2:
        return click_button_2()
    if num_1 == 3:
        return click_button_3()
    if num_1 == 4:
        return timetable.show()
    if num_1 == 5:
        return receipt.receipt_data()
    

def click_button_1():
    num_2 = user_interface.sub_menu_1_2()
    if num_2 == 0:
        return click_button_main()
    if num_2 == 1:
        return employee.employee_data_add()
    if num_2 == 2:
        return employee.employee_data_delete()
    if num_2 == 3:
        return employee.employee_data_print()


def click_button_2():
    num_2 = user_interface.sub_menu_1_2()
    if num_2 == 0:
        return click_button_main()
    if num_2 == 1:
        return service.service_data_add()
    if num_2 == 2:
        return service.service_data_delete()
    if num_2 == 3:
        return service.service_data_print()

def click_button_3():
    num_2 = user_interface.sub_menu_1_2()
    if num_2 == 0:
        return click_button_main()
    if num_2 == 1:
        return client.client_data_add()
    if num_2 == 2:
        return client.client_data_delete()
    if num_2 == 3:
        return client.client_data_print()
    