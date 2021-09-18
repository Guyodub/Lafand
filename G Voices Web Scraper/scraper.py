import requests
from bs4 import BeautifulSoup
import xlrd


# en_url= "https://globalvoices.org/2021/05/28/trinidad-and-tobago-edges-closer-to-amending-its-equal-opportunity-act-to-include-sexual-orientation/"
# sw_url = "https://sw.globalvoices.org/2021/05/trinidad-na-tobago-yakaribia-kurekebisha-sheria-ya-fursa-sawa-kutambua-ushoga/"


excel_file = "../Corpus_links.xlsx"

sw_file = open("swahili.sw","a", encoding = "utf-8")
en_file = open("english.en","a", encoding = "utf-8")

def scrap_text(url):
    r1 = requests.get(url)
    mypage = r1.content

    soup1 = BeautifulSoup(mypage, "html.parser")
    article = soup1.find_all('div', class_='entry full-post-content')

    txt=article[0].get_text()
    print(txt)
    return txt

def write_to_file(sw_text,en_text):
    sw_file.write(sw_text)
    en_file.write(en_text)

def read_from_spreadsheet(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    sheet = workbook.sheet_by_index(0)

    for i in range(1,sheet.nrows):
        sw_url = sheet.cell_value(i, 0)
        en_url = sheet.cell_value(i, 1)

        sw_text = scrap_text(sw_url)
        en_text = scrap_text(en_url)

        write_to_file(sw_text,en_text)

read_from_spreadsheet(excel_file)
