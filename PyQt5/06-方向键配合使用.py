import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Examle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('花猹')

        self.lab = QLabel('方向',self)

        self.lab.setGeometry(150, 100, 50, 50)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Examle()
    sys.exit(app.exec_())