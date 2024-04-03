from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time, os, sys
# Qt에서 제공하는 기본 창을 커스터마이징하여 사용한다

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Escape', self)
        btn.clicked.connect(QCoreApplication.instance().quit) # 클릭 시 어플리케이션 종료
        btn.setGeometry(150,125,100,50)
        btn.setToolTip('클릭 시 꺼짐')
        
        btn1 = QPushButton('Button 1', self)
        btn1.setGeometry(50,175,100,50)
        btn1.setToolTip('1 버튼')
        
        btn2 = QPushButton('Button 2', self)
        btn2.setGeometry(150,175,100,50)
        btn2.setToolTip('2 버튼')

        btn3 = QPushButton('Button 3', self)
        btn3.setGeometry(250,175,100,50)
        btn3.setToolTip('3 버튼')

        btn4 = QPushButton('Button 4', self)
        btn4.setGeometry(350,175,100,50)
        btn4.setToolTip('4 버튼')

        btn5 = QPushButton('Button 5', self)
        btn5.setGeometry(450,175,100,50)
        btn5.setToolTip('5 버튼')

        menuBar = self.menuBar()
        menu1 = menuBar.addMenu("파일")
        menu2 = menuBar.addMenu("편집")

        loadFile = QAction('불러오기',self)
        saveFile = QAction('저장하기',self)
        quitApp = QAction('나가기',self)
        
        # 클릭 시 동작 추가하기
        loadFile.triggered.connect(self.add_open)
        saveFile.triggered.connect(self.add_save)
        quitApp.triggered.connect(QCoreApplication.instance().quit)

        menu1.addAction(loadFile)
        menu1.addAction(saveFile)
        menu1.addAction(quitApp)
        
        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('GUI\penguin-icon.ico'))
        self.move(600,600)
        self.resize(600,600)
        self.show()

    # 파일을 선택하면 해당 파일이 열림 (실행됨)
    def add_open(self):
        fname = QFileDialog.getOpenFileName(self, '불러오기', './')
        os.system(fname[0])

    # 파일명을 입력하고 저장하면 폴더에 파일이 추가됨
    def add_save(self):
        fname = QFileDialog.getSaveFileName(self, '저장하기', './')
        if fname[0] != '' :
            with open(fname[0], 'w', encoding='utf8') as f :
                f.write('저장할 내용')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = App()
    sys.exit(app.exec_())
