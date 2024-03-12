'''# 변수 선언
counter = 0

# 함수를 선언


def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력합니다.
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    # 피보나치 수를구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

# 딕셔너리에 값이 메모되어 있으면 처리를 수행하지 않고 곧바로 메모된 값을 돌려주어 코드 속도를 빠르게 해줌
dictionary = {
    1: 1,
    2: 1
}
# 함수를 선언


def fibonacci(n):
    if n in dictionary:
        # 메모가 되어있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output


# 함수 호출
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))
print("fibonacci(60):", fibonacci(60))


def flatten(data):
    output = []
    for item in data:
        if type(item) == list:  # item 타입이 list 면, item요소를 output = []에 추가함,
            output += flatten(item)
            print("list 타입일 때 output",output)
            print("list 타입일 때", item)
        else: # item 요소가 list가 아니면, output = [] 에 item 요소를 배열에 넣음 
            output.append(item)
            print("list 타입 아닐 때 output",output)
            print("list 타입 아닐 때  ", item)
    return output


example = [
    [1, 2, 3], 
    [4, 
     [5, 6],
     ], 
     7,
     [8, 9]
     ]

print("원본 : {}".format(example))
print(f"변환 : {flatten(example)}")

tuple_test = (10,20,30)

print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])

[a, b] =  [10, 20]
(c, d) = (10, 20)

#출력합니다
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

# 괄호가 없는 튜플

tuple_test = 10, 20, 30 , 40

print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test) :", type(tuple_test))
print()

a,b,c = 10, 20, 30
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("a:",a)
print("b:",b)
print("c:",c)

a , b = 10, 20
print("a , b = 10, 20")
print("교환 전 : a, b", a, b)

a , b = b, a
print("a, b = b, a")
print("교환 후 : a, b", a, b)


# 함수 선언
def test():
    return (10,20)
# 여러 개의 값을 리턴받습니다.
a, b = test()

# 출력합니다.
print("a: ",a)
print("b: ",b)

#람다(lambda)
#함수의 매개변수로 함수 전달하기

def call_10_times(func):
    for i in range(10):
        func()

# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

#조합하기
call_10_times(print_hello)
'''


