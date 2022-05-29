from xml.etree.ElementTree import parse
import pandas as pd
from config import get_secret
from requests import get
from zipfile import ZipFile
from openpyxl.workbook import Workbook


OPEN_DART_API = get_secret("OPEN_DART_API")


def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


if __name__ == '__main__':
    url = "https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={0}".format(
        OPEN_DART_API)
    download(url, "./codes/codes.zip")

with ZipFile('./codes/codes.zip', 'r') as zipObj:
    # Extract all the contents of zip file in current directory
    zipObj.extractall()

# 2단계 xml 파일 읽고 엑셀로 저장
tree = parse('CORPCODE.xml')
root = tree.getroot()
kids = root.getchildren()

data = []
for child in kids:
    if child.tag == "list":
        temp = []
        for i in child:
            temp.append(i.text)
        data.append(temp)

고유번호 = []
회사이름 = []
종목코드 = []
변경일 = []

for i in data:
    고유번호.append(i[0])
    회사이름.append(i[1])
    종목코드.append(i[2])
    변경일.append(i[3])
df = pd.DataFrame({"고유번호": 고유번호, "회사이름": 회사이름, "종목코드": 종목코드, "변경일": 변경일})
df.to_excel("./result_files/회사고유번호.xlsx")
