---
title: VSCode-Rhino 联动写python程序的软件配置
---
需要以下两个操作，就能在vscode上写rhinopython：

1. VSCode(1.6.2)端安装RhinoPython这个插件。---client side

2. Rhino(7.1)端安装Codelistener这个插件。 ---server side
3. 更新： 

效果如下：


![从VSC发送程序至Rhino运行测试，成功](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/vsc0.jpg)
<!--more-->
![从VSC发送程序至Rhino运行测试，成功。其实Rhino自带编辑器也挺好用，唯一不能忍就是自定义变量名不能补全，Rhinopython里各种长变量名简直要逆天。比金箍棒还要长的变量名，你能忍就能敲出来，不能忍就用VSCode。](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/vsc1.jpg)



其实主要就是vscode这个插件的安装配置。纯翻一下，给不想费力的同学。

以下内容来自：[RhinoPython - Visual Studio Marketplace](https://marketplace.visualstudio.com/items%3FitemName%3Ddesigntoproduction.rhinopython)

图片载入有问题，更换了自己的图片。配置文件也使用了自己的文件。

### RhinoPython
RhinoPython是一个VSCode插件，可以在VSCode编辑器内写Rhino python程序，但最终程序运行是在Rhino环境内进行的。 它不仅继承了原装Rhino python编辑器的自动补全功能，反应速度还更快，同时也能享受到VSCode提供的各种好处。

它原是[DesignToProduction](http://designtoproduction.com/) 的一个开源项目，供其内部使用。

从v0.1.7开始, 它同时支持Rhino 5 和Rhino 6.（本次安装使用的是7.1）

⭐ 如果喜欢用Visual Studio, 试一试[RhinoPythonForVS](https://github.com/ccc159/RhinoPythonForVS)， 那玩意更快更智能!

### 功能
和原装Rhino python编辑器一样。只是更高效、简单和快速。

如果可以看土鳖，可以点一下 [视频链接](https://www.youtube.com/watch%3Fv%3DQbmnKFIKBYs%26feature%3Dyoutu.be) 。

### 要求
这个插件是安装在VSCode上，RhinoPython编辑器的客户端。

程序发送到Rhino运行是通过安装在Rhino上的服务端监听VSCode，那个是Rhino插件：CodeListener

### 安装过程
1. 安装 [VS code](https://code.visualstudio.com/)
2. 安装 [python for VS code](https://marketplace.visualstudio.com/items%3FitemName%3Dms-python.python)。如果不熟python for VS code，先看看这个[帖子](https://code.visualstudio.com/docs/languages/python)
3. 安装 [RhinoPython for VS code](https://marketplace.visualstudio.com/items%3FitemName%3Djingchengchen.rhinopython)
下载Rhino插件`CodeListener` ([food4rhino](https://www.food4rhino.com/app/code-listener))并安装
4. 打开Rhino, 点击`tools（工具） -> pythonscript（python脚本） -> edit（编辑）`, 在Rhino python编辑器窗口，点击 `tools -> options`, 复制Module search path里的所有路径到文本文件备用。
![目录展示](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/vsc2.jpg)
5. 在Rhino窗口，点击 `tools（工具） -> options（选项） -> Plug-ins（插件程序） -> CodeListener -> Proterties（详情）`, 点击文件名称后面那个链接打开资源管理器。向上两级，到达包含AutoComplete文件夹的目录。进入AutoComplete文件夹并复制 AutoComplete 文件夹的当前路径。
![目录地址](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/vsc3.jpg)
打开VS Code，打开`user settings（常用设置`） 快捷键`Ctrl+`, 在搜索栏键入"python.autoComplete.extraPaths"，在出现的选项中点击“在settings.json中编辑",把刚才复制的几个库路径与自动完成路径复制入设置文件。请参考以下我的配置文件内容。
![设置路径](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/vsc4.jpg)

!!! warning ""
    如果加入路径到python.autoComplete.extraPaths，自动补全并没有生效， 有一种可能是并没有正确定稿库文件的根目录。比如你的库 ExampleLib 在文件夹"...\Libs"下，你可能需要写入的路径是"...\Libs", 而不是"...\Libs\ExampleLib"。 **请注意使用双斜杠\\\\**


```json
{
    "python.defaultInterpreterPath": "C:\\Program Files\\python\\python.exe",
    "python.autoComplete.extraPaths": [
        
        "D:\\Program Files\\Rhino 7\\Plug-ins\\IronPython\\Lib",
        "C:\\Users\\kriswu\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
        "C:\\Users\\kriswu\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\scripts",
        "C:\\Users\\kriswu\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\CodeListener (8c4235b6-64bc-4508-9166-bef8aa151085)\\0.1.7.0\\AutoComplete"
    ],
    "python.analysis.extraPaths": [
        "D:\\Program Files\\Rhino 7\\Plug-ins\\IronPython\\Lib",
        "C:\\Users\\kriswu\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
        "C:\\Users\\kriswu\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\scripts",
        "C:\\Users\\kriswu\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\CodeListener (8c4235b6-64bc-4508-9166-bef8aa151085)\\0.1.7.0\\AutoComplete"
    ]

}
```
### 使用方法
- 打开Rhino, 输入命令 `CodeListener`。应该看到以下输出：`VS Code Listener Started....`
>可以把`CodeListener` 加入Rhino自启命令列表。
>其他相关的的命令还有: `StopCodeListener, CodeListenerVersion`

- 打开VS Code, 新建一个(为了使自动补全和代码分析生效，必须选择编程语言为python) 或打开一个已经有后缀.py的python文件。
- 写好程序后，按F2发送到Rhino执行，或者按F1( Ctrl+Shift+P)，在出现的>后输入`CodeSender` ，会看到程序在Rhino执行后的输出或错误信息。根据配置文件选项`RhinoPython.ResetAndRun` ，可能脚本环境会在每次发送程序前自动重置。
- 如果需要重置Rhino Python脚本环境，在VSCode按`Ctrl + R`。
### 插件设置
在**用户配置**下有以下可选的设置项:

- `RhinoPython.Enabled`: 开/关插件
- `RhinoPython.ResetAndRun`: 决定每次按下F2(或发送命令`CodeSender`)是否重置脚本环境
### 已知问题
- 调试功能暂无
- 只支持监听一个Rhino实例。如果需要切换Rhino程序，可以关掉已经连接的Rhino实例，或给它发送命令`StopCodeListener` 终止监听。
### 答谢
VSCode里RhinoCommon的智能识别工作来源于以下项目 [ironpython-stubs](https://github.com/gtalarico/ironpython-stubs) 。感谢 [Gui Talarico](https://github.com/gtalarico).