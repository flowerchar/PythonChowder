import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, \
    QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout


class Demo(QWidget):
    choice = 'a'
    choice_list = ['b', 'c', 'd', 'e']

    def __init__(self):
        super(Demo, self).__init__()

        # 这是一个普通下拉框
        self.combobox_1 = QComboBox()
        # 这是一个字体下拉框，里面有默认的字体
        self.combobox_2 = QFontComboBox()

        self.lineedit = QLineEdit()

        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.combobox_init()

    def layout_init(self):
        self.v_layout.addWidget(self.combobox_1)
        self.v_layout.addWidget(self.combobox_2)
        self.v_layout.addWidget(self.lineedit)

        self.setLayout(self.v_layout)

    def combobox_init(self):
        # QComboBox.addItem()是为组合框添加一个选项
        # 这一步是默认把第一个框设为a，否则是items里的第一个
        self.combobox_1.addItem(self.choice)
        # 这是为组合框添加更多选项
        self.combobox_1.addItems(self.choice_list)
        # 如果当前的组合框选项的序号发生改变，发射信号到槽函数
        self.combobox_1.currentIndexChanged.connect(lambda :self.on_combobox_func(self.combobox_1))

        # 如果当前字体组合框的字体发生改变，发射信号到槽函数
        self.combobox_2.currentFontChanged.connect(lambda :self.on_combobox_func(self.combobox_2))

    def on_combobox_func(self, combobox):
        print(self.sender())
        if combobox == self.combobox_1:
            # currentIndex()是获得该组合框里面的选项，从0开始排列
            # currentText()是获得在此选项框里，选中选项的文本
            QMessageBox.information(self, 'ComboBox 1', f'{combobox.currentIndex()}: {combobox.currentText()}')
        else:
            # 否则如果是combobox_2的话，在编辑行里面设置字体
            # setFont()将输入框字体设为当前选中的字体，currentFont()获取下拉框当前的字体
            self.lineedit.setFont(combobox.currentFont())
            print(combobox.currentFont())
            print(combobox.currentText())
            print(combobox.font())
            print(combobox.fontInfo())
            print(combobox.fontMetrics())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())