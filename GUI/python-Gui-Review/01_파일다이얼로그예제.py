from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 메뉴바 생성 및 메뉴 추가
        menuBar = self.menuBar()  # 창에 추가할 메뉴바 생성
        menu1 = menuBar.addMenu("파일")
        menu2 = menuBar.addMenu("편집")

        # 액션 생성 및 추가하기
        loadFile = QAction('불러오기', self)
        saveFile = QAction('저장하기', self)
        quitApp = QAction('종료하기', self)

        loadFile.triggered.connect(self.load)
        saveFile.triggered.connect(self.save)
        quitApp.triggered.connect(QCoreApplication.instance().quit)  # 프로그램 종료

        menu1.addAction(loadFile)
        menu1.addAction(saveFile)
        menu1.addAction(quitApp)
       
        

        # 메인 창에 대한 설정
        self.setWindowTitle("Review Program")
        # 윈도우창이 x,y 값만큼 이동하여 출력
        # self.move()
        self.resize(500, 400)
        self.show()

    def load(self):
        fname = QFileDialog.getOpenFileName(self, '불러오기', './')
        os.system(fname[0])

    def save(self):
        fname = QFileDialog.getSaveFileName(self, '저장하기', './')
        if fname[0] != '':
            with open(fname[0], 'w', encoding='utf8') as f:
                f.write('저장할 내용')


# 이 파일을 직접적으로 실행시킬 때만
if __name__ == "__main__":
    # sys.argv 에는 이 파일의 이름이 포함되어 있다.
    app = QApplication(sys.argv)
    # App 생성
    view = App()  # 보여준다.
    sys.exit(app.exec_())
