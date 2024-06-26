import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)

        
        self.btn = QPushButton('창 띄우기', self)
        self.btn.clicked.connect(self.showDialog)

        grid.addWidget(self.btn, 0, 0)

        self.setCentralWidget(widget)

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()
        
    def showDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print('선택한 색상 : %s' % color.name())
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())