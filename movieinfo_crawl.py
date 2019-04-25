from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlsxwriter as xw

# Defining every needed global variables
link = "https://movie.naver.com/movie/bi/mi/basic.nhn?code="
start_idx = 100000
end_idx = 100100

# Defining excel object
workbook = xw.Workbook('movie.xlsx')
worksheet = workbook.add_worksheet()

"""제목 뽑기"""
def find_title(soup):
    title = soup.find("h3", "h_movie")
    print(title.a.text)
    return title.a.text

"""영화 내용 뽑기인데, 문제점이 있지.다른 영화면..? ex) 배우가 더 많다던가..
content = soup.find_all("dd")
for hit in content:
    print(hit.text)
"""

def find_content(soup):
    temp = []
    content = soup.findAll({"dl" : 'span'})

    for tag in content:
        try:
            hit = tag.dd.get_text(" ",strip=True)
            print(hit)
            temp.append(hit)
        except Exception as e:
            break
    return temp

def crawl(row, start, end):
    for i in range(start, end):
        crawl_link = link + i.__str__()

        # Assign soup a document
        soup = BeautifulSoup(urlopen(crawl_link), "html.parser")

        # Run function
        try:
            title = find_title(soup)
            content = find_content(soup)
            worksheet.write(row, 0, str(title))
            worksheet.write(row, 1, str(content))
            row = row + 1

        except Exception as e:
            print(e)
            crawl(row+1,i+1, end)
            break

row = 0

crawl(row, start_idx, end_idx)

workbook.close()