import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QFormLayout

class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('花猹')
        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('登陆', self)
        self.signin_button = QPushButton('注册', self)

        # 实例化一个表单对象
        self.form_layout = QFormLayout()
        # 实例化一个水平布局
        self.button_h_layout = QHBoxLayout()
        # 实例化一个垂直布局
        self.all_v_layout = QVBoxLayout()

        # 在表单布局中，第一个参数是用户标签，第二个是行编辑
        self.form_layout.addRow(self.user_label, self.user_line)
        # 左边放密码标签，右边放行编辑
        self.form_layout.addRow(self.pwd_label, self.pwd_line)
        # 在一行里左边设置登陆按钮
        self.button_h_layout.addWidget(self.login_button)
        # 在这行里右边设置注册按钮
        self.button_h_layout.addWidget(self.signin_button)
        # 垂直布局上面是表单布局
        self.all_v_layout.addLayout(self.form_layout)
        # 垂直布局下面是水平布局
        self.all_v_layout.addLayout(self.button_h_layout)

        # 整体采用垂直布局
        self.setLayout(self.all_v_layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())
