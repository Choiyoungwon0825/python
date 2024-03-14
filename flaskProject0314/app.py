# 모듈을 읽어 들인다.
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

#웹서버 생성
app = Flask(__name__)
@app.route('/')



def hello():
    # urlopern 함수로 기상청 전국 날씨를 읽는다
    target = request.urlopen(
        "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    # BeautifulSoup를 사용해 웹 페이지를 분석한다.
    soup = BeautifulSoup(target, "html.parser")


    output = "<div style = 'text-align : center;'><hr/>"
    # location 태그를 찾는다.
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력한다.

        output += "'<b>{}'</b> 의 날씨는 : '<b>{}</b>' 입니다.</br>".format(
            location.select_one("city").string,
            location.select_one("wf").string)
        output += "최저 / 최고기온: {}°C / {}°C".format(
                  location.select_one("tmn").string,
                  location.select_one("tmx").string,
        )
        output += "<hr/>"

        
    return output

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
