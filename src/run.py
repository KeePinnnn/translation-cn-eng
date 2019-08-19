from excel.data import file_info
from scrape.trans import scrap

if __name__ == "__main__":
    f = file_info()
    f.set_file_path("translation.xlsx")
    f.read_data()

    list_cn = f.extract_col("Chinese")
    s = scrap(list_cn)

    list_en = s.get_content()
    f.write_data_en(list_en, "English")

