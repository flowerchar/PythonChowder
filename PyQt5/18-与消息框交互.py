import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton('Click here', self)
        self.button.clicked.connect(self.show_messagebox)
        self.show()

    def show_messagebox(self):
        # 用choice接收QMessageBox.question的返回值
        choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change',\
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            # 如果choice是Yes，那么button伤显示文本Changed!
            # setText()是QPushButton类的一个方法
            self.button.setText('Changed!')
        elif choice == QMessageBox.No:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())