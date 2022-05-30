import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel,\
    QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap

# 这个例子也可以用QToolButton来使用，但是图片只能是图片形式，过于小了
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.off_button = QRadioButton('off', self)
        self.on_button = QRadioButton('on', self)

        # 这里如果放入字体，会被之后的图片给掩盖
        self.pic_label = QLabel('h')

        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        # 这三步使得图片居中
        self.pic_h_layout.addStretch(1)
        self.pic_h_layout.addWidget(self.pic_label)
        self.pic_h_layout.addStretch(1)

        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        # 这里只标记了off_button一个按钮的标记状态，这是因为只有两个按钮
        # 且这两个按钮均为单选框，所以如果off_button为True了，那另一个自然就为False了
        self.off_button.setChecked(True)
        self.off_button.toggled.connect(self.on_off_bulb_func)

    def label_init(self):
        self.pic_label.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\pictures\images\灯泡暗.png'))

    def on_off_bulb_func(self):
        # print(self.on_button.isChecked())
        if self.off_button.isChecked():
            # QLabel有个方法setPixmap，用来接收QPixmap对象
            # QPixmap对象接收一个图片的路径
            self.pic_label.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\pictures\images\灯泡暗.png'))
        else:
            self.pic_label.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\pictures\images\灯泡亮.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())