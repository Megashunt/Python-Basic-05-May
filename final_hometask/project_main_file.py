from core import CSVProcessor, FileProcessor, DataEntry, JSONProcessor, MetricCalculator

if __name__ == '__main__':
    # путь к файлам
    user_input = r'/Users/advakhov/Рабочая папка /PyCharm/final_hometask/core/SKU/'
    # инициализация CSVProcessor
    collect_csv_data = CSVProcessor(user_input)
    # собираем все данные в список
    list_csv = collect_csv_data.all_csv_data_list()
    # инициализация JSONProcessor
    collect_json_data = JSONProcessor(user_input)
    # собираем все данные в список
    list_json = collect_json_data.all_csv_data_list()
    # объединяем данные
    FileProcessor.data_entry_list = list_csv + list_json
    # инициализируем класс DataEntry
    transfer_data = DataEntry(FileProcessor.data_entry_list)
    # инициализируем класс MetricCalculator
    metric_calc = MetricCalculator(transfer_data)

    print("Створіть індекси:")
    # выводим индекс в зависимости от колонки
    x = 'sku'  # or warehouse or operation
    task_1 = metric_calc.indx_column(x)
    for key, value in task_1.items():
        print(key, ':', value)

    print("прибуток від усіх операцій типу sale (сума колонки operation_cost де колонка operation == 'sale')")
    first_metric = metric_calc.first_metric()
    print(f'Прибыль {first_metric} UAH')
    print(len(FileProcessor.data_entry_list))
