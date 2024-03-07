import time as t
import keyword
import math

# print(math.pi)
# print(keyword.kwlist)
# t.sleep(0.5)
print("Hello Python Programming..")  # 문자열을 출력합니다


def calculate_rectagle_area(length, width):
    '''
    직사각형의 넓이를 계산합니다.

    Args:
        length (float): 가로 길이
        width (float): 세로 길이

    Returns:
        float: 직사각형의 넓이 
    '''
    area = length * width
    return area


print(calculate_rectagle_area(5.14, 10.0))
print("hello", "python")
print()
print("안녕하세요", "저의", "이름은", "윤인성입니다.")

print("# 하나만 출력합니다.")
print("Hello Python Programming..!")
print()
# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "윤인성입니다!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("---확인 전용선---")
print()
print()
print("---확인 전용선---")

print(type("안녕하세요"))
print(type(123.2))
print(type(True))

print("안녕하세요")
print('안녕하세요')

print("\\ㅎㅇ\\")
print("이름\t|\t나이\t|\t지역")
print("-----------------------------------------")
print("윤인성\t|\t25\t|\t강서구")
print("윤아린\t|\t24\t|\t강서구")
print("구름\t|\t3\t|\t강서구")

print("\\ \\ \\ \\")

print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산\n대한사람 대한으로길이 보전하세")
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로길이 보전하세""")

print("a", "d")
print("h"+"d"+str(10))
print("Hello", end='!')
print("world")
print("Hello", "world")
print("Hello", "world", sep=',')

print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

print("안녕하세요"[0:2])
print("안녕하세요"[1:3])
print("안녕하세요"[2:4])

print(len("안녕하세요"))

print("동해물과 백두산이\n마르고 닳도록\n\t하느님이 보우하사 \"우리나라 만세\'")
print()
print("Hello", "world", "Hi", "Python", sep='~', end='!')
print()

print("apple")
print("juice")
print("apple""juice")
print("apple", "juice")
print("apple", "juice", sep='~')
print("apple", "juice", end=' is ')
print("tasty")

a = "안녕 하세요"
print(a[2])

print("A\nB\nC\nD")

print("5 + 7 =", 5+7)
print("5 - 7 =", 5-7)
print("5 * 7 =", 5*7)
print("5 / 7 =", 5/7)
print("3 / 2 =", 3/2)
print("3 // 2 =", 3//2)
print("3 % 2 =", 3 % 2)
print("3 ** 1 =", 3 ** 1)
print("3 ** 2 =", 3 ** 2)
print("3 ** 3 =", 3 ** 3)
print("3 ** 4 =", 3 ** 4)

print(15, "+", 4, "=", 15+4)

pi = 3.14159265

print(pi)
print(pi+2)
print(pi-2)
print(pi*2)
print(pi/2)
print(pi % 2)
print(pi*pi)

r = 10
# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r)

a = 10
print(a)
a += 20
print(a)

number = 100
number += 10
number += 20
number += 30

print("number:", number)

string = "안녕하세요"
string += "!"
string += "!"
print("string :", string)
'''
string = input("인삿말을 입력하세요 > ")
print(string)
print(type(string))

'''
"""
string1 = input("입력 > ")
print("입력 + 100 :", string1+100)

stringA = input("입력 A > ")
int_a = int(stringA)

stringB = input("입력 B > ")
int_b = int(stringB)

print("문자열 자료: ", stringA + stringB)
print("숫자 자료: ", int_a+int_b)


output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

str_input = input("원의 반지름 입력 >")
num_input = int(str_input)

print("원의 둘레 : ", pi*num_input)
print("원의 넓이 : ", pi*num_input*2)

# format() 함수로 숫자를 문자열로 변환하기
string_a = "{}".format(10)

# 출력하기
print(string_a)
print(type(string_a))
"""
format_a = "{}만원".format(50000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

# 정수
output_a = "{:+d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)


print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
output_a1 = "{:+5d}".format(52)
output_a2 = "{:+5d}".format(-52)
output_a3 = "{:=+5d}".format(52)
output_a4 = "{:=+5d}".format(-52)
output_a5 = "{:+05d}".format(52)
output_a6 = "{:+05d}".format(-52)
print("-----------")
print(output_a1)
print(output_a2)
print(output_a3)
print(output_a4)
print(output_a5)
print(output_a6)