'''
원래 같으면 이렇게 선언함 함수는
def power(x: x*x):
    return power

print(power(3))

def under_3(x: x < 3):
    return under_3

print(under_3(4))

# 근데 함수를 간단하게 쓰려면 lambda를 쓰면된다.
# 함수를 선언합니다.

def power(x): return x*x
def under_3(x): return x < 3


# 변수를 선언합니다.
list_input_a = [1, 2, 3, 4, 5]

# map() 함수는-> 리스트를 받으면 리스트로 반환해줌
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("#map(power, list_input_a):", output_a)
print("#map(power, list_input_a):", list(output_a))
print()

# filter() 함수는 -> 리스트에 요소를 함수에 넣어 True 인것만 반환
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("#map(under_3, list_input_a):", output_b)
print("#map(under_3, list_input_a):", list(output_b))
print()

# 더 간단하게~
list_input_a = [1, 2, 3, 4, 5]

# map() 함수는-> 리스트를 받으면 리스트로 반환해줌
output_a = map(lambda x: x*x, list_input_a)
print("# map() 함수의 실행 결과")
print("#map(power, list_input_a):", output_a)
print("#map(power, list_input_a):", list(output_a))
print()
# filter() 함수는 -> 리스트에 요소를 함수에 넣어 True 인것만 반환
output_b = filter(lambda x: x, list_input_a)
print("# filter() 함수의 실행 결과")
print("#map(under_3, list_input_a):", output_b)
print("#map(under_3, list_input_a):", list(output_b))
print()

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]


def a(x, y): return x * y
# || 같다
# def a(x,y):
#     return x*y


print(a(10, 2))
result = map(a, list1, list2)
print(list(result))


# w = write, r = read, a = append
# 파일 열기
file = open("오픈해볼께0312.txt", "r")

# 파일에 텍스트를 씁니다.
file.write("잘 되누\n")
file.write("잘 되누")

# 파일 닫기
file.close()

with open("오픈해볼께0312.txt", "w") as file:
    # 파일에 텍스트 쓰기
    file.write("hello hello hello")

# 파일 열기
with open("오픈해볼께0312.txt", "r") as file:
    # 파일을 읽고 출력하기
    contents = file.read()
print(contents)



# 랜덤한 숫자를 만들기 위해 가져옵니다.
import random as r
# 간단한 한글 리스트 만들기
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기 모드로 합니다.
with open("info0312.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성
        name = r.choice(hanguls) + r.choice(hanguls)
        weight = r.randrange(40, 100)
        height = r.randrange(140, 200)

        # 텍스트를 씁니다.
        file.write("{}, {}, {}\n".format(name, weight, height))


with open("info0312.txt","r") as file:
    for line in file:
        # 변수를 선언합니다.
        (name, weight, height) = line.strip().split(", ")

        # 데이터가 문제없는지 확인,문제가 없으면 지나감
        if (not name) or (not weight) or (not height):
            continue # 
        # 결과를 계산합니다.
        bmi = int(weight) / ((int(height) / 100) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result ="정상 체중"
        else:
            result ="저체중"

        print('\n'.join([ # join이란? => 문자열.join(문자열로 구성된 리스트) 로 사용된다 ex) print("::".join([1,2,3,4,5])) -> 1::2::3::4::5
            "이름 : {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name,weight,height,bmi,result))
        print()


# 이터레이터 (iterator)
#        반복 가능한 객체(interable)의 요소들에 접근하는 방법을 제공한다. 
#        ex) 리스트, 딕셔너리, 파일등이 이터레이터 임 
#        range()

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3

# 제네레이터는 함수 내부에 yeild를 사용하면 제네레이터 함수가 된다.
# 제네레이터 함수는 일반 함수와 다르게 출력이 되지 않는다.

def test():
    print("함수가 호출되었습니다.")
    yield "test"

# 함수 호출
print("A 지점 통과")
test()
print("B 지점 통과")
test()
print(test())

# 함수 선언


def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")


output = test()
# next 함수 호출
print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)  # 다음 yield 키워드가없어서 오류가 날 것임
# 한 번 더 실행하기
next(output)

numbers = [1, 2, 3, 4, 5, 6]

print("::".join(map(str, numbers)))

numbers = list(range(1, 10+1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))


print("# 3 이상, 7 미만 인 수 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))


print("# 제곱해서 50 미만 인 수 추출하기")
print(list(filter(lambda x: x ** 2 < 50, numbers)))

for i in range(1,10):
    print(f"구구단 {i}단 ",)
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")


aList = [1,2,3]

bList = [10,100,1000]

for a in aList:
    for b in bList:
        print(a * b, end=' ')
    print() 
'''
'''
# 1부터 10까지 차례로 출력하는 프로그램 작성
for i in range(1, 10+1):
    print(i)


# 1부터 입력받은 정수까지 차례로 출력하는 프로그램 작성
n = int(input("정수를 입력하세요 >> "))
for i in range(1, n + 1):
    print(i)

# 1부터 100까지 숫자 중 짝수만 출력하는 프로그램을 작성
for i in range(1, 100+1):
    if i % 2 == 0:
        print(i)


sinput = input("문자를 입력하세요 >> ")
for i in range(5):
    print(sinput)

n = int(input("정수를 입력하세요 >> "))
for i in range(n, 50+1):
    print(i)


# 5명의 키 총합과 평균 출력하기
sum = 0
h_list = [159, 163, 173, 158, 169]
for h in h_list:
    sum += h
print("sum : %d" % sum)
print("avg : %.2f" % (sum/len(h_list)))

'''


# 5명의 키를 입력받아 입력받은 키의 총합과 평균을 구하는 프로그램을 작성해 봅시다.
sum = 0
h_list=[]
for _ in range(5):
    h = int(input("입력 : "))
    sum += h

print(sum)
print(sum/len(h_list))