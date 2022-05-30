import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.checkbox1 = QCheckBox('Checkbox 1', self)
        self.checkbox2 = QCheckBox('Checkbox 2', self)
        self.checkbox3 = QCheckBox('Checkbox 3', self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):
        # QCheckBox有个方法setChecked(),True代表让复选框为选中状态，False为不选中
        self.checkbox1.setChecked(True)
        # 还有一种更完善的方法，setCheckState(),Qt.Checked是选中,Qt.Unchecked是未选中,Qt.PartiallyChecked是半选中
        # self.checkbox1.setCheckState(Qt.Checked)
        self.checkbox1.stateChanged.connect(lambda :self.on_state_change_func(self.checkbox1))

        self.checkbox2.setChecked(False)
        self.checkbox2.stateChanged.connect(lambda :self.on_state_change_func(self.checkbox2))

        # 这个方法规定复选框有三种状态，一般与setCheckState配合使用
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda :self.on_state_change_func(self.checkbox3))

    def on_state_change_func(self, checkbox):
        # checkState()方法获取当前复选框的状态，0为无选中，1为半选中，2为全选中
        # checkbox.text()是按1,2,3,这样排列的一个数组
        print(f'{checkbox.text()} was clicked, and its current state is {checkbox.checkState()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())