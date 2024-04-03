from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

# Qt에서 제공하는 기본 창을 커스터마이징하여 사용한다

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Escape', self)
        btn.clicked.connect(QCoreApplication.instance().quit) # 클릭 시 어플리케이션 종료

        btn1 = QPushButton('Button 1', self)
        btn1.setGeometry(50,175,100,50)
        
        btn2 = QPushButton('Button 2', self)
        btn2.setGeometry(150,175,100,50)

        btn3 = QPushButton('Button 3', self)
        btn3.setGeometry(250,175,100,50)
        btn3.setToolTip("나는 요네 뽑는다 기모링")

        
        self.setWindowTitle('PyQt Application')
        self.setWindowIcon(QIcon('GUI\penguin-icon.ico'))
        self.move(600,600)
        self.resize(600,600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = App()
    sys.exit(app.exec_())


