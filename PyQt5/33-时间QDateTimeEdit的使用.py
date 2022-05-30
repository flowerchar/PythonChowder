import sys
# 这个类是用来编辑日期时间的
from PyQt5.QtWidgets import QApplication, QWidget, QDateTimeEdit,\
    QDateEdit, QTimeEdit, QVBoxLayout
# 这一个类是获得日期时间的
from PyQt5.QtCore import QDate, QTime, QDateTime


class Demo(QWidget):
        # 这里的信号发生改变是值变了，删除不算
    def __init__(self):
        super().__init__()
        self.datetime_1 = QDateTimeEdit()
        # 这是一个日期时间控件，但是这里的信号只是日期改变
        self.datetime_1.dateChanged.connect(lambda :print('Date Changed!'))

        # 这里通过QDateTime.currentDateTime()为self.datetime_2设置当前时间
        # 否则是默认2000-01-01 00:00:00
        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        # 为self.datetime_2的显示设为'yyyy-MM-dd HH:mm:ss'这个格式
        self.datetime_2.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        # 信号是时间发生改变
        self.datetime_2.timeChanged.connect(lambda :print('Time Changed!'))
        print(self.datetime_2.date())
        print(self.datetime_2.time())
        print(self.datetime_2.dateTime())

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        # 这个的信号是日期时间，只要其中任意发生改变就启动槽函数
        self.datetime_3.dateTimeChanged.connect(lambda :print('DateTime Changed!'))
        # QDateTimeEdit.setCalendarPopup(bool),为True就是设置日历弹窗，，默认是False
        self.datetime_3.setCalendarPopup(True)

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self) # 只传入当前日期
        self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self) # 只传入当前时间

        self.date = QDateEdit(QDate.currentDate(), self)
        self.date.setDisplayFormat('yyyy/MM/dd')
        print(self.date.date())

        self.time = QTimeEdit(QTime.currentTime(), self)
        self.time.setDisplayFormat('HH:mm:ss')
        print(self.time.time())

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)
        self.v_layout.addWidget(self.date)
        self.v_layout.addWidget(self.time)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())