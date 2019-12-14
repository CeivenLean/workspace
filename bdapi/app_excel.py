import os,math,time
import app 

client = app.getClient()

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('/Users/xxxl/VSProjects/workspace/bdapi/1.jpg')
print(type(image))


# # #从识别结果json里取出表头
# word = ''
# result_json = client.tableRecognition(
#     image,
#     {
#         'result_type': 'json',
#     },
# )
# word = eval(result_json['result']['result_data'])['forms'][0]['header'][0]['word']

# excel_url = ''
# result_excel = client.tableRecognition(
#     image,
#     {
#         'result_type': 'excel',
#     },
# )
# excel_url = result_excel['result']['result_data']

# print("table_name,table,url:",word,excel_url)
# timeout = 10000
# options = {}
# options["result_type"] = "json"
# """ 调用表格文字识别 """
# result = client.tableRecognitionAsync(image)
# # # #print(result)
# request_id = result['result'][0]['request_id']
# # # #print(request_id)
# word = ''
# for i in range(int(math.ceil(timeout / 1000.0))):
#     result = client.getTableRecognitionResult(request_id, options)  
#     # 完成
#     if int(result['result']['ret_code']) == 3: 
#         break
#     time.sleep(1)
# word = eval(result['result']['result_data'])['forms'][0]['header'][0]['word']

# excel_url = ''
# options["result_type"] = "excel"
# for i in range(int(math.ceil(timeout / 1000.0))):
#     result = client.getTableRecognitionResult(request_id, options)  
#     # 完成
#     if int(result['result']['ret_code']) == 3: 
#         break
#     time.sleep(1)
# excel_url = result['result']['result_data']
# print("table_name,table,url:",word,excel_url)

# options["result_type"] = "excel"
# r2 = client.getTableRecognitionResult(request_id,options)

# excel_url = ''
# while r2['result']['ret_code']==3:
#     excel_url = r2['result']['result_data']
# print(excel_url)
# """ 同步获取表格识别 返回识别结果 
# r2 = client.tableRecognition(
#     image,
#     {
#         'result_type': 'excel',
#     },
# )
# print(r2)
# """



# 下载
# import requests 
# r = requests.get(excel_url)
# with open(os.path.dirname(__file__)+'/'+word+".xls", "wb") as code:
#     code.write(r.content)
