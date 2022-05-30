import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox,\
    QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # 这是一个整型数字调节框
        self.spinbox = QSpinBox()
        # setRange()给该调节框设一个范围
        self.spinbox.setRange(-99, 99)
        # setSingleStep()设置一个步长
        self.spinbox.setSingleStep(1)
        # 为调节框设一个初始值66
        self.spinbox.setValue(66)
        # 当调节框里的值发生改变时，发动槽函数
        self.spinbox.valueChanged.connect(self.value_change_func)

        # 这是一个浮点型的数字调节框
        self.double_spinbox = QDoubleSpinBox()
        # 这个可以来设置小数位数有多少
        # self.double_spinbox.setDecimals(5)
        # 设置范围
        self.double_spinbox.setRange(-99.99, 99.99)
        # 设置步长
        self.double_spinbox.setSingleStep(0.01)
        # 设置初始值66.66
        self.double_spinbox.setValue(66.00)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.double_spinbox)
        self.setLayout(self.h_layout)

    def value_change_func(self):
        # 当spinbox的值发生改变，改变doublebox的值
        # value()是获得当前的值
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())
        # setValue()是设置当前的值
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())