import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('花猹')

        formlayout = QFormLayout()

        namelabel = QLabel('姓名')
        nameLineEdit = QLineEdit('')
        introductionLabel = QLabel('简介')
        introductionLineEdit = QTextEdit('')

        # 在表单中加一行，姓名标签和姓名编辑行
        formlayout.addRow(namelabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)
        self.setLayout(formlayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())