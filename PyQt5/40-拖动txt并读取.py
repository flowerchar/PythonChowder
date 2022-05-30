import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser

# 继承至QTextBrowser，也就是下面实现该控件的拖放事件及函数
class Demo(QTextBrowser):

    def __init__(self):
        super(Demo, self).__init__()
        # QTextBrowser.setAcceptDrops(bool)，为True则让控件接收放下事件
        self.setAcceptDrops(True)

    # 只要目标有一丝进入QTextBrowser，就会触发该事件
    def dragEnterEvent(self, QDragEnterEvent):
        print('Drag Enter')
        # 先判断进入目标的类型是否为text/plain
        if QDragEnterEvent.mimeData().hasText():
            # 如果是,调用QDragEnterEvent.acceptProposedAction()表明可以在QTextBrower上拖放
            QDragEnterEvent.acceptProposedAction()

    # 在进来之后，不放下继续拖动就触发
    def dragMoveEvent(self, QDragMoveEvent):
        print('Drag Move')

    # 只有完全离开才会触发
    def dragLeaveEvent(self, QDragLeaveEvent):
        print('Drag Leave')

    # 释放事件触发
    # 这个效果实现的方式是，通过dropEvent来获得当前目标的文件路径
    # 然后在用open打开文件所在路径，再设置，而不是直接把内容给放在上面
    def dropEvent(self, QDropEvent):
        print('Drag Drop')
        # QDropEvent.mimeData().text()获得的是文件的file:///形式的路径
        tet_path_init = QDropEvent.mimeData().text()
        print(tet_path_init)
        # 用replace去掉file:///
        tet_path = tet_path_init.replace('file:///', '')
        print(tet_path)
        with open(tet_path, 'r') as f:
            self.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())