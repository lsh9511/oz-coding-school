import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요: ")

url = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keyword}"

req = requests.get(url)
html = req.text

soup = BeautifulSoup(html, "html.parser") # B 대문자 = 클래스
#print(soup)

'''
스크래핑시 고려사항
1. 사이트 분석 -> 안되면 고생함.
'''
result = soup.select(".view_wrap") # select_one = 가장 처음 발견되는 클래스 명만 찾아서 가져온다.

for i in result:
    ad = i.select_one(".link_ad")

    if ad :
        pass
    else:
        title = i.select_one(".title_link").text
        link = i.select_one(".title_link")['href']
        writer = i.select_one(".name").text
        dsc = i.select_one(".dsc_link").text

        print(f'작성자 : {writer}')
        print(f'링크 : {link}')
        print(f'제목 : {title}')
        print(f'요약글 :{dsc}')
        print()

# select -> list와 동일한 형태의 데이터 타입으로 모든 정보를 가져옵니다.