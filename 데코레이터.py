def test(function):
    def wrapper():
        print("인사 시작ㅎㅎ")
        print("함수 앞임")
        function()
        print("함수 뒤임ㅎㅎ")
        print("인사 종료")
    return wrapper

@test
def hello():
    print("hello")

hello()