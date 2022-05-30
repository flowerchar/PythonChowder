import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

# 创立一个自定义图标类
class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 此方法为move和resize的结合
        self.setGeometry(300,400,200,300)
        self.setWindowTitle('花猹')
        self.setWindowIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\学姐.jpg'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())