---
title: notepad++ 配置python运行环境(代码自动格式化/运行/高亮)
---
如果只是练习python，或者快速运行小程序片断，各种IDE就显得大材小用。配置一个notepadd++可以完成快速的任务。只需要配置3个方面的功能：

* 运行
* 代码自动格式化
* 高亮
  
### 1. 运行
从Notepad++可以直接配置快捷键运行当前python程序。
点击 `运行(R)` -`运行(R)...`
在弹出的输入框内输入以下命令，点击 保存... 分配一个名称与快捷键，即可以按快捷键运行当前程序。
```
cmd /k  cd /d "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & pause & exit
```
解释：

* cmd /k   : 告诉Notepad++接下来运行的是Windows命令行程序 
* cd /d "\$(CURRENT_DIRECTORY)"  : 切换程序运行目录为当前目录，否则程序运行目录为Notepad++安装目录
* &  ：运行多条命令连接符
* python "\$(FULL_CURRENT_PATH)"  ： 运行当前程序，前提是python要设置在系统PATH，否则python换成安装目录全路径
* pause : 运行完程序后暂停
* exit： 弹出提示"请按任意键继续..."

<!-- more -->
  ---
接下来进行一些改进项目
运行完程序后不想退出，想在命令行继续奋斗。去除最后两个命令：

`cmd /k  cd /d "$(CURRENT_DIRECTORY)"& python "$(FULL_CURRENT_PATH)"`

运行完程序后不想退出python环境，想在python里继续测试变量：

`cmd /k  cd /d "$(CURRENT_DIRECTORY)"& python -i "$(FULL_CURRENT_PATH)"`

Windows本身的命令行直接运行python太简陋，需要稍高级一点，提供代码补全，花花绿绿输出与清屏功能的ipython:

`cmd /k  cd /d "$(CURRENT_DIRECTORY)"& ipython -i "$(FULL_CURRENT_PATH)"`

试一试。写个以下内容的程序：
```py
print('运行在花花绿绿的Ipython内')
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(f'{self.name}:{self.score}')
```
按下快捷键。从Notepad直接进入了ipython并且程序定义的类已经生效。谢谢。
​![XXX](https://pic3.zhimg.com/v2-a5a0888d39d46092ef22a855892e9e46_r.jpg)
你要达到以上命令。首要条件就是python和ipython都在你系统路径里，简单说就是你能从Windows命令行直接输入python和ipython从而运行程序。

### 2. 代码格式化
代码格式化通过插件NppExec调用black格式化代码，并设置快捷键，以达到无感快速使用。
#### 2.0 安装black
在CMD界面运行以下代码安装好black格式化程序。black格式化，不问对错，直接给你改成正确格式。

`pip install black`

#### 2.1 直接绑定快捷键使用
如果不想安装插件，请直接绑定一个快捷键使用。
像上一节设置运行快捷键那样，请给如下语句绑定一个快捷键直接就可以对写好的无语法错误的程序块进行格式化。运行快捷键之前请手动保存一下。

`cmd /k  cd /d "$(CURRENT_DIRECTORY)"& black "$(FULL_CURRENT_PATH)"&exit`

#### 2.2 安装并设置插件NppExec使用
notepadd++安装插件NppExec,然后按F6。在弹出的输入窗口键入以下代码
```
SET add = $(FULL_CURRENT_PATH)
npp_save $(add)
black $(add)
npp_save $(add)
npp_close $(add)
npp_open $(add)
```
然后，依次点击菜单`插件(P)` -  `NppExec` - `Advanced Options...`按以下步骤设置：
![](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/nppexec.png)
最后依次点击菜单 `宏(M)` -  `管理快捷键...` - `插件命令`，找到刚才设置的命令，给它设置一个快捷键，比如ALT+F
#### 2.3 使用
写好python代码，按下快捷键ALT+F，就可以格式化代码了，至少比自己排版的代码强很多，好看，快速。
有个小问题，必须是语法正确的代码才会进行格式化操作。比如像下面这样你定义了一个函数，但不写内容，格式化并不会生效。如果需要生效，请在函数体内完成语法正确的语句或加个pass。如果没生效，请检查一下程序是否有语法错误。
```python
def fun():
    pass
def wrong():
```

正确的语法
```python
def fun():
    pass
def right():
    pass
```
执行格式化后会变成：#函数定义之间需要2条空白行
```python
def fun():
    pass


def right():
    pass
```

### 3. 高亮
基本语法高亮功能notepad++可以实现，自行在设置里开启高亮功能。基本够用。
但是函数参数等语义分析提示功能，notepad++暂时无法做到，即一个对象有什么方法可以使用，这些复杂的功能需要IDE的支持。
