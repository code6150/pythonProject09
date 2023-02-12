from section17 import *

# try    -시도할 코드
# except -오류시. 실행 할 코드
# finally-오류가 났든 안났든 실행 할 코드
# else   -오류가 안났을 때, 실행 할 코드(except 아래에 올 수 있다.)

# class InputError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# try:
#     x = int(input('숫자를 입력하세요 >>> '))  # 숫자 아닐때 - ValueError
# except ValueError:
#     print('숫자만 입력하세요')
# except TypeError:
#     print('숫자랑 문자는 더할 수 없습니다.')
# else:
#     print('정상적인 실행')
# finally:
#     print('finally')

# try:
#     print('우리나라의 6개의 모든 도를 맞추는 퀴즈입니다람쥐. 하나씩 대답하세요.')
#     Quiz.challenge()
# except Exception as e:
#     print(e)



# url = 'https://kin.naver.com/'
# res = requests.get(url)
#
# bs = bs4.BeautifulSoup(res.text, 'html.parser')
#
# ul = bs.select_one('ul.ranking_list')
# ul2 = bs.select_one('#rankingChart > ul:nth-child(2)')
#
# title = ul.select("li > a.ranking_title")
# title2 = ul2.select("li > a.ranking_title")
#
# top

import requests
import bs4

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
res = requests.get(url)

bs = bs4.BeautifulSoup(res.text, 'html.parser')

tbody = bs.select_one('tbody')

title = tbody.select('tr')

movie = [i.text for i in title]

for i in title:
    for j in i.select('td.ac'):
        img = j.find('img')
        if img is not None:
            if img['alt'] == 'up':
                print(i.select_one('div.tit3 >  a').text)
