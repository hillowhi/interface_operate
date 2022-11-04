### request 库 文档地址：https://requests.readthedocs.io/en/latest/

>模拟接口请求：get,post,delete...
request.get() request.post()  

r= request.get() #获取到的是一个请求的返回类

>获取请求结果，不指定编码格式返回结果就是字节流可指定编码格式：

response = r.content 或者指定编码格式 r.content.decode(encoding="UTF-8")

>获取请求状态码：

r.status_code

>获取请求结果 输出结果编码格式由请求头里的编码格式(content_type)决定,返回结果是str类型：

r.text

>获取json类型请求结果 注意：这里引用的是json()方法,**返回类型是字典dict**,获取响应结果必须转换成字典类型:

r.json() 

>还有一种将返回结果转换成字典的方法：

dic_response = json.loads(r.text)

>反过来 将字典类型结果转换成json

json.dump


>获取返回结果的内存地址，例如 <urllib3.response.HTTPResponse object at 0x000001969BE15BB0>

print(r.raw)

### 通过响应结果查看响应信息

> r.request.url 获取请求url

> r.request.method 获取请求方法

>r.request.path_url 获取请求的接口路径 

>r.request.headers 获取请求头


### 新学到一个方法！！很棒！(ง •_•)ง r.raise_for_status()
用于捕捉请求异常 r = requests.get(url) 如果请求异常code在400-600之间 就会抛出异常



