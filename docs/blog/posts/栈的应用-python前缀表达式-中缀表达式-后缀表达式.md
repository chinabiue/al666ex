---
title: 栈的应用(python)：前缀表达式 <- 中缀表达式 -> 后缀表达式
---
## 1. 栈的实现
可使用列表，按自己的方式实现栈的数据结构。类的方法可以实现栈的基本操作。

既然是用列表实现的，可以创造一些方便的方法比如__repr__以方便查看栈的内容。

```python  hl_lines="23-27"
class Stack():
    def __init__(self):            # 使用空列表初始化栈
        self.items = []

    def isEmpty(self):             # 查看栈是否为空
        return self.items == []
    
    def push(self, item):          # 入栈基操
        self.items.append(item)
    
    def pop(self):                 # 出栈基操
        return self.items.pop()

    def peek(self):                # 查看栈顶元素
        return self.items[len(self.items) - 1]

    def __len__(self):             # 使用列表特性，返回栈的长度
        return len(self.items)

    def __getitem__(self, n):      # 使用列表特性，获取栈元素
        return self.items[n]
    
    def __repr__(self):            # 使用列表特性，打印栈内容
        if self.items:
            return str(self.items)
        else:
            return 'None'
```

## 2. 前缀表达式 <- 中缀表达式 -> 后缀表达式
* 中缀表达式： 人类通常使用的表达式，易于人的理解
* 前缀表达式： 计算机通常使用的表达式，易于机器理解与执行
* 后缀表达式： 同上。

要理解这三种表达式，可以通过以下实例理解：

| 中缀表达式        | 前缀表达式    | 后缀表达式    |
| ----------------- | ------------- | ------------- |
| A + B             | + A B         | A B +         |
| A + B - C         | - + A B C     | A B + C -     |
| A + B * C         | + A * B C     | A B C * +     |
| (A + B) * C       | * + A B C     | A B + C *     |
| A + B * C - D     | - + A * B C D | A B C * + D - |
| (A + B) * (C - D) | * + A B - C D | A B + C D - * |
| A * B + C / D     | + * A B / C D | A B * C D / + |
| A + B - C + D     | + - + A B C D | A B + C - D + |

<!-- more -->
### 2.1 中缀表达式 -> 后缀表达式
假设中缀表达式是一个以空格分隔的标记串。其中，运算符标记有* 、/ 、+ 和- ，括号标记有 ( 和 ) ，操作数标记有A 、B 、C 等。下面的步骤会生成一个后缀标记串。
!!! note ""

    (1) 创建用于保存运算符的空栈opStack ，以及一个用于保存结果的空列表。

    (2) 使用字符串方法split 将输入的中序表达式转换成一个列表。

    (3) 从左往右扫描这个标记列表。
    
      * 3.1 如果标记是操作数，将其添加到结果列表的末尾。<BR>
      * 3.2 如果标记是左括号，将其压入opStack 栈中。<BR>
      * 3.3 如果标记是右括号，反复从opStack 栈中移除元素，直到移除对应的左括号。将从栈中取出的每一个运算符都添加到结果列表的末尾。<BR>
      * 3.4 如果标记是运算符，将其压入opStack 栈中。**但是，在这之前，需要先从栈中取出优先级更高或相同的运算符，并将它们添加到结果列表的末尾。**

    (4) 当处理完输入表达式以后，检查opStack 。将其中所有残留的运算符全部添加到结果列表的末尾。


```python
import string

def infix2Postfix(infexExp):
    prec = { '*': 3, '/': 3,
             '+': 2, '-': 2,
             '(': 1, ')': 1
           }                # 设置符号优先级
    
    opStack = Stack()       # (1)
    result = []             # (1)
    
    tokenList = infexExp.split() # (2)
    
    for token in tokenList:      # (3)
        # print('opStack: ', opStack)
        # print('result : ', result, '\n') # 调试使用，可以查看每一步栈内容与列表内容
        
        if token in string.ascii_uppercase: # 对应3.1
            result.append(token)
        elif token == '(':                  # 对应3.2
            opStack.push(token)
        elif token == ')':                  # 对应3.3
            topOp = opStack.pop()
            while topOp != '(':
                result.append(topOp)
                topOp = opStack.pop()
        else:                               # 对应3.4
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                result.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():            # (4)
        result.append(opStack.pop())
    
    return ' '.join(result)
```

### 2.2 前缀表达式 <- 中缀表达式
假设中序表达式是一个以空格分隔的标记串。其中，运算符标记有* 、/ 、+ 和- ，括号标记有( 和) ，操作数标记有A 、B 、C 等。下面的步骤会生成一个前缀标记串。

!!! note ""

    (1) 创建用于保存运算符的空栈opStack ，以及一个用于保存结果的空列表。

    (2) 使用字符串方法split 将输入的中序表达式转换成一个列表，**反转列表**。

    (3) 从左往右扫描这个标记列表。

    * 3.1 如果标记是操作数，将其添加到结果列表的末尾。<BR>
    * 3.2 如果标记是右括号，将其压入opStack 栈中。<BR>
    * 3.3 如果标记是左括号，反复从opStack 栈中移除元素，直到移除对应的右括号。将从栈中取出的每一个运算符都添加到结果列表的末尾。<BR>
    * 3.4 如果标记是运算符，将其压入opStack 栈中。**但是，在这之前，需要先从栈中取出优先级更高的运算符，并将它们添加到结果列表的末尾。**

    (4) 当处理完输入表达式以后，检查opStack 。将其中所有残留的运算符全部添加到结果列表的末尾。

    (5) **反转结果列表**


```python
import string

def infix2Prefix(infexExp):
    prec = { '*': 3, '/': 3,
             '+': 2, '-': 2,
             '(': 1, ')': 1
           }                # 设置符号优先级
    
    opStack = Stack()       # (1)
    result = []             # (1)
    
    tokenList = infexExp.split()[::-1] # (2)
    
    for token in tokenList:      # (3)
        # print('opStack: ', opStack)
        # print('result : ', result, '\n')
        
        if token in string.ascii_uppercase: # 对应3.1
            result.append(token)
        elif token == ')':                  # 对应3.2
            opStack.push(token)
        elif token == '(':                  # 对应3.3
            topOp = opStack.pop()
            while topOp != ')':
                result.append(topOp)
                topOp = opStack.pop()
        else:                               # 对应3.4
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] > prec[token]):
                result.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():            # (4)
        result.append(opStack.pop())

    result.reverse()                        # (5)

    return ' '.join(result)
```
!!! info ""

    1. 参考文档：Python数据结构与算法分析（第2版），作者：[美] 布拉德利 • 米勒 戴维 • 拉努姆
    2. 前缀表达式 <- 中缀表达式 -> 后缀表达式 有的地方也叫 前序表达式 <- 中序表达式 -> 后序表达式
