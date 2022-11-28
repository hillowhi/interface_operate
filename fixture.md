### fixture 的定义用法

> 类似于setup前置函数 每个引用了fixture函数的测试用例在执行之前调用该函数
> 则自动调用该fixture函数，fixture函数不用导入 可以直接引用 

#### fixture函数的定义
在声明函数前修饰 @pytest.fixture 则声明该函数为fixture函数 
一般fixture函数是数据处理后返回测试用例需要的数据，基本可以当作是前置函数用
eg: 
- @pytest.fixture
- def pytest_fixture() 
- 则pytest_fixture()函数为fixture函数
#### fixture函数的引用
在定义测试用例函数时 将fixture函数的函数名作为测试函数的参数 即 fixture函数的参数返回值作为测试函数的入参
- @pytest.fixture
- def pytest_fixture()
-   return a  
- def test_fixture(pytest_fixture)  将pytest_fixture函数的函数名作为测试函数的参数,即将返回值a 作为该测试用例的参数
#### fixture函数的作用域
> autouse 参数默认是False 设置为True的时候 就会默认该模块下所有的测试函数都默认引用了该fixture函数，不用通过传参去引用
> ps:ui自动化可能会不灵 至于为啥不灵还不知道

- @pytest.fixture(autouse =True)

> scope 指定fixture函数的作用域 

@pytest.fixture(autouse =True,scope ='session') 括号里() 可指定参数 也可以不指定

- session项目级别(每个session调用一次)>module(每个py文件调用一次)>class(如果有类和非类方法同时存在 
  则方法也会被认为是一个类 也会调用)>function

#### conftest.py  pytest指定的固定的fixture配置文件 可以用来导入外部插件 或者指定hook函数 不用导入可直接引用 作用域是所在目录及其子目录文件
>- 1.conftest.py文件名称不可更改
- 2.conftest.py文件要放在根文件夹（用例的根文件夹）
- 3.conftest.py夹下方要存在__init__.py文件
- 4.在调用conftest文件中的方法时，可以在方法中直接传递方法名即可
- 5.autouse=True表名该方法无需输入对应的方法名即可调用
- 6.scope=‘module’ 作用域的范围在.py文件。每个.py文件只调一次

#### 关键字 yield 用在fixture函数里 用来声明后置函数 后可接返回值，可当作return返回  这时候声明函数的@pytest.fixture()要加()
- @pytest.fixture()
- def test_fixture()
-   a=a+1 (前置运行函数体)
-    yield a (test_fixture返回值)
-    print(a--) (函数的后置运行体，运行完前置体后会打印a)


