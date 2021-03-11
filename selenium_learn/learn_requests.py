import requests
# get请求
req1 = requests.get("http://www.baidu.com")
# post请求，传递
req2 = requests.post("http://httpbin.org/post", data={"key": 'value'})
# 状态码
print(req1.status_code)
# 编码
print(req1.encoding)
req1.encoding = 'utf-8'
# 获取返回的内容
print(req1.text)
