### 用例参数化 
在用例执行前标记 @pytest.mark.parametrize('参数1,参数2,...',('值1,值2'),(('值1,值3'),...))
> - eg: 单个参数格式

@pytest.mark.parametrize('a',[(1),(2),(3),(4)]) # 该示例一共四个参数值,调用的用例会依次执行四次

> - eg: 多参数格式 

@pytest.mark.parametrize('a,b',[(1,2),(2,3),(3,4),(4,6)])

@pytest.mark.parametrize('a,b,login_data',[(1,2,{"empNumber": "012682","empPassword": "123456"}),
(1,2,{"empNumber": "012682","empPassword": "12345678"}),
(1,2,{"empNumber": "012688","empPassword": "666"}),
(1,2,{"empNumber": "012688","empPassword": "666"})])

>- eg:函数参数化格式

@pytest.mark.parametrize('a,b',get_data())  get_data()函数返回格式必须符合list里面包含元组
get_data()