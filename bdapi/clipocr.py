import os,math,time
import app 
from PIL import ImageGrab
from PIL import Image
import io

client = app.getClient()

# Pull image from clibpoard
# return PIL Image
img = ImageGrab.grabclipboard()

# Convert PIL Image to Byte(eg: b'....' )
imgByteArr = io.BytesIO()  
img.save(imgByteArr, format='PNG')  # PNG就是图片格式，我试过换成JPG/jpg都不行
imgByte = imgByteArr.getvalue() #这里转换后就是b''格式的数据
# print(imgByte)

result = client.basicAccurate(imgByte)
words_array = result['words_result']
#print(words_array)
for i,j in enumerate(words_array):
    print(j['words'])