'''
sum = 0
for i in range(5):
    n = int(input("키를 입력해 주세요 >> "))
    sum += n 

print("sum: %d" % sum)
print("avg : %.2f" % sum/5)

    
for i in range(3):
    for j in range(1,6):
        print(j, end=' ')
    print()
print()

for i in range(5):
    for j in range(5):
        print("*", end='')
    print()
print()

for i in range(2,10):
    print("< %d 단>" % i )
    for j in range(1,10):
        print("%d * %d = %d" % (i, j, i*j))


# 입력받은 정수의 3의 배수 합
sum = 0
n = int(input("정수를 입력하세여 >> "))
for i in range(1, n + 1):
    if i % 3 == 0:
        sum += i
print("입력받은 정수까지의 3의배수의 합 : ",sum)
    
# 양의 정수를 입력받아 입력받은 정수의 각 자리 숫자의 합
sum = 0 
n = input("양의 정수를 입력 >> ")
for i in n:
    sum += int(i)
print("숫자의 합 :", sum)


sum = 0
slist =[]
for _ in range(5):
    a = input("입력 (숫자와 숫자사이 공백을 넣어주세요) >> ").split()
    sum = int(a[0])+int(a[1])
    slist.append(sum)    

for i in slist:
    print(i, end=' ')
'''
'''
lis=[]
for _ in range(3):
    a = input().split()
    sum = 0
    for i in range(len(a)):
        print(len(a)) 
        sum+=int(a[i]) 
    print(sum)
    lis.append(sum)

for i in lis:
    print(i,end=" ")


# 정수 10개를 입력받아 그 중 가장 큰 수를 출력하는 프로그램을 작성

a = input("정수 10개 입력 >> ").split()
mx = 0
for i in range(len(a)):
    if mx < int(a[i]):
        mx = int(a[i])

print(mx)

a = [1,54,6,3,3,5,2,3,4,5]
a.sort() 

print(a)
print(a[-1])    

a = input("정수 10개 입력 >> ").split()
for i in range(len(a)):
    a[i] = int(a[i])

a.sort()
print(a[-1])

# 정수 n을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램을 작성

n = int(input("정수 n 입력 >> "))
for i in range(n + 1):
    print("*" * i)
# 정수 n을 입력받아 n단의 오른쪽 직각 이등변 삼각형을 그리는 프로그램을 작성

n = int(input("정수 n 입력 >>"))
for i in range(n + 1):
    print(" " * (n-i), "*" * i)


n = int(input("정수 n 입력 >>"))
for i in range(n):
    for j in range(i + 1):
        print("*", end='')
    print()


n = int(input("정수 n 입력 >>"))
for i in range(n):
    for j in range(i + 1):        
        print("*", end='')
    print()
'''

'''
n = int(input("정수 n 입력 >>"))
for i in range(n):
    # 빈칸
    for j in range(n - i - 1):        
        print(" ", end='')
    # 별
    for j in range(i+1):        
        print("*", end='')
    print()

# 구문 오류 : 프로그램 실행 전 발생하는 오류
# 런타임 오류 : 프로그램 실행 중 발생하는 오류

nInput = int(input("정수 입력 > "))

print("원의 반지름 : ", nInput)
print("원의 둘레 : ", 2 * 3.14 * nInput)
print("원의 넓이 : ", 3.14 * nInput)


try:
    # 예외가 발생할 가능성이 있는 코드
    pass

except: 
    # 예외가 발생한 후 코드
    pass




list_input = ["52","273","32","스파이","103"]
list_number = []
for item in list_input:
    try:
        float(item)
        list_number.append(item)

    except:
        pass
print("{} 내부에 있는 숫자는".format(list_input))
print("{} 입니다".format(list_number))


try:
    #숫자로 변환합니다.
    nmInput = int(input(" 정수 입력 >> "))
except: 
    print("정수가 아닌데용")
    
else:
    #출력
    print("원의 반지름 : ", nmInput)
    print("원의 둘레 : ", 2 * 3.14 * nmInput)
    print("원의 넓이 : ", 3.14 * nmInput)

finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

try:
    #파일을 엽니다.
    file = open("info0312.txt","w")
    # 여러가지 처리 수행
    # 파일 닫기
    file.close()
except:
    print("오류발생")

print("파일이 닫혔는지 확인하기")
print("file.colsed : ", file.closed)

def test():
    print("test()함수 첫 줄")

    try:
        print("try 실행")
        return
        print("try 구문의 return 구문 뒤입ㄴ다.")
    except:
        print("except 실행")
    else:
        print("else 실행")
    finally:
        print("finally 실행")
    print("test() 마지막")

test()

print("--------------")

print("프로그램이 시작되었습니다")
while True:
    try:
        print("try 구문 실행")
        break
        print("try 구문 break 키워드 뒤")
    except:
        print("except 실행")
    finally:
        print("finally 실행")
    print("while 반복문 마지막줄")
print("프로그램 종료")


numbers =[52,273,32,103,90,10,275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52,numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 1000
if number in numbers:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
else:
    print("- 리스트내부에 없는 값입니다.")
print()

print("---정상적으로 종료되었습니다.---")

try:
    #숫자로 변환합니다.
    nmInput = int(input(" 정수 입력 >> "))
    #출력
    print("원의 반지름 : ", nmInput)
    print("원의 둘레 : ", 2 * 3.14 * nmInput)
    print("원의 넓이 : ", 3.14 * nmInput)
except Exception as exeption:
    print("type(exception): ", type(exeption))
    print("exception", exeption)
'''
# 변수 선언
list_number =[52,273,32,72,100] 

while True:
    try:
        number_input = int(input("정수 입력 >> "))
        #리스트 출력
        print("{}번째 요소: {} ".format(number_input,list_number[number_input]))
    except ValueError :
        print("정수를 입력하세요")
    except IndexError:
        print("리스트의 인덱스를 벗어났어요")
    except Exception as exception:
        print("미리 파악하지 못한 예외가 발생했습니다.")

