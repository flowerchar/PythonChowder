import requests


# url = 'https://study.163.com/j/my/learnRecord.json?pageSize=5'
# headers = {
#     'user-agent':'mozilla/5.0',
#     'cookie':'EDUWEBDEVICE=d6d8c7bd87a44af9a335fde4a255f643; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; NTESSTUDYSI=094d6c02706a4a1b9b07fb5feec3b634; utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPVBDaXhILUJFMlBQUFlRcnZ4eFJoVTVTZi1lR0J5VEN6dVFSVlZXd0F5WmEmd2Q9JmVxaWQ9OGQ4YTJlNzAwMDAwMDIzODAwMDAwMDA1NjA0ODdlMTM=; eds_utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPVBDaXhILUJFMlBQUFlRcnZ4eFJoVTVTZi1lR0J5VEN6dVFSVlZXd0F5WmEmd2Q9JmVxaWQ9OGQ4YTJlNzAwMDAwMDIzODAwMDAwMDA1NjA0ODdlMTM=; hb_MA-BFF5-63705950A31C_source=www.baidu.com; __utmc=129633230; __utma=129633230.626998373.1604727517.1604727517.1615363606.2; __utmz=129633230.1615363606.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; STUDY_UUID=b2b305e9-ae36-4cba-a0a0-b34c6d0fcb1f; STUDY_NOT_SHOW_PROMOTION_DIALOG=true; NTES_YD_SESS=VyidxSSgJgcrIVd21Tvkl1ryTbe_rLnuURyZOpAossD0zSAkzfcxNLpM3mBgW3rDO9xCm7U_.N6T_iYrJWF0lT5CdIKR4SFajiNbRPBiqyVCkOe1p82ggd_d8BkFmHjcvMm2eLDJy7u7LCOphpa59CMicHu.peLG_J9YJVA1heCzvnA9vjdA_9DGovhCm3DsqtdThgJrLdt5t.Y52O3pdVJTMC0T00Ui4CfQIvYnxwXPW; NTES_YD_PASSPORT=ugvF10m.U.V2IuYqhZaYWPVnysY9DmQjm17zUWl7oPirsHBnse9N0vGWChtj2Cxya_NJhp1fm0V7iGmKzX4eGsGCYxRiBmleJr0yFgDTi6HejDAIT7Ah.VGfCO1jEadyQa4A6OOnOthk5iT4gJ2_w6hiqQoj6BgUbx_4KcvZSFazH49HR3FP3LdqxryWSBcGM6F9qBlQmrX_lacFWSuOfzLqi; S_INFO=1615363677|0|3&80##|19822636863; P_INFO=19822636863|1615363677|0|study|00&99|jis&1615101420&study_client#jis&320100#10#0#0|&0|null|19822636863; STUDY_INFO="yd.e7fd68fae3d34c28b@163.com|8|1409640230|1615363678122"; STUDY_SESS="oT1VBNemWKG+8VRDOHTgx9nk1ZaYYawgpsvIowNPlUTy1lY3KWMzVbn2f9zeXakOvVAgImo+r3s2bQ89R7hLMViMbSyySXDa4yTs9i6oOIxa63c/D/Y0Kl4J5RieP0KzseVe8FYtmKb8SdA6RElmGLacHSfEP+7KTE1EgVBAAsULhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="2YaKxjKoLi5CgEzTqvUM3x4iom6pJzQawTIPC1cg+cBt0c+kNHbJA6xt1wpRlRRfwJuwmTuYQ3mbxzcuWTMjto3x8sBasmHrshbCoJsncq/XV8MQ5a1qLmdezugGiWLVzIKnZePnR8dPBSc1BL4H8ynBTWacttk0uuUv1EOtOj2co/APStn7A63JKU8q8tjltAUUqcl9//QKSDP5hnbDw0GhWXeMTUypeqbgZBswWVjZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; DICT_SESS=v2|7XtJeJlPWBwuhMlMRfJz0QuhMzG0MQu0puRHqLPMgK0J4OLUGPLzf0lGOfPLRfquRUlO4zfOf6z0TLOMUm0fJyRU5nHlGh4wB0; DICT_LOGIN=1||1615363678185; NETEASE_WDA_UID=1409640230#|#1577631938790; NTES_STUDY_YUNXIN_ACCID=s-1409640230; NTES_STUDY_YUNXIN_TOKEN=9854a8729f6f2966df5c9c3c0d3bdbc1; __utmb=129633230.27.8.1615364504879'
# }
# resp = requests.post(url=url, headers=headers)
# print(resp.status_code)
# print(resp.text)
# print(resp.json())

session = requests.Session()

