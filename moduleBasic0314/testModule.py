def div():
    print("-------------------")
print("# import 된 모듈의 __name__출력")
print(__name__)
div()
PI = 3.141592

def numberInput():
    output = input("숫자 입력 > ")
    return float(output)

def getCircumference(radius):
    print(f"반지름이 '{radius}' 인 원의 둘레는 : ", end='')
    return 2 * PI * radius

def getCircleArea(radius):
    print(f"반지름이 '{radius}' 인 원의 넓이는 : " ,end='')
    return PI * radius

# 엔트리 포인트 확인
if __name__ == "__main__":
    print(getCircumference(10))
    print(getCircleArea(10))

else:
    print("메인이 아니지롱")

