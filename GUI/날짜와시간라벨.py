import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 메인윈도우는 메뉴바와 상태바가 지원되는 창을 만든다.
        # 큐위젯은 다양한 위젯을 추가할 수 있는 공간을 만든다.
        # 따라서 큐위젯을 메인윈도우에 포함이 가능하다.

        widget = QWidget()
        datetime = QDateTime.currentDateTime()

        label = QLabel(datetime.toString('yyyy년 MM월 dd일, hh:mm:ss'), self)
        label.setAlignment(Qt.AlignCenter)


        font = label.font()
        font.setPointSize(12)

        label.setFont(font)
        label.setGeometry(100, 100, 200, 100)

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())


