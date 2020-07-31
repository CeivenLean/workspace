import requests
import re


res = requests.get("https://www.todesk.com/download.html")

res.encoding = "utf-8"

t = re.search(r"<div class=\"bj_first\"(.*?)<div class=\"bjk\"", res.text, re.DOTALL)
#print(t)
t1 = t.group(1)
#print(t1)
t2 = re.search(r"<li.*>(.*)</li>", t1, re.DOTALL)
print(t2.group())