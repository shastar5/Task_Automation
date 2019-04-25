from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlsxwriter as xw

# Defining every needed global variables
link = "https://movie.naver.com/movie/bi/mi/basic.nhn?code="
idx = 100000
reallink = ""
reallink = link+idx.__str__()

# Assign soup a document
soup = BeautifulSoup(urlopen(reallink), "html.parser")

# Defining excel object
workbook = xw.Workbook('movie.xlsx')
worksheet = workbook.add_worksheet()

"""제목 뽑기"""
def find_title():
    title = soup.find("h3", "h_movie")
    print(title.a.text)
    return title.a.text

"""영화 내용 뽑기인데, 문제점이 있지.다른 영화면..? ex) 배우가 더 많다던가..
content = soup.find_all("dd")
for hit in content:
    print(hit.text)
"""

def find_content():
    temp = []
    content = soup.find_all({"dl" : 'span'})

    for tag in content:
        hit = tag.dd.get_text(" ",strip=True);
        temp.append(hit)
        print(hit)
    return temp

workbook.close()