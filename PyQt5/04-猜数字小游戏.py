import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.num = randint(1,100)

    def initUI(self):
        '''
        建立主窗口
        :return:
        '''
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('花猹')
        self.setWindowIcon(QIcon(r'C:/Users/DELL/Desktop/格式工厂/3911775.ico'))

        self.bt1 = QPushButton('我猜',self)
        self.bt1.setGeometry(115,150,70,30)
        # 当鼠标放置在“我猜”这个按钮上时，会有提示“点击这里猜数字”
        self.bt1.setToolTip('<b>点击这里猜数字<b>')
        # 当bt1按钮被点击时，执行函数showMessage()
        self.bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字',self)
        # 选中所有内容
        self.text.selectAll()
        # 让光标自动聚焦在内容框里
        self.text.setFocus()
        self.text.setGeometry(80,50,150,30)

        self.show()

    def showMessage(self):
        # 获得QLineEdit中的内容
        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber > self.num:
            # 第二个参数是消息盒子的标题，第三个参数是内容
            QMessageBox.about(self, '看结果', '猜大了')
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了')
        else:
            QMessageBox.about(self, '看结果', '答对了！进入下一轮！')
            self.num = randint(1, 100)
            # 答对后，清除QLineEdit的内容
            self.text.clear()
            # 答对后，光标自动聚焦到QLineEdit里面
            self.text.setFocus()
    # 该方法是一个重写，换个名字就不行
    def closeEvent(self, event):
        # 第二个参数是消息盒子的标题，第三个参数是消息盒子的内容，最后的参数是默认选择的那一个
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())