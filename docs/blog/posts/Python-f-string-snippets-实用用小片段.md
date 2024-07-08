---
title: Python f-string snippets 实用小片段
tags: python
categories: [coding]
authors:
    - Alex
date: 
    created: 2022-09-20 21:52:06
    updated: 2024-07-08 21:09:11
---
# Python f-string

本文展示如何通过f-string格式化字符串。

##  Python f-string 实用小片段
Python f-string是Python字符串格式化的最新语法。从Python3.6开始可用。在Python语言中，它提供了一种更快、可读性更好、更简洁、更不易出错的字符串格式化方法。

f-strings使用 `f` 前缀与花括号 `{}` 来格式化字符串。

类型、填充或者对齐等格式指示符在冒号后指定，例如`f'{price:.3}'`，price是变量名。

##  Python字符串格式化
以下例子总结了Pyhton里可用的字符串格式化选项。

```py title="formatting_strings.py" hl_lines="8"
#!/usr/bin/python

name = 'Peter'
age = 23

print('%s is %d years old' % (name, age))
print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')
```
例子使用两个变量格式化字符串。

=== "类C经典方式"

    ```py
    print('%s is %d years old' % (name, age))
    ```

    * 这是最老的选项。使用百分号%和经典的格式化指示符号，比如%s和%d。

=== "格式化函数"

    ```py
    print('{} is {} years old'.format(name, age))
    ```

    * 从Python 3.0开始,引入格式化函数以进行一些高级的格式化操作。

=== "f-strings"

    ```py 
    print(f'{name} is {age} years old')
    ```

    * Python f-strings 从Python 3.6以后可用。使用 $f${.red} 前缀与花括号 __{ }__{.red} 来格式化字符串。

<!-- termynal-->
```bash
$ python formatting_string.py
Peter is 23 years old
Peter is 23 years old
Peter is 23 years old

```

<!-- more -->
##  Python f-string表达式
花括号`{ }`中可以使用表达式。

```py title="expressions.py"
#!/usr/bin/python

bags = 3
apples_in_bag = 12

print(f'There are total of {bags * apples_in_bag} apples')
```
f-string内的表达式会自动计算。

```bash
$ python expressions.py
There are total of 36 apples
```

##  Python f-string 字典
字典在f-strings内仍然起作用。

```py title="dicts.py"
#!/usr/bin/python

user = {'name': 'John Doe', 'occupation': 'gardener'}

print(f"{user['name']} is a {user['occupation']}")
```
f-string内的字典会自动进行取值操作。

```bash
$ python dicts.py
John Doe is a gardener
```

##  Python f-string debug
Python 3.8 通过 `=` 符号在f-string内引入了自文档表达式。

```py title="debug.py"
#!/usr/bin/python

import math

x = 0.8

print(f'{math.cos(x) = }')
print(f'{math.sin(x) = }')
```
调试模式内本例输出了sin和cos的值。

```bash
$ python debug.py
math.cos(x) = 0.6967067093471654
math.sin(x) = 0.7173560908995228
```

##  Python 多行 f-string
f-string的多行模式。

```py title="multiline.py"
#!/usr/bin/python

name = 'John Doe'
age = 32
occupation = 'gardener'

msg = (
    f'Name: {name}\n'
    f'Age: {age}\n'
    f'Occupation: {occupation}'
)

print(msg)
```
例子展示了一个多行f-string。在圆括号内放置多行f-string；每一行字符串都以f开头。

```bash
$ python multiline.py
Name: John Doe
Age: 32
Occupation: gardener
```

##  Python f-string 调用函数
f-strings内也可以调用函数。

```py title="call_function.py"
#!/usr/bin/python

def mymax(x, y):

    return x if x > y else y

a = 3
b = 4

print(f'Max of {a} and {b} is {mymax(a, b)}')
```
在f-string内调用了一个自定义函数。

```bash
$ python call_fun.py
Max of 3 and 4 is 4
```

##  Python f-string对象
Python f-string也可以接受对象；接收的对象必须在内部实现`__str__`或`__repr__`函数。

```py title="objects.py"
#!/usr/bin/python

class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __repr__(self):
        return f"{self.name} is a {self.occupation}"

u = User('John Doe', 'gardener')

print(f'{u}')
```
在f-string内会自动求值对象的字符串输出。

```bash
$ python objects.py
John Doe is a gardener
```

##  Python f-string 转义字符
以下例子展示如何在f-string内转义特定字符。

```py title="escaping.py"
#!/usr/bin/python

print(f'Python uses {{}} to evaludate variables in f-strings')
print(f'This was a \'great\' film')
```
要输出花括号，请输入两次花括号。单引号使用反斜杠转义。

```bash
$ python escaping.py
Python uses {} to evaludate variables in f-strings
This was a 'great' film
```

##  Python f-string 格式化日期时间

以下例子格式化日期时间。

```py title="format_datetime.py"
#!/usr/bin/python
import datetime

now = datetime.datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')
```
例子中打印一个格式化的日期时间。日期时间格式化指示符位于冒号:之后。

```bash
$ python format_datetime.py
2021-08-20 15:13
```

##  Python f-string 格式化浮点数
浮点数带f后缀。也可以指定精度：小数点后位数。精度由点号`.`后跟着的数字决定。

```py title="format_floats.py"
#!/usr/bin/python

val = 12.3

print(f'{val:.2f}')
print(f'{val:.5f}')
```
例子输出一串格式化后的浮点数。

```bash
$ python format_floats.py
12.30
12.30000
```

从输出可以看到小数位分别为2和5位。

##  Python f-string 格式化宽度
宽度指示符设置输出的宽度。如果输出数值小于指定宽度，前面由空格或其他字符填充。

```py title="format_width.py"
#!/usr/bin/python

for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}')
```
本例输出3列数值，每列有指定宽度。第一列使用0填充不足2位的数据。

```bash
$ python format_width.py
01   1    1
02   4    8
03   9   27
04  16   64
05  25  125
06  36  216
07  49  343
08  64  512
09  81  729
10 100 1000
```

##  Python f-string 对齐字符串
默认的对齐方式是左对齐。可以使用 `>` 符号指定右对齐。`>`符号紧跟于冒号之后。

```py title="justify.py"
#!/usr/bin/python

s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')
```
这里有4行不同长字符串。我们设置输出宽度为10，右对齐。

```bash
$ python justify.py
         a
        ab
       abc
      abcd
```

##  Python f-string 数值表示法
数值有不同的表示方法，比如10进制或16进制。

```py title="format_notations.py"
#!/usr/bin/python

a = 300

# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# scientific
print(f"{a:e}")
```
这里输出了一个数值的3种不同进制

```bash
$ python format_notations.py
12c
454
3.000000e+02
```

在本文中，我们简单的学习了f-string。