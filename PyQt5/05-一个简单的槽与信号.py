import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QDial, QApplication, QSlider

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # dial是信号，lcd是对应的槽
        lcd = QLCDNumber(self)
        dial = QDial
        # dial = QSlider(self)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('花猹')

        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)
        # 当信号有所改变，那么连接槽
        dial.valueChanged.connect(lcd.display)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())