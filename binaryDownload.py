#모듈 읽기
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽는다
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")

output = target.read()
print(output)

5,477,700,000,000