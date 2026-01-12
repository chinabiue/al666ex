---
title: Grasshooper入门与提高
icon: material/grass
# tags: Grasshopper
# categories: book
# authors:
#     - Alex
# date: 
#     created: 2022-05-15 19:12:47
#     updated: 2024-05-28 22:12:22
---
## Grasshooper入门与提高 - From TU Delft

对通过使用生成算法探索新造型的设计师来说，Grasshopper是一个紧密集成于Rhino内部的图形算法编辑器。和RhinoScript不同，Grasshopper基本不要求有编程或脚本基础，但仍然允许设计师构建从简单到令人敬畏的造型生成器。

> 代尔夫特理工大学的学生可以通过@Hok学生ICT支持: [@Hok 安装指南](https://adhok.bk.tudelft.nl/manuals/windows-manuals/)安装最新版本的Rhino，从而获得Grasshopper的使用权。

### 1. Grasshopper是什么?
![grasshopper设计参数化曲面模型示例](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/ghp/Grasshopper_FrontPage_Parametric_surface.png)

Grasshopper （GH） 是面向设计人员的编程接口。它不使用编程语言，而使用类似乐高的界面。但是，可以实现与编程代码类似的结果。使用简单的模块，设计人员可以轻松创建参数化设计。Grasshopper不仅仅是一个工具或软件，它代表了一种设计问题的思维方式，一种称为参数化或关联化的“方法”。更简单地说：Grasshopper的易用性使建筑师能够使用参数化或关联化设计的概念，而无需成为脚本/编程方面的专家。因此，建筑师可以专注于“为什么”而不是“如何”。Grasshopper由McNeel开发，内置于Rhinoceros中。
<!--more-->
### 2. Grasshopper基础知识
![在Z方向移动点5个单位(基于Rhino文件设置)的电池组](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/ghp/Grasshopper_FrontPage_Component.png)
grasshopper的核心在于它的电池。电池是程序的积木。每个电池包含2或3个组成部分：

* 1个或多个输入
* 操作：电池对输入进行处理的过程
* 1个或多个输出


![电池组件的标签列表](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/ghp/FrontPage_ModulesBar.png)

在Grasshopper面板或电池组件菜单有各种不同类型的电池组件可以选择。它们分布于10个不同的标签列表之下：Params, Maths, Set, Vector, Curve, Surface, Mesh, Intersect, Transform 和 Display。每个标签之下有多个面板和不同的电池组件，并且电池组件以命令组的不同已经分好类。在面板里有画几何图形比如直线和圆的电池组件，也有移动、缩放、分割和变形这些几何体的电池组件。所以有的电池功能是画几何体和生成数据，有的电池功能是操作已经存在的几何体或数据。*参数*是代表数据，比如1个点或1条直线，的对象。*电池组件* 是执行操作，比如移动、复制和添加，的对象。可以通过安装grasshopper插件获得更多各种功能的电池。

通过输入和输出，电池组件可以链接而形成巨大的网络。Grasshopper的画布(Canvas)是所有使用的电池组件以及它们之间内部关系的视觉呈现。它可以类比为编写脚本，但是使用的是已经定义好的代码块。这称之为可视化编程。这种方式对设计师来说更加有意义和实用。网络的运行模式是至上而下流动。

#### 2.1 入门
![大型网络的一部分](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/ghp/Front_page_A_part_of_a_large_network.png)

以下链接展示grasshopper的工作方式：

* [Grasshopper入门](http://wiki.bk.tudelft.nl/toi-pedia/Getting_Started_with_Grasshopper)
* [Grasshopper几何体介绍](http://wiki.bk.tudelft.nl/toi-pedia/Introduction_Grasshopper_Geometry)
* [Grasshopper界面](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Interface)

关于特定主题的详细解释，请参考grasshopper主题列表：

* [Grasshopper主题](http://wiki.bk.tudelft.nl/toi-pedia/Category:Grasshopper)


### 3. 学习教程

读完**入门章节**过后，要继续学习grasshopper，请完成以下教程。建议完成相关教程好，好好读读插曲的内容。

#### 3.1 初学者
* [教程 0 - 基本概念讲解](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_0_-_Basic_Principles_Explained)
* [教程 1 - 移动方块](http://wiki.bk.tudelft.nl/toi-pedia/Modules)
> //插曲: [模块]()
* [教程 2 - 曲面](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_surfaces)
* [教程 3 - 栏杆](http://wiki.bk.tudelft.nl/toi-pedia/Railing)
* [教程 4 - 门和窗](http://wiki.bk.tudelft.nl/toi-pedia/Door_and_Window)
> //插曲: [点、曲线、曲面和实体](http://wiki.bk.tudelft.nl/toi-pedia/Points,_Curves,_Surfaces_and_Solids)
* [教程 5 - 旋转塔](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_1_-_Rotating_Tower)
* [教程 6 - 曲面上的随机点](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_8_-_Random_Points_On_Surface)
> //插曲: [救命! 俺的脚本运行不了!](http://wiki.bk.tudelft.nl/toi-pedia/Help!_My_script_doesn%27t_work!)
* [教程 7 - 洞顶](http://wiki.bk.tudelft.nl/toi-pedia/Roof_with_Holes)
* [教程 8 - 创建网格](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_5_-_Creating_Grids)
> //插曲: [基本列表操作](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Basic_List_Actions)
* [教程 9 - 坡道 - 初级](http://wiki.bk.tudelft.nl/toi-pedia/Ramp_Easy)
* [教程 10 - 楼梯 - 初级](http://wiki.bk.tudelft.nl/toi-pedia/Stairs_Easy)
> //插曲: [一些好习惯](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_%22Good_Practice%22)

#### 3.2 中级
* [教程 11 - 生成图形](http://wiki.bk.tudelft.nl/toi-pedia/Making_Graphs)
> //插曲: [编辑数据树](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Data_Tree_Editing)
* [教程 12 - 曲线框架阵列 (重分布)](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Curve_Frames-Arrays)
* [教程 13 - 曲面操作](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_2_-_Surface_Manipulation)
> //插曲: [基本数据树操作](http://wiki.bk.tudelft.nl/toi-pedia/Basic_Data_Tree_Actions)
* [教程 14 - 楼梯 - 中级](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Stairs)
* [教程 15 - 坡道 - 中级](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Ramp)
* [教程 16 - 阶梯拓补图形](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_Extrude-Loft-Contour-Project)

#### 3.3 高级
* [教程 17 - 填充曲面](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_3_-_Populate_Surface)
* [教程 18 - 从曲面生成3D网格](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper_3D_Grid_from_Surface)
* [教程 19 - 砖墙](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_6_-_Brick_wall)
* [教程 20 - 吸引子](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_7_-_Attractors)
* [教程 21 - 空间框架](http://wiki.bk.tudelft.nl/toi-pedia/Tutorial_9_-_Spaceframe)
* [教程 22 - Galapagos优化](http://wiki.bk.tudelft.nl/toi-pedia/Galapagos_Optimization)

#### 3.4 专家
* [基于时间的建模实验-跳跳球](http://wiki.bk.tudelft.nl/toi-pedia/Time_Based_Modelling_-_Jumping_Ball)
* [Clusters 和 Hops](http://wiki.bk.tudelft.nl/toi-pedia/Clusters_and_Hops)

#### 3.5 GHPython
* [如何使用GhPython?](http://wiki.bk.tudelft.nl/toi-pedia/How_to_use_GhPython)
* [Python算法 (Collatz猜想)](http://wiki.bk.tudelft.nl/toi-pedia/Python_Algorithm)
* [Python楼梯](http://wiki.bk.tudelft.nl/toi-pedia/Python_Stairs)
* [分形树冠](http://wiki.bk.tudelft.nl/toi-pedia/Fractal_Canopy)
* [给IronPython 2.7安装python模块](http://wiki.bk.tudelft.nl/toi-pedia/Installing_IronPython_modules_for_Grasshopper)

#### 3.6 插件
* [安装与使用插件](http://wiki.bk.tudelft.nl/toi-pedia/Installing_and_using_Grasshopper_Plugins)
* [Ladybug安装](http://wiki.bk.tudelft.nl/toi-pedia/Ladybug_installation)
* [Ladybug光照分析](http://wiki.bk.tudelft.nl/toi-pedia/Ladybug_Light_Analysis)
* [使用Galapagos优化Ladybug](http://wiki.bk.tudelft.nl/toi-pedia/Ladybug_Optimization_using_Galapagos)
* [通过Speckle进行并行工作](http://wiki.bk.tudelft.nl/toi-pedia/AR0139-speckle)
* [Elk插件](http://wiki.bk.tudelft.nl/toi-pedia/Elk_with_grasshopper)


### 4. 书籍 / 推荐阅读
生成艺术领域发展迅速。如果很感兴趣，以下有很多有意思的博客和网站你可以访问：

**AAD_ 算法辅助设计**
使用Grasshopper讲解参数策略，一本很好Grasshopper算法书，作者Arturo Tedeschi。很多网店有售。

TU Delft图书馆 [可借阅](https://tudelft.on.worldcat.org/oclc/903993172 )

购买链接 [Bol.com](https://www.bol.com/nl/nl/p/aad-algorithms-aided-design/9200000098505502/ )

 **计算设计之数学基础** 
 计算设计的基本数学向设计专业人员介绍了有效开发3D建模和计算机图形计算方法所必需的数学概念。

下载链接 [Essential Mathematics ](https://www.rhino3d.com/download/rhino/6/essentialmathematics)

 **生成算法** 
 来自伦敦建筑协会（AA）EmTech的研究生Zubin Khabazia在线出版了一本关于他在建筑和几何相关领域的设计实验书。

下载链接 [Generative Algorithms](http://download.mcneel.com/s3/mcneel/grasshopper/1.0/docs/en/Generative%20Algorithms.pdf )

### 5. 其他链接
[Food4Rhino](http://www.food4rhino.com/) 最流行的Grasshopper和Rhino插件集合。

[McNeel Forum](http://discourse.mcneel.com/) McNeel官方论坛，可以向全世界使用相关软件的人提问与交流问题。

[Karamba3D](http://www.karamba3d.com/ ) Karamba 3D是一个Grasshopper的参数化工程插件。

[@Hok TU Delft](http://adhok.bk.tudelft.nl/ ) 代尔夫特理工大学学生的@Hok ICT支持，内含Rhino, Karamba 和 Grasshopper软件的安装指南手册。

---
原文来源于代尔夫特理工大学[设计信息学维基百科](http://wiki.bk.tudelft.nl/toi-pedia/TOI-Pedia:About) 之[Grasshopper分页面](http://wiki.bk.tudelft.nl/toi-pedia/Grasshopper)。

除非特殊说明，所有内容符合[Attribution-Noncommercial-Share Alike 3.0 Unported](http://creativecommons.org/licenses/by-nc-sa/3.0/)。

![](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/ghp/By-nc-sa_30.png)
