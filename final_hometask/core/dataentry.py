import datetime


def date_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        x = data_entry['date']
        y = datetime.datetime.strptime(x, '%d-%b-%Y')
        if data_entry['date'] not in new_index:
            new_index[y] = list()
        new_index[y].append(data_entry)
    return new_index


def time_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        x = data_entry['time']
        y = datetime.datetime.strptime(x, '%H:%M:%S')
        if data_entry['time'] not in new_index:
            new_index[y] = list()
        new_index[y].append(data_entry)
    return new_index


def sku_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        if data_entry['sku'] not in new_index:
            new_index[data_entry['sku']] = list()
        new_index[data_entry['sku']].append(data_entry)
    return new_index


def wrhs_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        if data_entry['warehouse'] not in new_index:
            new_index[data_entry['warehouse']] = list()
        new_index[data_entry['warehouse']].append(data_entry)
    return new_index


def wrhs_cell_id_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        x = int(data_entry['warehouse_cell_id'])
        if data_entry['warehouse_cell_id'] not in new_index:
            new_index[x] = list()
        new_index[x].append(data_entry)
    return new_index


def operation_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        if data_entry['operation'] not in new_index:
            new_index[data_entry['operation']] = list()
        new_index[data_entry['operation']].append(data_entry)
    return new_index


def invoice_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        if data_entry['invoice'] not in new_index:
            new_index[data_entry['invoice']] = list()
        new_index[data_entry['invoice']].append(data_entry)
    return new_index


def exp_date_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        x = data_entry['expiration_date']
        y = datetime.datetime.strptime(x, '%d-%b-%Y')
        if data_entry['expiration_date'] not in new_index:
            new_index[y] = list()
        new_index[y].append(data_entry)
    return new_index


def operation_cost_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        x = float(data_entry['operation_cost'])
        if data_entry['operation_cost'] not in new_index:
            new_index[x] = list()
        new_index[x].append(data_entry)
    return new_index


def comment_indx(all_data: list) -> dict:
    new_index = dict()
    for data_entry in all_data:
        if data_entry['comment'] not in new_index:
            new_index[data_entry['comment']] = list()
        new_index[data_entry['comment']].append(data_entry)
    return new_index


class DataEntry:

    def __init__(self, all_data: list):
        self.all_data = all_data
        self.date = date_indx(all_data)
        self.time = time_indx(all_data)
        self.sku = sku_indx(all_data)
        self.warehouse = wrhs_indx(all_data)
        self.warehouse_cell_id = wrhs_cell_id_indx(all_data)
        self.operation = operation_indx(all_data)
        self.invoice = invoice_indx(all_data)
        self.expiration_date = exp_date_indx(all_data)
        self.operation_cost = operation_cost_indx(all_data)
        self.comment = comment_indx(all_data)
