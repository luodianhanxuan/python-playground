# #########################################   Level 1   #####################################
# def decorator1(func):
#     def warp():
#         print('before')
#         func()
#         print('end')
#
#     return warp
#
#
# @decorator1
# def hello1():
#     print('hello')
#
#
# print(hello1)
# hello1()
#
#
# # 由此得出：调用被装饰者函数装饰的函数时， @ 符号作用：打断原始函数的调用效果
# # ，将被装饰的函数对象作为参数传入装饰者函数并得到一个被装饰的函数，然后解释器继续往下运行
#
# #########################################   Level 2   #####################################
def decorator2(f):
    def wrap(name):
        print('before')
        f(name)
        print('end')

    return wrap


@decorator2
def hello2(name):
    print('hello ' + name)


hello2('world')

#
#
# 解释器 hello2 对象时发现有 @ 符号，则根据 @ 后的定义寻址装饰者函数对象，
# 得到装饰者函数对象后将 hello2 函数对象作为参数调用装饰者函数对象，
# 得到返回值（返回值还是函数），在返回值的基础上程序继续执行('world') 调用
#
# 由此得出：至此上面的结论依然站的住脚
#
#
# #########################################   Level 3   #####################################
# def decorator3(label):
#     print("标签" + label + "被调用")
#
#     def dec(func):
#         def wap(name):
#             print('before')
#             func(name)
#             print('end')
#
#         return wap
#
#     return dec
#
#
# @decorator3('abc')
# def hello3(name):
#     print('hello ' + name)
#
#
# hello3('world')

# 解释器执行到 hello3 ，发现 @ 符号，则通过 @ 后面的定义去获取装饰者函数对象，
# 发现依然是个函数，则调用函数 decorator3('abc') 得到装饰器函数对象，
# 得到装饰者函数对象后将 hello3 函数对象作为参数调用装饰者函数对象，
# 得到返回值（返回值还是函数），在返回值的基础上程序继续执行('world') 调用

'''
结论：

@ 符号的作用：
打断原始函数的调用效果
通过 @ 符号后面的定义获取装饰者函数对象，
将被装饰的函数对象作为参数传入装饰者函数并得到一个被装饰的函数，然后解释器继续往下运行

获取装饰者函数对象的方式有两种：
1. 通过函数定义。          比如  @decorator
2. 通过运行一个函数得到返回值作为装饰者函数对象。      比如@decorator('abc')

'''
