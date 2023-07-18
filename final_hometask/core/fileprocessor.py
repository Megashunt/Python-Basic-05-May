class FileProcessor:
    """
    Класс родитель который принмает директорию файлов
    """

    def __init__(self, path: str):
        self.path = path
        self.filepaths = None
        self.data_entry_list = None

    def all_data_list(self):
        raise NotImplementedError


