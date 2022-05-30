import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        # 用来显示当前操作的内容
        self.label = QLabel('No Click')

        # 实例化一个树形控件
        self.tree = QTreeWidget()
        # 这个方法将控件的列数设为2，默认为1
        self.tree.setColumnCount(2)
        # 这个为每列设置一个标题，如果只有一列的话
        # 通过setHeaderLabel(str)为单列设置标题
        self.tree.setHeaderLabels(['Install Components', 'Test'])
        # 当点击QTreeWidget中的任意一项，就会触发该信号
        # 这个信号会自动为槽函数传入两个参数，item,column，第一个为点击的项，第二个为项所在的列
        self.tree.itemClicked.connect(self.change_cha)

        # preview的父类为self.tree，则preview为最顶层
        self.preview = QTreeWidgetItem(self.tree)
        # 0表示preview在第一列，后一个为文本
        self.preview.setText(0, 'Preview')

        # 这步操作也跟上面的效果一样
        # self.preview = QTreeWidgetItem()
        # self.preview.setText(0, 'Preview')
        # self.tree.addTopLevelItem(self.preview)

        self.qt5112 = QTreeWidgetItem()
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        # 让该项以复选框的形式呈现出来
        self.qt5112.setCheckState(0, Qt.Unchecked)
        # preview添加子项qt5112
        self.preview.addChild(self.qt5112)

        choice_list = ['macOS', 'Android x86', 'Andriod ARMv7', 'Sources', 'ios']
        self.item_list = []
        for i, c in enumerate(choice_list):
            # 实例化五个子项，添加到qt5112中，并以复选框显示
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)
            item.setCheckState(0, Qt.Unchecked)
            self.item_list.append(item)

        self.test_item = QTreeWidgetItem(self.qt5112)
        self.test_item.setText(0, 'test1')
        self.test_item.setText(1, 'test2')

        # 该方法使得所有的项都是打开显示的，必须要在所有的项实例化后调用
        self.tree.expandAll()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)
        self.h_layout.addWidget(self.label)
        self.setLayout(self.h_layout)

    def change_cha(self, item, column):
        self.label.setText(item.text(column))

        print(item.text(column))
        print(column)
        # 如果被点击的项是qt5112
        if item is self.qt5112:
            # 再如果qt5112被选中
            if self.qt5112.checkState(0) == Qt.Checked:
                # 它的所有子项都设为选中状态
                [x.setCheckState(0, Qt.Checked) for x in self.item_list]
            else:
                # 否则全部子项为未选中状态
                [x.setCheckState(0, Qt.Unchecked) for x in self.item_list]
        # 如果被点击的不是qt5112
        else:
            check_count = 0
            # 判断有多少子项被选中
            for x in self.item_list:
                if x.checkState(0) == Qt.Checked:
                    check_count += 1
            # 如果为5，则设置为全选中
            if check_count == 5:
                self.qt5112.setCheckState(0, Qt.Checked)
            # 如果数量在0到5之间，设为半选中状态
            elif 0 < check_count < 5:
                self.qt5112.setCheckState(0, Qt.PartiallyChecked)
            else:
                self.qt5112.setCheckState(0, Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())