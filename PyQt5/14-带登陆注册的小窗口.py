import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.user_label = QLabel('<h1 style="color:blue;">Username</h1>', self)
        self.pwd_label = QLabel('<h1 style="color:blue;">Password</h1>', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('登陆', self)
        self.signIn_button = QPushButton('注册', self)

        self.label_v_layout = QVBoxLayout()     #标签垂直排列
        self.line_v_layout = QVBoxLayout()      #行编辑垂直排列
        self.button_h_layout = QHBoxLayout()        #按键水平排列
        # 水平布局管理器
        self.label_line_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        # 在左垂直方向添加“Username”
        self.label_v_layout.addWidget(self.user_label)
        # 在左垂直方向添加“Password”
        self.label_v_layout.addWidget(self.pwd_label)
        # 在右垂直方向添加行编辑
        self.line_v_layout.addWidget(self.user_line)
        # 在右垂直方向添加行编辑
        self.line_v_layout.addWidget(self.pwd_line)
        # 在左水平方向添加“登陆”键
        self.button_h_layout.addWidget(self.login_button)
        # 在左水平方向添加“注册”键
        self.button_h_layout.addWidget(self.signIn_button)
        # addLayout是布局管理器
        # label_v_layout已经是一个布局了，它是垂直方向上的一个“Username”和“Password“
        # 现在将这个布局当做一个控件，作为左水平上的一个部件
        self.label_line_h_layout.addLayout(self.label_v_layout)
        # line_v_layout是一个布局，它是上下形式的垂直布局
        # 把这两个行编辑布局右水平放置
        self.label_line_h_layout.addLayout(self.line_v_layout)
        # 把标签和行编辑这两个水平布局当做一个控件，放在上面
        self.all_v_layout.addLayout(self.label_line_h_layout)
        # 把按钮键向下垂直放置
        self.all_v_layout.addLayout(self.button_h_layout)

        # 把all_v_layout当做全局布局
        self.setLayout(self.all_v_layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
