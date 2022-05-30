import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, \
    QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout

class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # 添加user_label标签到网格布局里，它的坐标是（0，0）
        # 参数分部：横轴坐标，纵轴坐标，横轴跨距，纵轴跨距
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())