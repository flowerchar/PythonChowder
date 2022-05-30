import sys
# QDesktopWidget提供了用户桌面信息
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    # 在initUI方法里面在调用一个方法
    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 获得主窗口所在的框架
        qr = self.frameGeometry()
        print(qr)
        # cp = QDesktopWidget().availableGeometry().center()
        # 获得当前桌面的信息
        cp = QDesktopWidget().availableGeometry()
        print(cp)
        # 获得当前桌面信息的中心坐标
        cp = cp.center()
        print(cp)
        # 把主框架的中心移到屏幕中心
        qr.moveCenter(cp)
        # 通过move方法将主窗口的左上角移到框架的左上角
        self.move(qr.topLeft())
        # self.move(0,0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())