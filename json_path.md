### jsonpath表达式的格式规范 只用于字典返回数据类型  jsonpath获取结果返回类型是list格式
> $表示从根节点开始

> .表示获取子节点

> ..表示获取所有符合条件的内容

> *表示所有元素节点 
>data = jsonpath.jsonpath("$.book[?(@.price>10)]")  只返回price
>data = jsonpath.jsonpath("$.*[?(@.price>10)]")  返回所有符合条件的所有节点
 

>[]表示迭代器的标示

>[,]表示多个结果的选择

>?()表示过滤操作  例如:获取价格>10的price返回值
> data = jsonpath.jsonpath("$.book[?(@.price>10)]") 

>@表示当前节点 data = jsonpath.jsonpath("$.book[?(@.price>10)]")
> @指的就是book节点