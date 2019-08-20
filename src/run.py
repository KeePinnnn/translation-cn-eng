from excel.data import file_info
from scrape.trans import scrap

if __name__ == "__main__":
    f = file_info()
    f.set_file_path("translation.xlsx")
    f.read_data()

    list_cn = f.read_col_en("English", "Chinese")
    s = scrap(list_cn)

    dict_en = s.get_content()
    print(dict_en)
    f.write_data_en(dict_en, "English", "Chinese")

