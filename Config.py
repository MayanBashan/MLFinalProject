import pathlib




class Config:
    def __init__(self, data_set_prefix):
        self.data_set_folder_path = ".\\DataSets"
        self.csv_files_names = self.read_data_sets_folder(data_set_prefix)

    def read_data_sets_folder(self, data_set_prefix):
        return list(pathlib.Path(self.data_set_folder_path).glob(f"{data_set_prefix}*"))
