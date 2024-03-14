# "from testPackage import *"로
# 모듈을 읽어 들일 때 가져올 모듈

__all__ = ["moduleA", "moduleB"]

#패키지를 읽어 들일 때 처리를 작서할 수도 있습니다.
print("testPackage를 읽어 들였습니다.")
