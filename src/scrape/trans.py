import string
import requests
import re

from bs4 import BeautifulSoup 

class scrap():
    def __init__(self, list_cn:list):
        self.exclude = set(string.punctuation)
        self.list_cn = list_cn
        self.pattern = re.compile('^[a-zA-Z ]+$')

    def get_content(self):
        list_en = []
        for each in self.list_cn:
            page = requests.get("https://www.youdao.com/w/" + each + "/#keyfrom=dict2.top")

            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                word_group = soup.findAll("span", {"class": "contentTitle"})
                sub_list = list(filter(self.pattern.search, [x.get_text() for x in word_group]))
                sub_list = map(lambda x: x.strip(), sub_list)
                str_list = ', '.join(str(x) for x in sub_list)

                list_en.append(str_list)

            else:
                print("word does not exist in website")
                list_en.append("")
        
        return list_en