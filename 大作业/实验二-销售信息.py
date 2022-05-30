import pandas as pd
import matplotlib.pyplot as plt

# 1.这里首先报错缺失xlrd
# 2.安装了xlrd后，依然报错，是因为版本太新了，不再支持xlsx的格式
# 3.安装了1.2版本后，再次报错'ElementTree' object has no attribute 'getiterator'，需要到python\Lib\site-packages\xlrd下的xlsx.py文件，改源代码
# 过于复杂了，一个更好的解决方法是engine='openpyxl'，让openpyxl代替xlrd打开文件
Salse_Sheet1 = pd.read_excel(r'souce\销售信息.xlsx', 'Sheet1', engine='openpyxl')
# print(Salse_Sheet1)
# 可以看到18行与10行重复
# 24,25行与15行重复
# s = Salse_Sheet1.duplicated()
# print(s)
Salse_Sheet1 = Salse_Sheet1.drop_duplicates()
# 用缺失值的前一项填补
Salse_Sheet1.loc[:, '水杯'] = Salse_Sheet1['水杯'].fillna(method='ffill')
Salse_Sheet1.loc[:, '手套'] = Salse_Sheet1['手套'].fillna(method='ffill')
# 去掉pandas自带的索引号,否则不会显示第16列
Salse_Sheet1 = Salse_Sheet1.reset_index(drop=True)
# print(Salse_Sheet1)
index_row = Salse_Sheet1.index
# 因为是要分组里个商品的销售总和，那么场次编号这一列就没有必要显示出来
part_sum = Salse_Sheet1.groupby('活动编号', as_index=False).sum().drop(columns=['场次编号'])
print(part_sum)
Mouse_data = Salse_Sheet1['鼠标']
Keyboard_data = Salse_Sheet1['键盘']
# 鼠标的最大值有两个，所以不显示；键盘的最小值有两个；不显示
Max_Keyboard_y = Keyboard_data.max()
Max_Keyboard_x = 16
Min_Mouse_y = Mouse_data.min()
Min_Mouse_x = 5
# 必须要加这两行代码，不然会出现中文乱码，以及负号不能正常显示
plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['axes.unicode_minus']=False
plt.title('鼠标与键盘销售对比折线图', fontsize=24, backgroundcolor='brown')
plt.xlabel('索引号', fontsize=14)
plt.ylabel('销售数量', fontsize=14)
# 设置线宽，标记，标记点
plt.plot(index_row, Mouse_data, linewidth=2, label='鼠标', marker='1')
plt.plot(index_row, Keyboard_data, linewidth=2, label='键盘', marker='H', color='g')
# 让刻度线显示更加清晰
plt.tick_params(axis='both', labelsize=14, direction='inout', color='r', width=2, length=8)
# 绘制标签在右下角
plt.legend(loc=4, fontsize=14, shadow=True)
# 无箭头版
# plt.text(Max_Keyboard_x, Max_Keyboard_y+1, f'键盘Max:{Max_Keyboard_y}', fontsize=14, color='g', alpha=1)
# plt.text(Min_Mouse_x, Min_Mouse_y-2, f'鼠标Min:{Min_Mouse_y}',fontsize=14, color='#1F77B4', alpha=1)
# 这里为了适配，并且不能遮住其他折线图，所以需要调整文本的坐标值
plt.annotate(f'鼠标Min:{Min_Mouse_y}', color='#1F77B4',xy=(Min_Mouse_x, Min_Mouse_y), xytext=(Min_Mouse_x+0.3, Min_Mouse_y-7),
             arrowprops=dict(facecolor="#1F77B4",shrink=0.05,headwidth=12,headlength=6,width=4),fontsize=12)
plt.annotate(f'键盘Max:{Max_Keyboard_y}', color='g', xy=(Max_Keyboard_x, Max_Keyboard_y), xytext=(Max_Keyboard_x-3, Max_Keyboard_y+5),
             arrowprops=dict(facecolor="g",shrink=0.05,headwidth=12,headlength=6,width=4),fontsize=12)
plt.grid(b=True, linestyle='-.')
Salse_Sheet1.to_excel(f'修改后的销售信息.xlsx', index=False)
plt.show()