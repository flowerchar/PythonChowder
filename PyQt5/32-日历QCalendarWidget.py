import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget,\
    QLabel, QVBoxLayout

EMOTION = {
    'Mon': '(╯°Д°)╯︵ ┻━┻',
    'Tue': '(╯￣Д￣)╯╘═╛',
    'Wed': '╭(￣▽￣)╯╧═╧',
    'Thu': '_(:з」∠)_',
    'Fri': '(๑•̀ㅂ•́) ✧',
    'Sat': '( ˘ 3˘)♥',
    'Sun': '(;′༎ຶД༎ຶ`)'
}


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1946, 2, 14))
        self.calendar.setMaximumDate(QDate(6666, 6, 6))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.show_emotion_func)

        print(self.calendar.minimumDate())
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)
        self.setWindowTitle('QCalendarWidget')

    def show_emotion_func(self):
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())