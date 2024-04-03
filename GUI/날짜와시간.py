from PyQt5.QtCore import * 

# 클래스 메소드 : 객체 생성 안해도 호출 가능한 메소드
dateTime = QDateTime.currentDateTime()
print(dateTime)
print(dateTime.toString()) # 문자열로 변환
print(dateTime.toString('yyyy년 MM월 dd일, hh시 mm분 ss초'))
# print(dateTime.toString())