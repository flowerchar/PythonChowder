import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.pic_label = QLabel()
        self.pic_label.setPixmap(QPixmap(r'C:\Users\DELL\Desktop\pictures\images\arrow.png'))

        # 左侧已经显示的列表
        self.listwidget_1 = QListWidget()
        # 右侧是选中的列表项
        self.listwidget_2 = QListWidget()
        # 如果在QListWidget里双击，则发出信号
        self.listwidget_1.doubleClicked.connect(lambda :self.change_cha(self.listwidget_1))
        self.listwidget_2.doubleClicked.connect(lambda :self.change_cha(self.listwidget_2))

        # 在列表中加入列表项的第一种方法：
        for i in range(6):
            text = f'Item{i}'
            # 通过QListWidgetItem()强制转换字符串
            self.item = QListWidgetItem(text)
            # 通过addItem()向列表里添加项
            self.listwidget_1.addItem(self.item)

        # 第二种，QListWidgetItem(string, QListWidget)
        self.item_6 = QListWidgetItem('Item 6', self.listwidget_1)

        # 第三种，直接addItem(string)
        self.listwidget_1.addItem('Item 7')
        str_list = ['Item 9', 'Item 10']
        # 或者addItems(iterable)，添加一个可迭代对象
        self.listwidget_1.addItems(str_list)

        self.item_8 = QListWidgetItem('Item 8')
        # 第四种在指定位置添加insertItem(number, QListWidgetItem)
        self.listwidget_1.insertItem(8, self.item_8)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listwidget_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listwidget_2)
        self.setLayout(self.h_layout)

    def change_cha(self, listwidget):
        if listwidget is self.listwidget_1:
            # QListWidget.currentItem()获得当前选中的项
            item = QListWidgetItem(self.listwidget_1.currentItem())
            self.listwidget_2.addItem(item)
            print(self.listwidget_2.count())
            # count()是在列表里的项数量
        else:
            # 这里只能使用currentRow()获得在第二个列表里选中的项
            # takeItem(row)就把项从里面删除了
            # print(self.listwidget_2.currentRow())
            # print(self.listwidget_2.currentIndex())
            # currentRow()获得的是一个对象
            # currentIndex()获得的是一个Int
            self.listwidget_2.takeItem(self.listwidget_2.currentRow())
            print(self.listwidget_2.count())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())