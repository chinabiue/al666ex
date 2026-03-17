---
icon: simple/framer
tags:
    - Fusion
    - shortcut
hide:
    - toc
date: 2026-03-17 21:33:25
---

# 设置Fusion快捷键 

--steps--

1. ### 显式可编辑快捷的命令

    比如**推拉**，直接点击命令边三个点   *$\vdots$*  ++"->"++  *更改键盘快捷键...*

    ![alt text](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/fusion/image.png){ width=500 }

    在弹出的窗口就可以直接按下想要的快捷键设置，最后确定。

    ![alt text](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/fusion/image-1.png){ width=500 }

2. ### 隐式可编辑快捷的命令

    不显示或隐藏的快捷方式
    __解决方案：__
    请参考官方文档

    [如何自定义在 Fusion 中不显示或隐藏的快捷方式。](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Customizing-hidden-shortcut-keys-in-Fusion-360.html)

3. ### 快捷键分享

    _把鼠标放置于中文上助记_

    | ==F==                                   | ==U==                                         | ==S==                            | ==I==                                          | ==O==                                          | ==N==                                                            | 快                                                      | 捷                                                 | 键                                             | 位                                     |
    | --------------------------------------- | --------------------------------------------- | -------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------- | -------------------------------------- |
    | ++q++                                   | ++w++                                         | ++e++                            | ++r++                                          | ++t++                                          | ++y++                                                            | ++u++                                                   | ++i++                                              | ++o++                                          | ++p++                                  |
    | __偏移__{.red title="offset,Q和O接近" } | __线圆角__{.red title="W,两个尖尖角给削圆了"} | __延伸__{.red title="Extend"}    | __中心矩形__{.red title="Rectangle"}           | __修剪__{.red title="Trim"}                    | __完成草图__{.red title="Yes,完成了"}                            | __样条曲线__{.red title="U的形状是非均匀有理B样条曲线"} | __圆柱体__{.blue title="I形似圆柱体"}              | __环形阵列__{.blue title="O本身就是环形阵列"}  | __投影__{.red title="Project"}         |
    | ++a++                                   | ++s++                                         | ++d++                            | ++f++                                          | ++g++                                          | ++h++                                                            | ++j++                                                   | ++k++                                              | ++l++                                          | ++semicolon++                          |
    | __直线__{.red title="没有理由，方便" }  | __搜索__                                      | __尺寸__{.red title="Dimension"} | __推拉__  {.red title="强记，体圆角可以用F推"} | __主视角__{.green title="Ground View原点视图"} | __过孔__{.blue title="Hole"}                                     | __装配连接__{.blue title="Joint"}                       | __中心圆弧__{.red title="K的的形状像一个中心圆弧"} | __矩形阵列__{.blue title="可以理解为二维List"} | __物理材料__{.blue title="多用就记住"} |
    | ++z++                                   | ++x++                                         | ++c++                            | ++v++                                          | ++b++                                          | ++n++                                                            | ++m++                                                   | ++comma++                                          | ++period++                                     | ++slash++                              |
    | __全部显示__{.green title="Zoom" }      | __构造线__{.red title="两条相交的线"}         | __中心圆__{.red title="Circle"}  | __移动__{.blue title="moVe"}                   | __布尔操作__{.blue title="Bool"}               | __外观__{.blue title="Nature，可以考虑换一个更好记更通用的功能"} | __实体镜像__{.blue title="Mirror"}                      | __断开__{.red title="逗号就是断点"}                | __点__{.red title=".就是一个点"}               | __移除__{.blue title="强行记住"}       |

    |       ==F== | ==U==                                     |         ==S== | ==I==                                         |          ==O== | ==N==                 |          快 | 捷                                  |
    | ----------: | ----------------------------------------- | ------------: | --------------------------------------------- | -------------: | --------------------- | ----------: | ----------------------------------- |
    | ++shift+1++ | __多视图__                                |   ++shift+t++ | 约束：__相切__{.red title="Tangle"}           | ++ctrl+space++ | __刷新__{.green}      | ++shift+s++ | __截面分析__{.blue title="Section"} |
    | ++shift+a++ | __草图镜像__{.red title="使用方便"}       |   ++shift+e++ | 约束：__重合__{.red title="Equal"}            |    ++shift+b++ | __两点矩形__{.red}    | ++shift+i++ | __相交__{.red title="Interface"}    |
    | ++shift+f++ | __新建草图__{.red title="经常使用的命令"} |   ++shift+v++ | 约束：__垂直__{.red title="Vertical"}         |    ++shift+c++ | __新建零部件__{.blue} | ++shift+w++ | __文本__{.red title="Wenben"}       |
    | ++shift+d++ | __测量__{.blue title="Dimension"}         |   ++shift+p++ | 约束：__平行__{.red title="Parallel"}         |        ++f1++: | __TopView__{.green}   |             |                                     |
    | ++shift+r++ | __干涉__ {.blue title="inteRfeRe"}        |   ++shift+m++ | 约束：__中点__{.red title="Midpoint"}         |         ++f3++ | __FrontView__{.green} |             |                                     |
    | ++shift+n++ | __显示颜色__{.blue title="和N对应"}       |   ++shift+g++ | 约束：__对称__{.red title="使用方便symmetry"} |         ++f4++ | __RightView__{.green} |             |                                     |
    |   ++grave++ | __更改参数__{.red title="定义用户参数"}   | ++backslash++ | 约束：__固定__{.red title="固定强记"}         |         ++f6++ | __全局缩放__          |             |                                     |



    红色为草图相关命令，蓝色为3D模式下命令

    分配规则为怎么方便怎么设置，尽量容易记住，左手区域分配给使用率高的命令。

    - **直线**默认快捷键是 ++l++，右手使用鼠标，左手离L太远了。所以设置为 ++a++ ，直接左手使用，效率高
    - **移动**默认快捷键是++m++，左手使用也不方便。所以设置为++v++，很方便
    - ++s++ 系统不允许更改，为命令搜索专用


    __需要特殊指出的几个设置__：

    - ++y++ 结束草图，使用方法2设置，命令为 `SketchStop`{.red}, 直接完成草图

      ```PYTHON
      HotKey.Dialog SketchStop
      SUCCESS.
      ```

    - ++shift+c++ 新建零部件，使用方法2设置。命令为 `FusionCreateNewCompnentCommand`{.red}, 在当前部件下新建零部件

        `hotkey.dialog FusionCreateNewCompnentCommand`

        ![alt text](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/fusion/image-3.png){ width=500 }

    __使用自制的自启动python addin达到特殊目的的快捷键__：

    - ++g++ 回到主视角，和点击右上角小房子 :material-home-outline:{.lg .red} 达到同样的效果，直接回到主视角，超级方便。

      ![alt text](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/fusion/HOMEVIEW11.gif){ width=500 }

    - ++z++ 缩放至适合窗口（不改变视角缩放当前可见物体至适合窗口），和按F6同样的效果++"Super"++方便。

      ![alt text](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/fusion/FIT.gif){ width=500 }

    - ++f1++ TopView / ++f2++ FrontView / ++f3++ RightView
    
    有时间更新如何用python达到++g++和++z++的快捷功能  

    另外，安装Powertoys，在画图时，把++enter++和++space++互相映射，就能方便的使用 :lucide-thumbs-up: 按空格完成大部分的确认工作，不用移动鼠标，不用右手小拇指按不准++enter++ 

--!steps--


