# *args的用法：当传入的参数个数未知，且不需要知道参数名称时。
def func_arg(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)


func_arg(1, "youzan", 'dba', '四块五的妞')
print("-----------------------")


# 输出结果如下：
# formal arg: 1
# another arg: youzan
# another arg: dba
# another arg: 四块五的妞

# **args的用法：当传入的参数个数未知，但需要知道参数的名称时(立马想到了字典，即键值对)
def func_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("keyword arg: %s: %s" % (key, kwargs[key]))


func_kwargs(1, id=1, name='youzan', city='hangzhou', age='20', 四块五的妞是='来日方长的')
print('--------------------')


# 输出结果如下：
# formal arg: 1
# keyword arg: id: 1
# keyword arg: name: youzan
# keyword arg: city: hangzhou
# keyword arg: age: 20
# keyword arg: 四块五的妞是: 来日方长的


# 利用它转换参数为字典
def kw_dict(**kwargs):
    return kwargs


print(kw_dict(a=1, b=2, c=3))
# 输出结果如下：
# --------------------
# {'a': 1, 'b': 2, 'c': 3}
