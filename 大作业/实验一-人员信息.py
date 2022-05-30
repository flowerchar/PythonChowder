import openpyxl
import jieba
import wordcloud
import sys
import os
from collections import Counter
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QGroupBox, QLineEdit,\
    QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QSpinBox


class ExperimentOne(QWidget):

    def __init__(self):
        super().__init__()
        # 初始化必要属性
        self.wbook = openpyxl.load_workbook(r'souce/人员信息.xlsx')
        self.wbook_sheet1 = self.wbook['Sheet1']
        self.name_list = []
        self.telephone_list = []
        self.cell = 2
        self.all_introduction = ''
        # 初始化PyQt5部件
        self.groupBox_font = QGroupBox('词云字体设置', self)
        self.hwfs_radio = QRadioButton('华文仿宋', self)
        self.hwxk_radio = QRadioButton('华文行楷', self)
        self.hwhp_radio = QRadioButton('华文琥珀', self)
        self.groupBox_cutmode = QGroupBox('jieba分词模式', self)
        self.lcut_radio = QRadioButton('精确模式', self)
        self.lcut_cutall_radio = QRadioButton('全模式', self)
        self.cut_for_search_radio = QRadioButton('搜索引擎模式', self)
        self.confirm_button = QPushButton('确定', self)
        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(10, 200)
        self.spinBox_label = QLabel('设置词云图的词数量：', self)
        self.height_edit = QLineEdit(self)
        self.width_edit = QLineEdit(self)
        self.height_edit.setPlaceholderText('在此处编辑高度，单位px，1500左右为佳')
        self.width_edit.setPlaceholderText('在此处编辑长度，单位px，2000左右为佳')
        self.h1_layout = QHBoxLayout(self)
        self.h2_layout = QHBoxLayout(self)
        self.h3_layout = QHBoxLayout(self)
        self.h4_layout = QHBoxLayout(self)
        self.v1_layout = QVBoxLayout(self)
        self.v2_layout = QVBoxLayout(self)
        self.all_v_layout = QVBoxLayout(self)
        self.font_list = [self.hwhp_radio, self.hwxk_radio, self.hwfs_radio]
        self.mode_list = [self.lcut_radio, self.lcut_cutall_radio, self.cut_for_search_radio]
        self.height_label = QLabel('<b style="color:red;">编辑词云图高度</b>', self)
        self.width_label = QLabel('<b style="color:red;">编辑词云图长度</b>', self)
        self.messageBox = QMessageBox.information(self, '提示框',\
                                      '在做完xlsx后，会生成一个前十个出现次数最多的词云图，可以设置三点：\n1.词云图的字体格式\n2.jieba的分词模式\n3.词云图的长度和高度\n4.词云图里的词数量'\
                                                  , QMessageBox.Yes)
        self.setWindowTitle('实验作业一')
        self.setWindowIcon(QIcon(r'souce/nau.jpg'))
        self.resize(800, 600)

        self.layout_init()
        self.QtWidget_init()
        self.show()

    def layout_init(self):
        '''
        布局处理
        :return:
        '''
        self.v1_layout.addWidget(self.height_label)
        self.v1_layout.addWidget(self.height_edit)

        self.v2_layout.addWidget(self.width_label)
        self.v2_layout.addWidget(self.width_edit)

        self.h1_layout.addWidget(self.hwfs_radio)
        self.h1_layout.addWidget(self.hwxk_radio)
        self.h1_layout.addWidget(self.hwhp_radio)

        self.h2_layout.addWidget(self.lcut_radio)
        self.h2_layout.addWidget(self.lcut_cutall_radio)
        self.h2_layout.addWidget(self.cut_for_search_radio)

        self.h3_layout.addLayout(self.v1_layout)
        self.h3_layout.addLayout(self.v2_layout)

        self.h4_layout.addWidget(self.spinBox_label)
        self.h4_layout.addWidget(self.spinBox)

        self.groupBox_font.setLayout(self.h1_layout)
        self.groupBox_cutmode.setLayout(self.h2_layout)

        self.all_v_layout.addWidget(self.groupBox_font)
        self.all_v_layout.addStretch(1)
        self.all_v_layout.addWidget(self.groupBox_cutmode)
        self.all_v_layout.addStretch(1)
        self.all_v_layout.addLayout(self.h3_layout)
        self.all_v_layout.addStretch(1)
        self.all_v_layout.addLayout(self.h4_layout)
        self.all_v_layout.addStretch(1)
        self.all_v_layout.addWidget(self.confirm_button)

        self.setLayout(self.all_v_layout)

    def QtWidget_init(self):
        '''
        让确定键不可用
        :return:
        '''
        self.confirm_button.setEnabled(False)
        self.height_edit.textChanged.connect(self.check_confirm_button_cha)
        self.width_edit.textChanged.connect(self.check_confirm_button_cha)
        self.confirm_button.clicked.connect(self.do_xlsx)

    def check_confirm_button_cha(self):
        '''
        检查两个编辑行是否有输入
        :return:
        '''
        if self.width_edit.text() and self.height_edit.text():
            self.confirm_button.setEnabled(True)

    def do_xlsx(self):
        '''
        用来完成xlsx的方法
        :return:
        '''
        # 从A列取出姓名，电话
        for col in list(self.wbook_sheet1.columns)[0][1:]:
            # 取到电话
            telephone = col.value[-11:]
            # 取到不含空白字符和以：结尾的名字
            pure_name = col.value[:-11].strip()
            if pure_name[-1] == '：':
                pure_name = pure_name.replace('：', '')

            self.name_list.append(pure_name)
            self.telephone_list.append(telephone)

        # 将名字添加到b列
        for name in self.name_list:
            self.wbook_sheet1[f'b{self.cell}'] = name
            self.cell += 1
        self.cell = 2

        # 将名字添加到c列
        for telephone in self.telephone_list:
            self.wbook_sheet1[f'c{self.cell}'] = telephone
            self.cell += 1
        self.wbook.save('修改后的人员信息.xlsx')

        # 按照选的单选按钮的不同，设置不同的模式或者字体
        for introduction in list(self.wbook_sheet1.columns)[3][1:]:
            self.all_introduction += introduction.value
        if self.lcut_radio.isChecked():
            cut_word = jieba.lcut(self.all_introduction)
        elif self.lcut_cutall_radio.isChecked():
            cut_word = jieba.lcut(self.all_introduction, cut_all=True)
        else:
            # 这里是生成器，需要强制转为list！！
            cut_word = list(jieba.cut_for_search(self.all_introduction))
        if self.hwfs_radio.isChecked():
            font = 'STFANGSO.TTF'
        elif self.hwxk_radio.isChecked():
            font = 'STXINGKA.TTF'
        else:
            font = 'STHUPO.TTF'
        count = Counter(cut_word)
        # 因为不同的分词模式会取到不同数量的标点符号，那么就把出现次数最多的几个数字范围放大，从而避免
        most_common_20 = count.most_common(20)
        # current代表是当前词语的序号，排在第几
        current = 1
        most_common_10 = ''
        # print(most_common_20)
        for number in most_common_20:
            if number[0] == '，' or number[0] == '。' or number[0] == '、' or number[0] == ' ':
                continue
            if current == 11:
                break
            single_word = f'{number[0]} 排在第{current}个出现了{number[1]}次'
            print(single_word)
            current += 1
            most_common_10 += single_word + '\n'
        # print(1)
        # print(cut_word)
        # print(2)
        text = ' '.join(cut_word)
        # print(text)
        # 这里一定要转换类型！！！！
        cloud = wordcloud.WordCloud(background_color='black', width=int(self.width_edit.text()), \
                                    height=int(self.height_edit.text()), \
                                    font_path=font, max_words=int(self.spinBox.text())).generate(text)
        cloud.to_file('词云图.jpg')
        QMessageBox.information(self, '提示框', f'生成的词云图已保存到{os.getcwd()}目录里\n'+most_common_10, QMessageBox.Ok)
        self.confirm_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    One = ExperimentOne()
    sys.exit(app.exec_())

