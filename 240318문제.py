import random as r
'''print("%10s %10d %10.3f" % ('dog', 127, 1.234))
print("{:>10s} {:>10d} {:>10.3f}".format('dog', 127, 1.234))

L = int(input("L 판매 개수 >> "))
M = int(input("M 판매 개수 >> "))
S = int(input("S 판매 개수 >> "))

sumL = 2500 * L
sumM = 1000 * M
sumS = 5000 * S
sum = sumL + sumM + sumS
print(f"오늘의 총 매출은 {sum}원 입니다.")

#음수 인덱스 이용하여 문자열 변수 a 에서 Diem을 슬라이싱
a = "Carpe Diem!"
#  0 1 2 3 4 5 6 7 8 9 10
# -9 -8 -7 -6 -5 -4 -3 -2 -1
print(a[-5:-1])
print(a[6:-1])
#문자열 변수 a 에서 Carpe을 슬라이싱
print(a[0:5])
''''''
for i in range(0, 6 , 2):
    # 빈칸
    for j in range(6 - i - 1):        
        print("-", end='')
    # 별
    for j in range(i + 1):        
        print("*", end='')
    print()

for i in range(1, 5, 2):
    # 빈칸            
    print("-" * i, end='')
    for j in range(5 - i - 1):        
        print("*", end='')
    print()


for i in range(1, 4):
    # print(" " *  (3 - i), end='')
    for j in range(3-i):
        print(" ",end='')# 2 1 0
    #print("*" * (2 * i - 1))
    for k in range(2 * i - 1):
        print("*", end = "") # 1 3 5 7 9
    print()

for i in range(2, 0, -1):
    # print(" " *  (3 - i), end='')
    for j in range(3-i):
        print(" " , end='') # 1 2
    #print("*" * (2 * i - 1))
    for k in range(2 * i - 1):
        print("*", end='') # 1 3 5 7 9
    print()

a =145
b =151
c = 149

print(a <= 140 and b <=140 and c <= 140)


y = int(input("연도를 입력하세요 >> "))
if (y % 4 ==0 and y % 100 != 0) or y % 400 == 0 :
    print("leap year")
else:
    print("common year")

print("===== menu ====")
print("1. burger")
print("2. sandwitch")
print("3. Hotdog")
print("4. coke")
print("5. milk")
menu = int(input("메뉴를 입력하세요 >> "))

if menu == 1:
    print("'Burgers are not available.'")
elif menu == 2 or 3:
    print("'What would you like to drink?'")
elif menu == 4:
    print("'I like coke, too.'")
elif menu == 5:
    print("'would you like hot or cold?'")
else:
    print("'Not menu.'")



listA = ["가위", "바위","보"]
user = int(input("가위 : 1, 바위 : 2, 보 : 3 >> "))
com = r.randint(1, 3)

if user > com :
    print("Com({}) : User({})".format(listA[com-1], listA[user-1]))
    print("User win!")
elif user < com :
    print("Com({}) : User({})".format(listA[com-1], listA[user-1]))
    print("User lose!")
elif user == com :
    print("Com({}) : User({})".format(listA[com-1], listA[user-1]))
    print("Draw!")


listB = ['월','화','수','목','금','토','일']

i = r.randint(0,6)
print(listB[i])

a = ['fun','fun','python']
s = ", ".join(a) # 문자열로
print(s) 
print(s.split(",")) # 리스트로

a ="간장공장공장장"
print(a.count("공장"))
print(a.find("공장"))


listC =['c','e','a','d','b']
listC.sort()
print(listC)
listC.pop()
print(listC)

n = 1
while n <= 20:
    if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
        print('X', end='')
    else:
        print(n,end='')
    n+=1

n = int(input("정수를 입력하세요 >> "))
for i in range(n):
    for j in range(n-i):
        print(" ",end='')
    for k in range(2 * i - 1):
        print("*", end = "")
    print()

for i in range(n):
    print(" "*(n-i), end= '')
    print("*"*(2 * i - 1))




def area(radius):
    return radius * radius * 3.14

n = int(input("반지름을 입력하세요 >> "))
print(area(n))


def getSum(n):
    sum = 0
    for i in range(1, n+1):
        print(">> ", i)
        sum += i
    return sum

print("sum: ",getSum(n))

def getMax(n):
    listA = []
    for _ in range(n):
        n = int(input(">> "))
        listA.append(n)   
    print("입력한 수의 리스트",listA)
    return max(listA)

n = int(input("n : "))
print(f"{n}개의 숫자를 리스트에 입력합니다. {n}개의 숫자를 입력하세요.")
print("가장 큰 수 >> ",getMax(n))



import math 

def rec():
    width = int(input("width >> "))
    height = int(input("height >> "))
    
    area = width * height
    return area

def tri():
    width = int(input("width >> "))
    height = int(input("height >> "))
    
    area = width * height /2
    return area

def circle():
    radius = int(input("radius >> "))

    area = radius ** 2 * 3.14
    return area

print("=== 넓이를 구할 도형을 선택하세요 ===")
print("1. 사각형의 넓이구하기\n2. 삼각형의 넓이구하기\n3. 원의 넓이구하기\n-1.종료하기")
while True:
    n = int(input("도형 번호 입력 >> "))

    if n == 1:
        print("사각형의 넓이 : ", rec(),end="\n")
    elif n == 2:
        print("삼각형의 넓이 : ", tri(),end="\n")
    elif n == 3:
        print("원의 넓이 : ", circle(),end="\n")
    elif n == -1:
        print("프로그램을 종료합니다.")
        break

    else:
        print("1, 2, 3 중 하나를 입력해주세요.", end="\n")



def Login(id, password):
    # 로그인 1, 2, 3, 4 반환

    idValue = "Cube"
    passwordValue = '1234'

    result = 0
    if id == idValue and password == passwordValue:
        return 1

    elif id == idValue and password != passwordValue:
        return 2

    elif id != idValue and password == passwordValue:
        return 3

    elif id != idValue and password != passwordValue:
        return 4


def Say(result):
    # 로그인 결과 반환
    if result == 1:
        return "Login Success !!"
    elif result == 2:
        return "Please check your Password"
    elif result == 3:
        return "Please check your ID"
    elif result == 4:
        return "Please check your ID and Password"


id = input("아이디를 입력하세요. >> ")
password = input("패스워드를 입력하세요. >> ")

print(Say(Login(id, password)))

# w = write, r = read, a = append
# 파일 열기
file = open("profile.txt", "w")

# 파일에 텍스트를 씁니다.
Name = input("Name >> ")
Age = input("Age >> ")
School = input("School >> ")

file.write("Name : " + Name + "\n")
file.write("Age : " + Age + "\n")
file.write("School : " + School + "\n")

# 파일 닫기
file.close()
'''

file = open("profile.txt", "r")
lines = file.readlines()
print(lines[2])
file.close()

for line in lines:
    dict={} # 파일에 들어있는걸 담을 딕셔너리
    data = line.split(':') # : 를 기준으로 데이터를 스플릿
    key = data[0].strip() # data에 split한 데이터의 [0]을 key 로 저장 ["name":"이름"]
    value = data[1].strip() #data에 split한 데이터의 [1]을 value 로 저장
    dict[key]=value
    print(dict)
    print("Key : ",data[0])
    print("Value : ", data[1]) 
    
print(dict["School"])
