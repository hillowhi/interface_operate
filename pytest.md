# pytest 运作机制
> - pytest 可以声明类 也可以不声明直接声明函数
>- pytest将在当前目录及其子目录中运行所有格式为test_*.或者 *_test.py文件
>- 测试方法(类里定义的函数叫方法，类外面定义叫函数)、测试函数必须以test开头
>- 测试类必须以Test开头
>- 测试类不能有__init__构造方法

### pytest的断言机制
>-  pytest 的断言机制就是python算术运算符 + - * /  或者逻辑运算符(!= ,==, <=, is true,is not true ) 加上assert实现
> - eg：assert except_response == return_response  return_response is true

### pytest用例批跑机制 定义在main函数里 
> if __name__ == '__main__':
> pytest.main(['参数配置'])

>   ####常用配置详情：
    # -s输出打印信息到控制台 -v输出更详细的用例信息
    # 更多关键词配置 可以到dos系统里 pytest --help
    # 运行包含某个关键字的用例 -k,'关键字'
    # -q 简化输出信息
    # -x 一条用例失败 则退出运行 pytest.main(['-x'])
    # 运行指定目录下的某个类或者某个类下的用例 pytest.main(['-s','相对于当前目录文件的地址'])
    # 相对于当前目录文件的路径表达：'/test_child_package::TestCase1::test_class_case'  类/方法都要用::双冒号隔开
    # 生成xml测试报告 --junit-xml=./report/junit_report01.xml
    # 允许最大用例失败数 pytest.main(['--maxfail==2']) 当出现2个失败用例时 则退出用例执行
    # 运行指定装饰器标记的用例 pytest.main(['-m', 'smoke']) smoke 是装饰器，-m 意思是mark
    '''
    装饰器 标记的 标记必须在pytest.init 文件中自定义 在当前文件根目录下创建init文件
    '''
    # 多进程运行用例 pytest.main(['2','-n','test_assert.py'])  指定两个cpu跑用例 pytest版本太高跑不起来
    # pytest.main(['2', '-auto', 'test_assert.py']) #跟运行电脑内核一样跑用例
    # 失败重试插件 pytest_failures 只支持python3.5以上，pytest5.0以上版本
    # pytest.main(['--reruns', '3', 'test_failures.py'])  # 指定失败的用例重跑次数3，每次有用例失败就重跑3次
    # pytest.main(['--reruns', '3', '--reruns-delay', '2', 'test_failures.py'])  # 失败延迟 重跑失败用例之前延迟2S
    # 文件内用例运行的前置后置函数 setup_module(moduel)  teardown_module(moduel) 运行该测试文件前和结束后会运行这两个函数 函数体自定义print
    # 函数内用例运行的前后内置函数 setup_function(function) teardown_function(function) 
    # (接上一行 )每个用例函数执行前后执行 这两个函数同 setup() teardown()一样 只是为了兼容版本变化 如果这俩同时存在先运行setup_function
    # 前置后置函数很有用，比如执行以下用例时必须满足什么条件 比如：启动某个浏览器 或者去拿某个随机值  哇！好棒！
    # 除此之外 还有类里定义的前后置函数 setup_class(cls) teardown_class(cls) 函数前需要用@classmethod 修饰

### pytest的init文件常用配置(文件作用范围：所在目录及其子目录)：
    - 配置文件中如果含有中文(尽量不要用)，应该转码 file - file properties -file encoding  改为GBK编码
    - addopts = -v -s --html=./report/html_report.html  命令行参数 默认加到执行过程中
    - testpath = ./package_name 运行指定测试文件目录
    - python_files = auto*.py 指定要运行的测试文件名规则
    - python_classes = Auto_* B_* 指定要运行的类名规则 可以指定多个规则 中间用，隔开
    - python_functions  = auto_* 指定要运行的测试用例名称规则 
