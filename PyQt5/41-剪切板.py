import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, \
    QPushButton, QGridLayout

# 这里的剪切板是无形的
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit()
        self.text_browser = QTextBrowser()

        # 实例化一个剪切板
        self.clipboard = QApplication.clipboard()
        # 当剪切板的内容发生变化，则触发该信号
        self.clipboard.dataChanged.connect(lambda :print('Data Changed'))

        self.copy_btn = QPushButton('Copy', self)
        self.copy_btn.clicked.connect(self.copy_cha)

        self.paste_btn = QPushButton('Paste', self)
        self.paste_btn.clicked.connect(self.paste_cha)

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.text_edit, 0, 0, 1, 1)
        self.g_layout.addWidget(self.text_browser, 0, 1, 1, 1)
        self.g_layout.addWidget(self.copy_btn, 1, 0, 1, 1)
        self.g_layout.addWidget(self.paste_btn, 1, 1, 1, 1)
        self.setLayout(self.g_layout)

    # 当点击copy按钮，则为剪切板设置文本内容，当前文本编辑区里的东西
    # 同时clipboard里的数据发生变化，打印Data Changed
    def copy_cha(self):
        self.clipboard.setText(self.text_edit.toPlainText())

    # 当点击paste按钮，text_browser设置内容为剪切板上的
    def paste_cha(self):
        self.text_browser.setText(self.clipboard.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())