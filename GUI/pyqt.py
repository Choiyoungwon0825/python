from PyQt5.QtWidgets import QApplication, QWidget 
import sys

# Qt에서 제공하는 기본 창을 커스터마이징하여 사용한다

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt Application')
        self.move(600,400)
        self.resize(600,400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = App()
    sys.exit(app.exec_())
