class FileProcessor:

    def __init__(self, path: str):
        self.path = path
        self.filepaths = None
        self.data_entry_list = None

    def all_csv_data_list(self):
        raise NotImplementedError

    def all_csv_data_dict_unique(self):
        raise NotImplementedError
