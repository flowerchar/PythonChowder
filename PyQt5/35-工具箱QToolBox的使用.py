import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QToolBox, QToolButton, QGroupBox,\
    QVBoxLayout

# QToolButton可设置图标
# 直接继承QToolBox
class Demo(QToolBox):

    def __init__(self):
        super().__init__()
        self.groupbox_1 = QGroupBox(self)
        self.groupbox_2 = QGroupBox(self)
        self.groupbox_3 = QGroupBox(self)

        self.toolbtn_f1 = QToolButton(self)
        self.toolbtn_f2 = QToolButton(self)
        self.toolbtn_f3 = QToolButton(self)
        self.toolbtn_m1 = QToolButton(self)
        self.toolbtn_m2 = QToolButton(self)
        self.toolbtn_m3 = QToolButton(self)

        self.v1_layout = QVBoxLayout(self)
        self.v2_layout = QVBoxLayout(self)
        self.v3_layout = QVBoxLayout(self)

        # QToolBox.addItem(QWidget, Str)
        # 将QGroupBox添加到QToolBox中，第一个为要添加的控件，第二个为为抽屉设定的名称
        # 因为这是继承于QToolBox，所以不具有addWidget()，而是addItem()

        self.addItem(self.groupbox_1, 'Couple One')
        self.addItem(self.groupbox_2, 'Couple Two')
        self.addItem(self.groupbox_3, 'Couple Three')
        # 当用户点击抽屉时，会触发currentChanged信号
        self.currentChanged.connect(self.print_index_func)

        self.layout_init()
        self.groupbox_init()
        self.toolbtn_init()

    def layout_init(self):
        self.v1_layout.addWidget(self.toolbtn_f1)
        self.v1_layout.addWidget(self.toolbtn_m1)
        self.v2_layout.addWidget(self.toolbtn_f2)
        self.v2_layout.addWidget(self.toolbtn_m2)
        self.v3_layout.addWidget(self.toolbtn_f3)
        self.v3_layout.addWidget(self.toolbtn_m3)

    def groupbox_init(self):
        # QGroupBox.setFlat(bool)为True则让边框消失
        self.groupbox_1.setFlat(True)
        self.groupbox_2.setFlat(True)
        self.groupbox_3.setFlat(True)
        self.groupbox_1.setLayout(self.v1_layout)
        self.groupbox_2.setLayout(self.v2_layout)
        self.groupbox_3.setLayout(self.v3_layout)

    def toolbtn_init(self):
        # QToolButton.setIcon()可以为按钮设置图标
        self.toolbtn_f1.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\f1.ico'))
        self.toolbtn_f2.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\f2.ico'))
        self.toolbtn_f3.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\f3.ico'))
        self.toolbtn_f3.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\m1.ico'))
        self.toolbtn_m1.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\m2.ico'))
        self.toolbtn_m3.setIcon(QIcon(r'C:\Users\DELL\Desktop\pictures\icon\m3.ico'))

    def print_index_func(self):
        couple_dict = {
            0:'Couple One',
            1:'Couple Two',
            2:'Couple Three'
        }
        # QToolBox.currentIndex()用来获得当前抽屉的序号，从0,1,2开始
        sentence = f'You are looking at {couple_dict.get(self.currentIndex())}'
        print(sentence)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())