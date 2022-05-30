import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(600, 600)

        self.lcd_1 = QLCDNumber()
        # QLCDNumber.setDigitCount()用来设置一共可以显示多少位数字
        self.lcd_1.setDigitCount(10)
        self.lcd_1.display(112345)

        self.lcd_2 = QLCDNumber()
        # QLCDNumber.setSegmentStyle()用来设置显示屏的数字样式
        # QLCDNumber.Outline 常量值为0，让内容浮现，其颜色同显示屏背景颜色相同
        # QLCDNumber.Filled 常量值为1，让内容浮现，颜色同窗口标题颜色相同
        # QLCDNumber.Flat 常量值为2，让内容扁平化显示，颜色同窗口标题颜色相同
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_2.setDigitCount(10)
        # QLCDNumber.setSmallDecimalPoint(bool)用来设置小数点的显示方式
        # 为True则小数点不单独占一个位置，为False则占一个位置，默认是False
        # self.lcd_2.setSmallDecimalPoint(True)
        self.lcd_2.display(0.12345)

        self.lcd_3 = QLCDNumber()
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        # self.lcd_3.setDigitCount(6)
        self.lcd_3.display('hello')

        self.lcd_4 = QLCDNumber()
        self.lcd_4.setSegmentStyle(QLCDNumber.Outline) # 顾名思义，就是只突出轮廓
        # QLCDNumber.setMode()用来更改数字的显示方式
        # QLCDNumber.Hex 常量值为0 十六进制
        # QLCDNumber.Dec 常量值为1 十进制
        # QLCDNumber.Oct 常量值为2 八进制
        # QLCDNumber.Bin 常量值为3 二进制
        self.lcd_4.setMode(QLCDNumber.Hex)
        self.lcd_4.setDigitCount(6)
        self.lcd_4.display(666)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)
        self.v_layout.addWidget(self.lcd_4)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())