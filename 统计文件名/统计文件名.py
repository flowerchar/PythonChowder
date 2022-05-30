import os
import re
import openpyxl
current_work_path = os.getcwd()
file_location = current_work_path+r'\txt'
file_names = 0
invalid_information = []
for root, dirs, file_names in os.walk(file_location, topdown=False):
    print(file_names)
 # 7461总文件数量
company_info = []
company_name_pat = r'\..+?：'
company_activity_pat = r'：.+.txt'
# 第一个匹配[临时公告] 第二个匹配公司前面的杂乱信息 第三个匹配公司后面可能出现的无效数字
pure_company_name_pat = r'\[临时公告\]|\s*?\.\d\s*?\.\s*?|\.\s*?\d\s*?无法复制\s*?\.\s*?|\s*?\d*?\s*?：|\.\d\s*?'
pure_company_acivity_pat = r'\s*?：\s*?|\s*?\.txt\s*?'
# 过滤不好处理的数据后，还剩7421条
after_filter_sum = 0
for i in file_names:
    time = i[:4:]
    try:
        company_name = re.findall(company_name_pat, i)[0]
        company_activity = re.findall(company_activity_pat, i)[0]
    except:
        # print('有一条不规则信息')
        invalid_information.append(i)
        continue
    pure_company_name = re.sub(pure_company_name_pat, '',company_name)
    pure_company_acivity = re.sub(pure_company_acivity_pat, '', company_activity)
    # print(pure_company_name, time, pure_company_acivity)
    company_info.append((pure_company_name, time, pure_company_acivity))
    after_filter_sum += 1
company_info.sort()


xlsx_name = r'统计文件名.xlsx'
my_workbook = openpyxl.load_workbook(current_work_path+rf'\{xlsx_name}')
my_workbook_worksheet = my_workbook['Sheet1']
# +5是从xlsx里写入的第一行，
for index, value in enumerate(company_info[2::]):
    print(value)
    my_workbook_worksheet[f'a{index+5}'] = value[0]
    my_workbook_worksheet[f'b{index+5}'] = value[1]
    my_workbook_worksheet[f'd{index+5}'] = value[2]
my_workbook.save(current_work_path+fr'\修改后的{xlsx_name}')

print(invalid_information)

print(current_work_path)
with open(current_work_path+r'\无效的公司信息.txt','w',encoding='utf8') as fp:
    for i in invalid_information:
        fp.write(i+'\r\n')
