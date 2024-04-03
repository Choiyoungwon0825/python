import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cbList = [QCheckBox('돈까스'), QCheckBox('햄버거'), QCheckBox('감자탕')]
        self.initUI()

    def initUI(self):
        
        widget = QWidget() # 메인 위젯
        tab1 = QWidget() # 탭 메뉴 포함될 하위 위젯1
        tab2 = QWidget() # 탭 메뉴 포함될 하위 위젯2
        tab3 = QWidget() # 탭 메뉴 포함될 하위 위젯2
        
        tabs = QTabWidget()
        tabs.addTab(tab1, 'TAB2 에서 음식 선택')
        tabs.addTab(tab2, 'TAB2')
        tabs.addTab(tab3,'확인')

        hbox1 = QHBoxLayout(tab1)
        hbox1.addStretch(1)
        hbox1.addWidget(QLabel(''))
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout(tab2)
        hbox2.addStretch(1)
        hbox2.addWidget(self.cbList[0])
        hbox2.addWidget(self.cbList[1])
        hbox2.addWidget(self.cbList[2])
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout(tab3)
        hbox3.addStretch(1)
        btn = QPushButton('선택 항목 확인')
        btn.clicked.connect(self.showCheckedFood)
        hbox3.addWidget(btn)
        hbox3.addStretch(1)


        vbox = QVBoxLayout(widget)
        vbox.addWidget(tabs)

        self.setCentralWidget(widget) # 메인 위젯을 창에 넣는다,

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

    def showCheckedFood(self) : 
        for cb in self.cbList :
            if cb.isChecked() :
                print(cb.text())

        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
