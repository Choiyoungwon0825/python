import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.list = [QCheckBox('돈가스'),QCheckBox('또도가스'),QCheckBox('가스')]
        self.initUI()

    def initUI(self):

        widget = QWidget()

        grid = QGridLayout()
        widget.setLayout(grid)
        
        grid.addWidget(QLabel('보낸 사람 : '), 0, 0)
        grid.addWidget(QLabel(': 람사 낸보'), 0, 2)
        grid.addWidget(QLabel('받는 사람 : '), 1, 0)
        grid.addWidget(QLabel(': 람사 는받'), 1, 2)
        grid.addWidget(QLabel('내용 : '), 2, 0)
        grid.addWidget(QLabel(': 내용'), 2, 1)
        grid.addWidget(QLabel('?'), 3, 0)
        grid.addWidget(QLabel('!'), 4, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
        grid.addWidget(QLineEdit(), 3, 1)
        grid.addWidget(QLineEdit(), 4, 1)

        hbox1 = QHBoxLayout()
        
        
        
        
        
        
        
        # 메인윈도우 안에서 다른 요소를 모아만든 위젯을 추가할 때
        self.setCentralWidget(widget)
        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('GUI\penguin-icon.ico'))
        self.move(0,0)
        self.resize(1920, 1080)
        self.show()


if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
