import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QMessageBox, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()

        # 记录是否已经保存
        self.is_saved = True

        self.textedit = QTextEdit(self)
        self.textedit.textChanged.connect(self.on_textchanged_cha)

        self.button = QPushButton('Save', self)
        self.button.clicked.connect(self.on_clicked_cha)

        self.v_layout = QVBoxLayout(self)
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def on_textchanged_cha(self):
        # 如果textedit里面还有文字，则是未保存
        if self.textedit.toPlainText():
            self.is_saved = False
        # 否则没有文字的话，直接不用询问
        else:
            self.is_saved = True

    def on_clicked_cha(self):
        self.save_func(self.textedit.toPlainText())
        self.is_saved = True

    def save_func(self, text):
        with open('saved.txt', 'w') as f:
            f.write(text)

    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the txt?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.textedit.toPlainText())
                # QCloseEvent.accept()会接收窗口关闭操作
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())