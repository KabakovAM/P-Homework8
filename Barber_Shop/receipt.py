import csv
import user_interface
import controller
import timetable
import client

client_csv = 'client.csv'
receipt_csv = 'receipt.csv'
receipt_id_csv = 'receipt_id.csv'


def receipt_data():
    newrow = []
    oldrows = []
    old = user_interface.receipt_data(newrow, 0)
    with open(client_csv, 'r', encoding='utf-8') as inp:
        data = csv.reader(inp)
        for line in data:
            if line[0]==old:
                newrow = line
            else:
                oldrows.append(line)
    user_interface.receipt_data(newrow, 1)
    num = user_interface.receipt_data(newrow, 2)
    if num == 0:
        return controller.click_button_main()
    else:
        user_interface.receipt_data(newrow, 3)
        timetable.tt_data_delete(newrow)
        with open(receipt_id_csv, 'r', encoding='utf-8') as inp:
            data = csv.reader(inp)
            for line in data:
                global_id = int(*line)
                newrow.insert(0, global_id)
        with open(receipt_csv, 'a', encoding='utf-8') as out:
            data = csv.writer(out, lineterminator='\n')
            data.writerow(newrow)
        with open(receipt_id_csv, 'w', encoding='utf-8') as out:
            data = csv.writer(out, lineterminator='\n')
            data.writerow([global_id+1])
        with open(client_csv, 'w', encoding='utf-8') as out:
            data = csv.writer(out, lineterminator='\n')
            for line in oldrows:
                data.writerow(line)
        return controller.click_button_main()