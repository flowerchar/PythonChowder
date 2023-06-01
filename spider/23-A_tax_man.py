import requests
import json

def get_A_tax_man(pageNo:int=667, pageSize:int=15)->dict:
    '''
    A级纳税人的识别号和名称，默认返回全部数据
    :param pageNo: 查询第几页
    :param pageSize: 每次查询多少家
    :return: 字典，包括list和size字段
    '''
    total = 0
    all_A_list = []
    url = 'https://guizhou.chinatax.gov.cn/irs/front/list'
    for i in range(1,pageNo):
        data = {
        "pageNo": i,
        "pageSize": pageSize,
        "tenantId": 71,
        "tableName": "t_17e6b2c59ad",
        "searchFields": [
            {
                "fieldName": "f_2022118461091",
                "searchWord": "2021"
            }
        ],
        "sorts": [
            {
                "sortField": "save_time",
                "sortOrder": "DESC"
            }
        ],
        "customFilter": {
            "operator": "or",
            "properties": [
                {
                    "property": "f_202211853800",
                    "operator": "eq",
                    "value": "5929700"
                }
            ]
        },
        "channelId": "5929700",
        "isPage": "true"
    }
        res = requests.post(url, json=data)
        res = res.json()
        for j in res["data"]["list"]:
            all_A_list.append({"id": j["f_2022118981169"], "name": j["f_2022118439324_ext"]})
            total += 1
    Info = {"list":all_A_list, "size": total}
    return Info

def keep_in_json(Info:dict)->None:
    with open("A_TAX.json","w")as fp:
        json.dump(Info, fp)

def get_info(path:str)->dict:
    with open("A_TAX.json","r")as fp:
        Info = json.load(fp)
    return Info
keep_in_json(get_A_tax_man())
print(get_info("A_TAX.json"))