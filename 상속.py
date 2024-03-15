# 부모 클래스 선언
class Parent:
    def __init__(self) :
        self.value ="테스트"
        print("부모 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("부모 클래스의 test() 메소드입니다.")

# 자식 클래스 선언
class Child(Parent):
    def __init__(self):
        super().__init__() # Parent의 생성자 함수를 호출함
        print("자식 클래스의 __init()__ 메소드가 호출되었습니다.")


child = Child()
# 순서 부모 생성자 함수 호출 
# -> 자식 생성자 함수 호출
#- > 부모생성자의 test 함수 호출 
child.test()
print(child.value)