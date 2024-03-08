import datetime as dt
import time as t


def div():
    print("---------------------------------")


'''output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)  # 15칸 만들기
output_c = "{:+15f}".format(52.273)  # 15칸에 부호 추가하기
output_d = "{:+015f}".format(52.273)  # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)

output_1 = "{:15.1f}".format(52.273)  # 소수점 첫째자리
output_2 = "{:15.2f}".format(52.273)  # 소수점 둘째자리
output_3 = "{:15.3f}".format(52.273)  # 소수점 셋째자리

print(output_1)
print(output_2)
print(output_3)

a = "Hello Python Programming...!"
print(a.upper())
print(a.lower())

b = " ffkkkkkkkkkk "

print(b)
print(b.strip())
print(b.lstrip())
print(b.rstrip())

print(b.isalnum())  # 알파벳 또는 숫자인지 확인
print(b.isalpha())  # 알파벳으로만 되어있는지
print(b.isidentifier())  # 식별자로 사용할 수 있는지
print(b.isdecimal())  # 문자열이 정수형태인지
print(b.isdigit())  # 문자열이 숫자인지
print(b.isspace())  # 공백이 포함됐는지
print(b.isupper())  # 대문자인지
print(b.islower())  # 소문자인지

output_e = "안녕안녕하세요".find("안녕")  # 왼쪽부터 찾아서 처음등장하는 위치 찾음
print(output_e)

output_f = "안녕안녕하세요".rfind("안녕")  # 오른쪽부터 찾아서 처음 등장하는 위치 찾음
print(output_f)

print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

a = "10 20 30 40 50".split(" ")
print(a)

print(True)
print(False)

print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

print("가방" == "가방")
print("가방" != "하마")
print("가방" < "하마")
print("가방" > "하마")

print(not True)
print(not False)

x = 10
under_20 = x < 20
print("under_20:", under_20)
print("under_20:", not under_20)

if True:
    print("True입니다..!")
    print("정말 True입니다..!")

number = input("정수 입력 > ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다.")

# 음수 조건
if number < 0:
    print("음수입니다.")

# 0 조건
if number == 0:
    print("0입니다.")
'''

now = dt.datetime.now()

