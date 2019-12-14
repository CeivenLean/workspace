from app import translateConfig
import hashlib
import requests

APPID, MIYUE = translateConfig()
request_url = "https://fanyi-api.baidu.com/api/trans/vip/translate"

#print(APPID, MIYUE)

q = input("输入词：")

from_type = "zh"
to_type = "en"

salt = "14356665613541358578700288"

signstr = APPID+q+salt+MIYUE
print(signstr)

hl = hashlib.md5()
hl.update(signstr.encode(encoding='utf-8'))
sign = hl.hexdigest()
#sign = hashlib.md5(signstr.encode("utf-8")).hexdigest()
print(sign,len(sign))

params_dic = {
    'q': q,
    'from': from_type,
    'to': to_type,
    'appid': APPID,
    'salt': salt,
    'sign': sign
}

resp = requests.get(request_url, params=params_dic)
print(resp.text)