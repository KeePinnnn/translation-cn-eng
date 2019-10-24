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

    def write_data_en(self, data:object, target_title:str, given_title:str):
        if type(data) is dict:
            for key, value in data.items():
                print(key)
                index = self.df.index[self.df[given_title] == key][0]
                self.df.loc[index, target_title] = value

            self.df.to_excel(self.file, sheet_name="Sheet1", index=False)
            print(f"data has been write into {self.file}")
        else:
            return "data should be in list format"

    def extract_col(self, col:str):
        return self.df[col].tolist()

    def read_col_en(self, target_col:str, given_col:str):
        self.df_nan = self.df.loc[self.df.English.isnull()]
        return self.df_nan[given_col].tolist()