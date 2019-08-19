import pandas as pd

from config import FILE_PATH

class file_info():
    def __init__(self):
        self.file_path = FILE_PATH

    def set_file_path(self, file_name:str):
        self.file = self.file_path + file_name
        return "set file path as " + self.file

    def read_data(self):
        self.data = pd.ExcelFile(self.file)
        self.df = self.data.parse("Sheet1")
        return self.df

    def write_data_en(self, data:object, title:str):
        if type(data) is list:
            # TODO
            # add in col and row to allow the data to be written in 
            # from center
            self.df.loc[ : , title] = data

            self.df.to_excel(self.file, sheet_name="Sheet1", index=False)
            print("data has been write into f{self.file}")
        else:
            return "data should be in list format"

    def extract_col(self, col:str):
        return self.df[col].tolist()