'''print(now,"현재")
print(now.year,"년")
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year, now.month, now.day, now.hour, now.minute, now.second))

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))

# ------------------------------------------------------------------------

if 3 <= now.month <= 5:
    print("이번달은 {}월로 봄입니다.".format(now.month))

if 6 <= now.month <= 8:
    print("이번달은 {}월로 여름입니다.".format(now.month))

if 9 <= now.month <= 11:
    print("이번달은 {}월로 가을입니다.".format(now.month))

if 12 and 1 <= now.month <= 2:
    print("이번달은 {}월로 겨울입니다.".format(now.month))

number = input("정수 입력 > ")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

print(last_number)

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수입니다.")
    
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9 :
    print("홀수입니다.")
    


'''
'''
number = input("정수 입력 > ")
last_character = number[-1]

# 짝수 조건
if last_character in "02468":
    print("짝수입니다.")

# 홀수 조건
if last_character in "13579":
    print("홀수입니다.")

if number % 2 == 0:
    print("짝수입니다.")

else :
    print("홀수입니다.")


if 3 <= now.month <= 5:
    print("이번달은 {}월로 봄입니다.".format(now.month))

elif 6 <= now.month <= 8:
    print("이번달은 {}월로 여름입니다.".format(now.month))

elif 9 <= now.month <= 11:
    print("이번달은 {}월로 가을입니다.".format(now.month))
else:
    print("이번달은 {}월로 겨울입니다.".format(now.month))


score = float(input("학점 입력 > "))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")

elif 3.5 <= score:
    print("현 체제의 수호자")

elif 2.8 <= score:
    print("일반인")

elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")

elif 1.75 <= score:
    print("오락문화의 선구자")

elif 1.0 <= score:
    print("불가촉천민")

elif 0.5 <= score:
    print("자벌레")

elif 0 < score:
    print("플랑크톤")

else:
    print("시대를 앞서가는 혁명의 씨앗")


number = input("정수 입력 > ")
number = int(number)

if number > 0:
    # 양수일 때 : 아직 미구현 상태입니다.
    pass
else:
    # 음수일 때 : 아직 미구현 상태입니다.
    pass


list_a =[273, 32, 103, "문자열", True, False]

print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])
print(list_a[3])
print(list_a[3][0])

list_a[0] = "변경"
print(list_a)

list_a = [[1,2,3], [4,5,6], [7,8,9]]
print(list_a[2][1])

list_a =[1,2,3]
list_b = [4,5,6]

print("# 리스트")
print("list_a = ",list_a)
print("list_b = ",list_b)
print()

# 기본 연산자
print("list_a + list_b =",list_a + list_b)
print("list_a * 3",list_a * 3)

# 함수 
print("# 길이 구하기")
print("len(list_a) =",len(list_a))

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

list_a.extend([7,8,9])
print(list_a)

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)
print("pop(2):", list_a)

list_b = [0,1,2,3,4,5,6]
del list_b[3:6]
print(list_b)

list_c = [1,2,1,2]
list_c.remove(2)
print(list_c)
list_c.remove(2)
print(list_c)

list_a =[273, 32, 103, 57, 52]
print(273 in list_a)
print(99 in list_a)
print(100 in list_a)
print(52 in list_a)

array = [273, 32, 103, 57, 52]

for element in array:
    # 출력합니다
    print(element)
 
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print("100 이상의 수:",number)

list_of_list =[
    [1,2,3],
    [4,5,6,7,],
    [8,9],
]

for i in list_of_list:
    for j in i:
        print(j)

# 딕셔너리 예
변수명 = {
    "키":"값",
}

dict_a ={
    "name": "어벤져스 엔드게임",
    "type": "히어로 무비"
}


print(dict_a)
print(dict_a["name"])
print(dict_a["type"])
div()

dict_b ={
    "director":["안소니 루소","조 루소"],
    "cast":["아이언맨","타노스","토르","닥터스트레인지","헐크"]
}
print(dict_b["director"])
print(dict_b["cast"])

dictionary ={
    "name":"7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

print("name:",dictionary["name"])
print("type:",dictionary["type"])
print("ingredient:",dictionary["ingredient"])
print("origin:",dictionary["origin"])
div()

dictionary["name"]="8D 건조 망고"
print("name:",dictionary["name"])

dictionary["ingredient"][1] ="설탕"
print(dictionary["ingredient"])

div()

name ="이름"

dict_key={
    name:"7D 건조 망고",
    type:"당절임"
}

print(dict_key)
dict_key[name]="바꾼 망고"
print(dict_key)

div()

dictionary1={
    "name":"7D 건조 망고",
    "type":"당절임"
}

#요소 제거 전에 내용을 출력해 봅니다.
print("요소 제거 이전: ",dictionary1)

#딕셔너리의 요소 제거
del dictionary1["name"]
del dictionary1["type"]

#요소 제거 후
print("요소 제거 이후 ",dictionary1)

dictionary2 ={
    "name":"7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

# 사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")

# 사용자로부터 입력을 받습니다.
if key in dictionary2:
    print(dictionary2[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

dictionary3 ={
    "name":"7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

# 존재하지 않는 키에 접근해 봅니다.
value = dictionary3.get("존재하지 않는키")
print("값: ",value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
'''
'''

# 내부에 들어있는 숫자가 몇번 등장하는지 출력하는 코드를 작성하세요.
    
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,8,7,2,3]
counter ={}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)
div()
character = {
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀 플레이트",
    },
    "skill":
        ["베기","세게 베기","아주 세게 베기"]
}
for key in character:
    if type(character[key]) is str:
        print("{} : {}".format(key, character[key]))
    elif type(character[key]) is int:
        print("{} : {}".format(key, character[key]))
    elif type(character[key]) is dict:
        for items in character[key]:
            print("{} : {}".format(items,character[key][items]))
    elif type(character[key]) is list:
        for skill in character[key]:
            print("{} : {}".format(key, skill))
div()

a = range(5)
print(a)
div()
list(range(5,10))
print(list(range(5,10)))
div()
list(range(0,10,2))
print(list(range(0,10,2)))
div()
a = range(0,10+1) # 10까지 포함할것을 강조할때 +1
list(a)
print(list(a))
div()
for i in range(5):
    print(str(i)+"=반복변수")
div()

for i in range(5,10):
    print(str(i)+"=반복변수")
div()

for i in range(0,10,3):
    print(str(i)+"=반복변수")
div()

array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
div()

#역반복문
for i in range(4,0-1,-1):
    #출력
    print("현재 반복 변수: {}".format(i))
div()

list2 = [1,2,3,4,5,6,7,8,9]

for i in reversed(range(len(list2))):
    print("{}".format(i))
'''
'''
# while

while True:
    print(".",end="")
'''
'''
i = 0

while i<10:
    print("{}번 반복함 ㅎㅎ".format(i))
    i +=1 

# 변수를 선언합니다.
list_test=[1,2,1,2]
value = 2

#list_test 내부에 value 가 있다면 반복
while value in list_test:
    list_test.remove(value)

print(list_test)


number = 0

target_tick = t.time() + 5
while t.time() < target_tick:
    number += 1

# 출력
print("5초 동안 {}번 반복했습니다.".format(number))

i = 0

#무한 반복합니다.
while True:
    # 몇번째 반복인지 출력합니다.
    print("{}번째 반복문입니다.".format(i))
    i = i + 1
    # 반복을 종료합니다.
    input_text=input("> 종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break

num = [5,15,6,20,7,25]

#반복을 돌립니다
for number in num:
    if number < 10:
        continue
    print(number)

'''
key_list = ["name", "hp","mp","level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

# 최종 출력
print(character)


