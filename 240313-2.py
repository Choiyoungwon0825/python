import math as m
import random as r
import os
import datetime as dt
import time as t
'''
print(m.sin(30))

print("- random(): ", r.random)
print("- uniform(10,20): ",r.uniform(10,20))
print("- randrange(10)",r.randrange(10))


print("- choice([1,2,3,4,5]): ", r.choice([1,2,3,4,5]))


#기본 정보 출력
print("현재 운영체제: ", os.name)
print("현재 폴더: ",os.getcwd())
print("현재 폴더 내부의 요소: ",os.listdir())

#폴더를 만들고 제거합니다
os.mkdir("hello")
os.rmdir("hello")

#파일 생성 + 파일 이름변경
with open("origin.txt","w") as file:
    file.write("hello")
os.rename("origin.txt","new.txt")

# 파일 제거

os.remove("new.txt")
# os.unlink("new.txt")

#시스템 명령어 실행
os.system("dir")


now = dt.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after = now + dt.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1,)

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print()

# 특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year+1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
'''

print("시공간 붕괴")
t.sleep(1)
print()
for i in reversed(range(1, 6)):
    print("{}초".format(i)+("." * i))
    t.sleep(1)

print()
t.sleep(1)
print("깡!")

'''
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시: ",location.select_one("city").string)
    print("날씨: ",location.select_one("wf").string)
    print("최저기온: ",location.select_one("tmn").string)
    print("도시: ",location.select_one("tmx").string)
    print()
    '''