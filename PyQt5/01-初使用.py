import sys
from PyQt5 import QtWidgets, QtCore
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    try:
        if len(sys.argv)<2:
            raise ValueError
        else:
            title = ''.join(sys.argv[1:])
    except ValueError as e:
        print(e)
        title = 'flowerchar'
    # print(sys.argv[0])
    # print(sys.argv[0].replace('/',r'\\'))
    widget = QtWidgets.QWidget()
    widget.resize(400,100)
    widget.move(0,0)
    widget.setWindowTitle(title)
    widget.show()
    exit(app.exec_())
