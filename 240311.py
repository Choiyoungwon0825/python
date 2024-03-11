numbers=[103,52,273,32,77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

list_a = [1, 2, 3, 4, 5]

list_reversed = reversed(list_a)

# 출력
print("# reversed() 함수")
print("reversed(1,2,3,4,5,) = ", list_reversed)
print("list(reversed(1,2,3,4,5,)) = ", list(list_reversed))
print()

# 반복문을 적용
print("# reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-", i)

ex_list = ["요소A","요소B","요소C"]
print("단순 출력")
print(ex_list)
print()

# enumerate() 함수 사용하여 출력
print("# enumerate() 함수 사용하여 출력")
print(enumerate(ex_list))
print()

# list() 함수로 강제 변환해 출력
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(ex_list)))

#for 반복문과 enumerate() 함수를 사용하여 출력
print("반복문과 조합하기")
for i, value in enumerate(ex_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
    

ex_dict = {
    "키A":"값A",
    "키B":"값B",
    "키C":"값C"
}

# 딕셔너리의 items() 함수 결과 출력하기
print("# 딕셔너리의 items() 함수")
print("items :", ex_dict.items())
print()

# for 반복문과 items() 함수 조합하여 사용하기
print("# for 반복문과 items() 함수 조합하여 사용하기")
for key, value in ex_dict.items():
    print("dictionary[{}] : {}".format(key, value))

array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

array = [i * i for i in range(0, 20, 2)]

print(array)

array = ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

# 출력합니다 
print(output)

"{:b}".format(10)
print("{:b}".format(10))
print(int("1010",2))

print("안녕안녕하세요".count("안"))

#1~100사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드

output = [i for i in range(1,101) if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계 : ", sum(output))

print("apple", "juice", sep='~')
print("apple", "juice", end=' is ')
print("tasty")
print("%d는 정수"%4)

x, y = 10, "code"
print(f"x is {x}")
print(f"y is {y}")
print(f"x is {x}, 0000000000000000000000y is {y}")


play = input("경기종목 : ")
grade = input("학년 : ")
win = input("이긴 반 : ")
lose = input("진 반 : ")

list = [play, grade, win, lose]

print("오늘 파이썬 초등학교에서 %s 경기가 열렸습니다." % play)
print("%s 학년 %s 반과 %s 반이 치열한 경기를 펼쳤고," % (grade, win, lose))
print("%s 반이 승리하였습니다." % win)
print()
print(f"오늘 파이썬 초등학교에서 {play}경기가 열렸습니다.")
print(f"{grade} 학년 {win} 반과 {lose} 반이 치열한 경기를 펼쳤고,")
print(f"{win} 반이 승리하였습니다.")
print()
print("경기종목".format(play))

year = input("연도 : ")
month = input("월 : ")
day = input("일 : ")

print(f"오늘은 {year}년 {month}월 {day}일")
print("오늘은 %s년 %s월 %s일" % (year,month,day))
print("오늘은 {}년 {}월 {}일".format(year,month,day))

unique_numbers = []
numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11]

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

list1 =[1,2,3,4,5]
list2 =[3,4,5,6,7]

result = []

for i in list1:
    if i in list2 :
        result.append(i)

print(result)

order ={

}
while True :
    food = input("음식: ")
    if food.lower =='q':
        break
    num = int(input("수량"))

    order[food]= num
    if food in order:
        order[food] += num
    else :
        order[food] = num

print("주문내역")
for key, value in order.items():
    print("{} : {} 개".format(key, value))

order={
} # 주문을 저장할 딕셔너리

print(order.keys())

while True:
    food = input("주문할 음식을 입력하세요 (종료하려면 'q'를 입력) >> ")    
    if food == "q":
        break
    num = int(input("주문할 수량을 입력하세요 >> "))       

    if food in order: 
        # 위에서 입력한 메뉴가 존재하는 경우 음식에 + 입력한 수량을 더한다
        order[food] += num
    else : 
        # 메뉴가 없으면 존재하지 않는 경우 메뉴 추가, 입력한 수량을 추가한다.
        order[food] = num

print("주문내역: ")
for i in order.keys():
    print("{} : {} 개".format(i, order[i]))
print("=================================================")    


grades = {

}


while True:
    name = input("이름을 입력하세요 (종료하려면 'q'를 입력) >> ")
    if name.lower() == "q":
        break
    score = float(input("점수를 입력하세요 >> "))
    
    grades[name] = score

avg = sum(grades.values()) / len(grades)
max_score = max(grades.values())    

print("성적 결과")
print("평균 성적:", avg)
print("최고 성적: ", max_score)


n = int(input("숫자를 입력하세요 >> "))
i = 1

for i in range(1, 10):
    print(n*i, end=' ')
print("\n================")

i = 1
while i < 10:
    print(n*i, end=' ')
    i += 1



while True:
    n = int(input("1부터 100사이의 숫자를 입력하세요 >> "))

    if n == 50:
        print("프로그램을 종료합니다.")
        break

    elif n < 50:
        print("숫자가 너무 작습니다. 다시 입력해주세요.") 

    else: 
        print("숫자가 너무 큽니다. 다시 입력해주세요.")


for i in range(10):
    print("*", end='\n')


for i in range(1, 10):
    print("*" * i)

for i in range(1, 10):
    for j in range(i):
        print("*", end='')
    print()

for i in range(2, 10):
    print("===구구단 {}단===".format(i), end="\n")
    for j in range(1,10):
        print("{} X {} = {}".format(i, j, i * j), end="\n")

def print_3_times():
    print("안녕")
    print("안녕")
    print("안녕")

print("안녕로봇 : ")
print_3_times()


def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕", 3)

def print_n_times(n, *values):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

def print_n_times(value, n=2):
    #n번 반복합니다.
    for i in range(n):
        print(value)

print_n_times("안녕하세요",4)

def print_n_times(*values,n=2):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",5)

def print_n_times(*values,n=2):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",n=5)

def test(a,b=10,c=100):
    print(a+b+c)


test(10,20,30)

value = input("> ")
print(value)


def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")

return_test()

def return_test():
    return 100

value = return_test()
print(value)


def return_test():
    return True

value = return_test()
print(value)


def return_test():
    return False

value = return_test()
print(value)

def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i

    return output

print("0 to 100: ", sum_all(0, 100))
print("0 to 1000: ", sum_all(0, 1000))
print("50 to 100: ", sum_all(50, 100))
print("500 to 1000: ", sum_all(500, 1000))

def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output

print("0 to 100: ", sum_all(0, 100, 10))

def f(x):
    return x

print(f(10))

def f(x): #f(x)=2x + 1
    return 2*x +1

print(f(10))

def f(x): #f(x)=x^2 + 2x + 1
    return x ** 2 + 2 * x + 1

print(f(10))

def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

print(mul(5, 7, 9, 10))

def function(*values, valueA, valueB): 
    pass
function(1,2,3,4,5)

def function(*values, valueA=10, valueB=20):
    pass
function(1,2,3,4,5)

def function(valueA, valueB, *values):
    pass
function(1,2,3,4,5)

def function(valueA=10, valueB=20, *values):
    pass
function(1,2,3,4,5)

def factorial(n):
    #변수 선언
    output = 1
    # 반복문 돌려 숫자 더하ㅓ기
    for i in range(1, n+1):
        output *= i
        # 리턴
    return output

print("1! :",factorial(1))
print("2! :",factorial(2))
print("3! :",factorial(3))
print("4! :",factorial(4))
print("5! :",factorial(5))

def factorial(n):
    # n이 0이라면 1을 리턴
    if n == 0:
        return 1
    # n이 0이 아니라면 n*(n-1)!을 리턴
    else: 
        return n * factorial(n-1)
    
print("0! :",factorial(0))
print("1! :",factorial(1))
print("2! :",factorial(2))
print("3! :",factorial(3))
print("4! :",factorial(4))
print("5! :",factorial(5))
print("6! :",factorial(6))

def fibonacci(n):
    if n ==1:
        return 1
    if n == 2:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
print("fibonacci(1) :",fibonacci(1))
print("fibonacci(1) :",fibonacci(2))
print("fibonacci(1) :",fibonacci(3))
print("fibonacci(1) :",fibonacci(4))
print("fibonacci(1) :",fibonacci(5))