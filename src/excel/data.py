from openpyxl import load_workbook
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
            self.en_data = pd.DataFrame({title: [data]})

            for index, row in self.en_data.iterrows():
                cell = 'C%d' % (index + 2)
                self.df[cell] = row[0]

            self.wb.save(self.file)
            return "data has been save into f{self.file}"
        else:
            return "data should be in list format"

    def extract_col(self, col:str):
        return self.df[col].tolist()