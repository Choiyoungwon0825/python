import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



# 오늘의 8교시 실습 과제
# - PyQT5 예제 전체적으로 훑어보기
# - 입력창과 버튼이 하나씩 있는 창을 하나 만들자

# 그리고 버튼을 누르면 입력창에 쓰여 있는 내용이
# 메시지박스에 띄워진다.

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()     
        self.initUI()
        
    
    def initUI(self):

        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)
        self.text_label = QLabel(self)
        self.lineEdit = QLineEdit(self)

        grid.addWidget(QLabel('아무 내용이나 입력하세요'))
        grid.addWidget(self.lineEdit)
        self.btn = QPushButton('입력 확인')
        self.btn.clicked.connect(self.buttonClick)
        grid.addWidget(self.btn)


   
        self.setCentralWidget(widget)
        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

      


    def buttonClick(self):
        text = self.lineEdit.text()
        reply = QMessageBox.question(self, '값 들어오는 곳 ', text,
                                    QMessageBox.Close)
        
        if reply == QMessageBox.close:
            App.quit()

       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = App()
    sys.exit(app.exec_())