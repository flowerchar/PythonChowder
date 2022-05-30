import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLineEdit, QPushButton,\
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox, QLabel

# 全局变量用户信息
USER_PWD = {
    'la_vie':'password'
}
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(300, 100)

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.lineeidt_init()
        self.pushbutton_init()
        self.layout_init()
        self.signin_page = SigninPage()

    def layout_init(self):
        '''
        设置布局
        :return:
        '''
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def lineeidt_init(self):
        '''
        在行里面写入默认文字
        :return:
        '''
        # QLineEdit有个方法setPlaceholderText，用来在一个框里面显示文字
        self.user_line.setPlaceholderText('Please enter your name')
        self.pwd_line.setPlaceholderText('Please enter your password')

        # QLineEdit有个信号textChanged
        # 该信号是输入框文本发生变化的时候发到槽里面
        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        '''
        检查框内是否已经有输入的文本，以此确定按钮是否能按下
        :return:
        '''
        # QLineEdit一个方法，text()用来获得框里的内容
        # 如果用户框和密码框同时有输入的，那么就使按钮可用
        if self.user_line.text() and self.pwd_line.text():
            # QPushButton有个方法，setEnabled(flag)，为True则按钮可用，否则不可用
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    def pushbutton_init(self):
        '''
        让刚开始的登陆按钮不可用
        :return:
        '''
        # QPushButton有个setEnabled()方法，是否可以用？True则是可以
        self.login_button.setEnabled(False)
        # QPushButton有个信号,clicked
        # 当登陆按钮被点击时，连接槽，检查是否正确
        self.login_button.clicked.connect(self.check_login_func)
        self.signin_button.clicked.connect(self.show_signin_page_func)

    def check_login_func(self):
        '''
        检查密码账户是否正确的槽函数
        :return:
        '''
        # QLineEdit有个方法text()，获取当前行里的内容
        # 字典有个方法get(value)，获得键为value的值
        # 也就是用户行输入的是‘la_vie’，并且密码是‘password’，则信息正确，这两个要同时满足
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, 'Information', 'Log in successfully!')
        else:
            QMessageBox.critical(self, 'Wrong', 'Wrong username or password')
        # QLineEdit有个方法,clear()，用来清除行里面的内容
        self.user_line.clear()
        self.pwd_line.clear()

    def show_signin_page_func(self):
        # 类似QWidget的show()，但是QDialog的exec_()可以让窗口是模态的
        self.signin_page.exec_()
        print(USER_PWD)

# 用于注册界面的类
# QDialog使得注册窗口是模态的，仅当该窗口执行完毕才能操作其他窗口
# QWidget不具有该方法，所以继承QDialog
class SigninPage(QDialog):

    def __init__(self):
        super().__init__()
        self.signin_user_label = QLabel('Username', self)
        self.signin_pwd_label = QLabel('Password', self)
        self.signin_pwd2_label = QLabel('Password', self)
        self.signin_user_line = QLineEdit()
        self.signin_pwd_line = QLineEdit()
        self.signin_pwd2_line = QLineEdit()
        self.signin_button = QPushButton('Sign in', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)
        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.signin_button)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        # 设置密码为圆点
        # QLineEdit具有的方法,setEchoMode
        self.signin_pwd_line.setEchoMode(QLineEdit.Password)
        self.signin_pwd2_line.setEchoMode(QLineEdit.Password)

        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.signin_user_line.text() and self.signin_pwd_line.text() and self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)
        #self.signin_button.clicked.connect(self.show_signin_page_func)

    def check_signin_func(self):
        if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
            QMessageBox.critical(self, 'Wrong', 'Two Password Typed Are Not Same!')
        # 如果两次密码框内容一致了，那么再如果USER_PWD里面不存在这个键值对
        # 再向里面添加一个
        elif self.signin_user_line.text() not in USER_PWD:
            USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
            QMessageBox.information(self, 'Information', 'Register Successfully!')
            self.close()
        else:
            QMessageBox.critical(self, 'Wrong', 'This Username Has Been Registerd!')

        self.signin_user_line.clear()
        self.signin_pwd_line.clear()
        self.signin_pwd2_line.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())