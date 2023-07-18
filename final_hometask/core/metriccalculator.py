from .dataentry import DataEntry
from uuid import uuid4


class MetricCalculator:

    def __init__(self, all_indexes: DataEntry):
        self.all_indexes = all_indexes
        self.all_data = self.all_indexes.all_data

    def indx_column(self, column_name: str) -> dict:
        new_index = dict()
        for data_entry in self.all_data:
            if data_entry[column_name] not in new_index:
                new_index[data_entry[column_name]] = list()
            new_index[data_entry[column_name]].append(data_entry)
        return new_index

    def first_metric(self, key_index="sale"):
        unique_uuid_index = dict()
        data_csv = self.all_data
        for _id, row in enumerate(data_csv):
            unique_uuid_index[uuid4()] = row
        list_1 = list()
        list_2 = list()
        for key1_2, value1_2 in unique_uuid_index.items():
            for key2_2, value2 in value1_2.items():
                if value2 == key_index:
                    list_1.append(key1_2)
                    list_2.append(float(unique_uuid_index[key1_2]['operation_cost']))
        result = sum(list_2)
        return result

