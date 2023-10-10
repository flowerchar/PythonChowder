import requests
from lxml import etree
def get_name(name_list:list)->list:
    new_list = []
    for i in name_list:
        new_list.append(i.split('/')[-1])
    return new_list

USERNAME = 'flowerchar'
EXCLUDE = ['example','pythonGame','fun-rec', 'PrivateNotes','JavaGuide', 'Python-crawler-tutorial-starts-from-zero', 'snake', 'PyQt5', 'zju_cmooc']
PAGES = 2
path = '//*[@id="user-repositories-list"]//h3/a/@href'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookies':'_octo=GH1.1.1549628366.1666595533; _device_id=d06dfcede7f563ed35a1465bb18a86ac; user_session=TkmYrdBOzr56J-W4p3onbAzj-WxdvpnZ4iHes_4q_gtX8Y4T; __Host-user_session_same_site=TkmYrdBOzr56J-W4p3onbAzj-WxdvpnZ4iHes_4q_gtX8Y4T; logged_in=yes; dotcom_user=flowerchar; fileTreeExpanded=true; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=v8CZz41D37%2F9u3CIz1IdLCjqzSsOhAwgbuZ7HlXYsG8J0EioIM47WXDEA6BZAIdP%2FR6zlwba7bXbxuYG8C169yGBrHxdGBrtk8VJhfMNishrC74wp5b7lo%2BXoqJlcDyCV1t0hDisStP7PPkxNttuakDoFyJwCZyxNdGHRWGskT%2Bhlq2oBlBaxNP8y0n58k8uC8u7qZAUM4yCnEeBlElOJ7UyYzyhnWbnHgVDqkWapnMiDCt5OyzN4h3KZCk%2Flmu4OLfG60kc8g167xND2QQwdP5EIFB34BxuHQph%2BCdGWIM0gbzGAyyfJoMy0X6yE6KU7Ghrtw%3D%3D--1LzVbA4mr1qKDf7P--Vd4b6hdiXlvcCSZtPzC4hw%3D%3D'
}
proxies = {
    'http': 'http://127.0.0.1:7890/',
    'https': 'http://127.0.0.1:7890/'
}
total_name_list = []
for i in range(1,PAGES+1):
    url = f'https://github.com/{USERNAME}?page={i}&tab=repositories'
    resp = requests.get(url=url, proxies=proxies, timeout=20)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    name_list = html.xpath(path)
    total_name_list += get_name(name_list)

print(total_name_list)
