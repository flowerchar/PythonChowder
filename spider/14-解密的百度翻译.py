import requests
import execjs

url = ''
with open('js/1.js',mode='r',encoding='u8') as fp:
    js_code = fp.read()
js_obj = execjs.compile(js_code)
js_obj_func = js_obj.call('e')