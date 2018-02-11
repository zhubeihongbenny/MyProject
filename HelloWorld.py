# coding=utf-8

from PythonPackage.HelloWorldSupport import *
from PythonPackage.Collection import *
from builtins import set
from PythonPackage.Pickle import *
from multiprocessing import sys
from sys import *

# def SayHello():
#     print ("hello, world")

# def Max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

store = 80

if store >= 80:
    print("很好")
elif store >= 70:
    print("尚可")
else:
    print("不及格")

for i in range(0, 100):
    print("item {0},{1}".format(i, "hello python"))

SayHello()

print(Max(3, 2))

h1 = Hello("zhubeihong")
h1.SayHello()

h2 = Hi("zhulei")
h2.SayHi()

list1 = ["a", "b", "c", "d", "e", "f"]
h3 = GetList(list1, 5)
h3.ListPrint()

# 定义集合
setA = set("abcc")
setB = set("acde")

# 交集
setX = setA & setB

# 并集
setY = setA | setB

# 差集
setZ = setB - setA

# 去除重复元素
setNew = set(setA)

# 字典
dicA = {"名前": "朱倍宏", "出身": "上海"}
dicB = {"年齢": "36"}

print(setX)
print(setY)
print(setZ)
print(setNew)
print(dicA.keys())
print(dicA.values())
print(dicA["名前"])
print(dicA.get("出身"))
print(dicA.copy())
print(dicA.clear())
print(dicA.items())

# 对象
print("")
print("对象")
list2 = ["a", "b", "c"]
p1 = UsingPickle(list2)
p1.PickleProcess()

# 余数
print()
print("余数")
print(5 % 3)

# 幂运算
print()
print("幂运算")
print(2 ** 3)

# while
print()
print("WHILE")
whileA = 1
while whileA < 10:
    if whileA <= 5:
        print(whileA)
    else:
        print("hello")
    whileA = whileA + 1
else:
    print("over")

# 文档字符串
print()
print("文档字符串")
Hi.Doc.__doc__
help(Hi.Doc)

# sys模块
print()
print("sys模块")
print(sys.version)
print(sys.getwindowsversion())
print(sys.modules.keys())

# name属性，判断该模块是不是主模块
print()
print("name属性，判断该模块是不是主模块")
if __name__ == "__main__":
    print("该模块是主模块")
else:
    print("该模块不是主模块")


# dir()函数
d = []
print(dir(d))
