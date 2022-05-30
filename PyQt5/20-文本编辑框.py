import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QTextEdit, \
    QTextBrowser, QHBoxLayout, QVBoxLayout, QLineEdit

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.edit_label = QLabel('QTextEdit', self)
        self.brower_label = QLabel('QTextBrower', self)
        # 因为这里不仅仅会用到一行上，所以不再使用QLineEdit
        # 而是使用范围更广的QTextBrowser
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.edit_v_layout = QVBoxLayout()
        self.brower_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()
        self.show()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.brower_v_layout.addWidget(self.brower_label)
        self.brower_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.brower_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        # 事件信号有且仅执行一次，且之后会一直监视
        self.text_edit.textChanged.connect(self.show_text_func)
        print('触发信号一次')

    def show_text_func(self):
        # 但是槽函数会根据信号来执行
        self.text_browser.setText(self.text_edit.toPlainText())
        print('执行槽函数一次')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())