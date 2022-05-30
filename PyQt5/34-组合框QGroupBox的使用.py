import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QLabel,\
    QVBoxLayout, QHBoxLayout

# QGroupBox可以把单选框给隔开，从而不是只选择一个
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # 实例化两个组合框，框里的文字会被虚线环绕并浮在上面
        self.groupbox_1 = QGroupBox('On and Off', self)
        self.groupbox_2 = QGroupBox('Change Color', self)

        self.red = QRadioButton('Red', self)
        self.blue = QRadioButton('Blue', self)
        self.green = QRadioButton('Green', self)
        self.yellow = QRadioButton('yellow', self)
        self.color_list = [self.red, self.blue, self.green, self.yellow]

        self.on = QRadioButton('On', self)
        self.off = QRadioButton('off', self)

        self.pic_label = QLabel(self)

        self.h1_layout = QHBoxLayout(self)
        self.h2_layout = QHBoxLayout(self)
        self.h3_layout = QHBoxLayout(self)
        self.all_v_layout = QVBoxLayout(self)

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.on)
        self.h1_layout.addWidget(self.off)
        # QGroupBox就有点像QWidget，可以设置布局
        self.groupbox_1.setLayout(self.h1_layout)

        self.h2_layout.addWidget(self.red)
        self.h2_layout.addWidget(self.blue)
        self.h2_layout.addWidget(self.green)
        self.h2_layout.addWidget(self.yellow)
        self.groupbox_2.setLayout(self.h2_layout)

        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)

        self.all_v_layout.addWidget(self.pic_label)
        self.all_v_layout.addLayout(self.h3_layout)

        self.setLayout(self.all_v_layout)

    # 在初始化方法中执行了该函数，在下面这个循环中设置四个事件循环
    def radiobutton_init(self):
        # 让yellow图片初始化为被标记
        self.yellow.setChecked(True)
        for btn in self.color_list:
            btn.clicked.connect(self.change_color_func)

        self.off.setChecked(True)
        # toggled信号是开关切换发出，开，关，而clicked是每个按钮只要toggled信号点击就触发
        self.off.toggled.connect(self.on_and_off_func)

    # 为灯泡初始化图片，并让灯泡居中
    def label_init(self):
        self.pic_label.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\pictures\images\off.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

    def change_color_func(self):
        if self.on.isChecked():
            path = r'C:\Users\DELL\Desktop\pictures\images\{}'.format([btn.text() for btn in\
                                                                       self.color_list if\
                                                                       btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))

    # 槽函数，当四个按钮有一个被点击则执行
    def on_and_off_func(self):
        # 如果在on的前提上，再为标签添加图片
        if self.on.isChecked():
            # 列表解析出来被标记的按钮，取他的文本内容，在取第一个
            # 因为这是单选框，所以在列表解析式中只有一个
            path = r'C:\Users\DELL\Desktop\pictures\images\{}'.format([btn.text() for btn in\
                                                                       self.color_list if\
                                                                       btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))
        else:
            self.pic_label.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\pictures\images\off.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())