---
tags: Rhino-Python-Primer-101
icon: material/spider-web
# categories: book
# authors:
#     - Alex
# date: 
#     created: 2022-02-19 13:33:40
#     updated: 2024-05-28 21:33:14
---

# 8.8 网格

本章要说的不是 Nurbs 曲面(这应该是 nurbs 曲线之后的下一个逻辑步骤)，而是网格。我将借这个机会向你介绍一个完全不同类别的几何体，官方名称是多边形网格，它代表了一种完全不同的造型方法。

网格不像NURB把曲面当做矩形NURBS方块的变形来处理，而是使用局部定义，这意味着一个单独的网格曲面可以有任何它想要的拓扑结构。网格面甚至可以是不相连的浮动面的复合体，这在Rhino的NURBS曲面上是绝对不可能的。因为网格是局部定义的，也可以直接在网格格式中存储更多的信息，如颜色、纹理坐标和法线。下面这个诱人的图片显示了我们可以通过RhinoScriptSyntax访问的本地属性。这些属性大多是可选或有默认值的。唯一必要的只有顶点和面。
<div align="center"><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshtopology.svg" width="80%"/></div>

了解网格相对于其他曲面范式的优缺点很重要，这样你就可以对某项任务使用哪一种曲面做出明智的决定。网格和NURBS之间的大多数区别是不言而喻的，这是从它们的定义方式自然而形成的区别。例如，你可以从网格中删除任何数量的多边形，剩下的对象仍然有效，但是你却不能在不破坏NURBS几何形状的情况下删除结点。不过，有些需要思考的点直接从理论是看不出来的。
<!--more-->
- 在Rhino中，网格顶点的坐标以单精度的数字来存储，以节省内存。因此，网格实体没有NURBS实体精确。这在物体非常小、非常大或离世界原点非常远的情况下尤其明显。网格对象比NURBS对象更容易出现问题，因为单精度的数字比双精度的数字有更大的缺口（见第6页）。
- NURBS没有明暗层次，NURBS几何体只有等高线和边缘可以直接在视口中绘制。如果一个NURBS曲面要有阴影，那么就必须转换成网格来实现。这意味着在一个有阴影的视口中插入NURBS曲面会导致一个明显的（有时是非常明显的）时间滞后，因为软件需要时间把NURBS转换为网格来产生阴影效果。
- 在Rhino中的网格可以是非框架的，也就是说有两个以上的面共享一条边。虽然从技术上来说，NURBS的行为并非不可能，但Rhino并不允许这样做。非网格形状在拓扑学上更难处理。如果一条边只属于一个面，它就是一条外部边（裸露的），如果它属于两个面，它就被认为是内部的。

## 8.8.1 几何学与拓扑学

如前所述，只有顶点和面是网格定义的必要组成部分。顶点代表网格定义的几何部分，面代表拓扑部分。你有可能不知道我在说什么......请允许我解释一下。

根据MathWorld.com的说法，拓扑学是 " *对通过物体的变形、扭曲和拉伸而保留下来的属性的数学研究* "。换句话说，拓扑学不关心大小、形状或气味，它只关心物体规则的几何属性，例如 "它有多少个洞？"、"有多少条裸边？"以及 "我如何从巴黎到里昂而不经过任何收费站？"。拓扑学领域的知识部分是常识性的（每个人都直观地了解基本知识），部分是抽象而难以理解的。幸运的是，我们在这里只需要面对直觉的部分。

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-topology.svg" width="80%"></div>

如果看一下上面的图片，你会看到一些在拓扑上相同（除了{E}）但在几何上不同的面。你可以弯曲{A}，然后得到{B}的形状：你所要做的就是调整一些顶点的位置。然后，如果进一步弯曲它，你会得到{C}和最终的{D}，在图D，右边的边缘已经被弯曲到触及曲面另一侧的边缘。直到你把这些边合并起来，才会得到形状{E}，这个形状突然改变了它的几何本质，也就是说，它从一个有四条边的形状变成了一个只有两条边的形状（而且这两条剩余的边现在也是闭合的环）。请注意，形状{D}和{E}在几何上是相同的，这也许有点令人惊讶。

网格对象的顶点是一个三维点的坐标列表。它们可以位于空间的任何位置，并控制网格的大小和形状。另一方面，面不包含任何坐标数据，它们只指示顶点的连接方式：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-connected.svg" width="100%"></div>

上面是一个非常简单的网格，有十六个顶点和九个面。像 *_Scale* 、 *_Move* 和 *_Bend* 这样的命令只影响顶点列表，像 *_TriangulateMesh* 和 *_SwapMeshEdge* 这样的命令只影响面列表，像 *_ReduceMesh* 和 *_MeshTrim* 这样的命令同时影响两个列表。请注意，最后一个面{*I*}的角是以顺时针方式定义的，而其他所有的面都是逆时针定义的。虽然这不会造成几何上的差异，但它确实会影响到网格法线的计算，一般来说，我们应该避免创建顺时针/逆时针不一致的网格。

既然知道了网格的组成要素，那么我们写一个程序，从0开始制作一个网格曲面。生成网格曲面很简单，只要找出一组匹配的顶点/面阵列。让我们从最简单的形状开始，一个由四边形连接的顶点网格组成的网格平面。为了保持趣味性，我们将使用一个用户指定的数学函数来决定网格点的Z坐标，其形式为：

$$f(x, y, \Theta, \Delta) = z$$

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshgraph_xy.svg){width=375 align=right }

其中，用户可以使用变量 *x* 、 *y* 、 *Θ* 和 *Δ* 指定任何有效的数学函数。网格平面中的每个顶点都有一个唯一的 *x* 和 *y* 值的组合，可以通过自定义的函数来确定该顶点的 *z* 值（ *Θ* 和 *Δ* 是 *x* 和 *y* 的极坐标）。这意味着平面上的每个点{A}都有一个与之相关的坐标{B}，它与A的 *x* 和 *y* 分量相同，但不包括 *z* 分量。B点就是我们网格的顶点。<BR><BR>

在编写这个脚本时，我们会遇到4个以前没有遇到过的问题，但其中只有两个与网格几何/拓扑结构有关:
</div>

生成一组网状顶点很容易，我们以前也做过类似的循环，用一个嵌套循环来生成一个包裹着圆柱体的网格。这次的问题是，仅仅生成这些点还不够。我们还必须生成面列表，这高度依赖于顶点列表的行和列尺寸。需要大量的逻辑洞察力来实现这个目标（可能最简单的是先做一个示意图）。让我们来看看生成顶点坐标的程序，这是一个简单的程序：

```Python linenums='1'
def createmeshvertices(function, fdomain, resolution):
    xstep = (fdomain[1] - fdomain[0]) / resolution
    ystep = (fdomain[3] - fdomain[2]) / resolution
    v = []
    for x in rs.frange(fdomain[0], fdomain[1] + (0.5 * xstep), xstep):
        for y in rs.frange(fdomain[2], fdomain[3] + (0.5 * ystep), ystep):
            z = solveequation(function, x, y)
            v.append((x, y, z))
    return v
```

| 行    | 描述                                                                                                                                                                                                                                                                                                                                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 这个函数将成为最终程序的一部分。这是一个非常特殊的函数，它只是将嵌套循环的逻辑与同一程序中的其他函数(我们还没有写出这些函数，但由于我们知道它的工作流程，所以我们可以假装它已经可用)相结合。这个函数需要三个参数：<BR>1.一个字符串变量，包含函数{f(x,y,Θ,Δ)}的格式<BR>2.一个由四个双精度实数组成的数组，表示函数在x和y方向的域<BR>3.一个整数，告诉我们在每个方向要取多少个样本。 |
| 2...3 | *fDomain()* 参数有四个双精度实数，排列方式如下:<BR>(0) 最小x值&emsp;&emsp;&emsp;&emsp;(1) 最大x值<BR>(2) 最小y值&emsp;&emsp;&emsp;&emsp;(3) 最大y值<BR>我们可以很容易地访问这些值，但是由于x和y方向的步长涉及到很多数学计算，最好保存结算结果，这样我们就不用反复进行同样的计算。                                                                                                |
| 5     | 从x域的下限值开始，逐步穿过整个域，直到达到最大值。我们可以把这个循环称为行循环。                                                                                                                                                                                                                                                                                                |
| 6     | 从y域的下限值开始，逐步穿过整个域，直到达到最大值。我们可以把这个循环称为列循环。                                                                                                                                                                                                                                                                                                |
| 7     | 这里调用一个尚不存在的函数。不过，我认为这个函数名很直接，现在不需要进一步解释。                                                                                                                                                                                                                                                                                                 |
| 8     | 将新顶点添加到 *V* 列表中。请注意，顶点是以一维列表的形式存储的，这使得在一个特定的( *行，列* )坐标上访问项目变得稍微麻烦了。                                                                                                                                                                                                                                                    |

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshfacelogic.svg){width=325 align=right}

一旦我们有了顶点，我们就可以创建连接它们的面列表。由于面列表是拓扑结构，我们的顶点在空间中的位置并不重要，重要的是它们的组织方式。右边的图片是我每次遇到网格面逻辑时都会画的网格示意图。该图显示了一个有12个顶点和6个四边形面的网格，它的顶点序列逻辑与上一页函数所创建的顶点列表相同。X和Y方向的顶点数量分别为4和3（N<sub>x</sub>=4，N<sub>y</sub>=3）。

</div>

现在，每个四边形面都要以逆时针的方式连接四个顶点。你可能已经注意到，每个面四角上的顶点指数的绝对差异是相同的。就左下角的四边形而言， *{A=0; B=3; C=4; D=1}* 。在右上角四边形的情况下 *{A=7; B=10; C=11; D=8}* 。我们可以用更简单的方式来定义这些数字，这样可以把变量的数量减少到只有一个，而不是四个：
*{A=？；B=（A+N<sub>y</sub>）；C=（B+1）；D=（A+1）}* ，其中 *N<sub>y</sub>* 是y方向的顶点数量。现在我们知道了面角数字的逻辑，剩下的就是遍历所有我们需要定义的面，并计算出 *A* 角的适当数值。

```Python linenums='1'
def createmeshfaces(resolution):
    nX = resolution
    nY = resolution
    f = []
    for i in range(nX):
        for j in range(nY):
            baseindex = i * (nY + 1) + j
            f.append(
                (
                    baseindex,
                    baseindex + (nY + 1),
                    baseindex + (nY + 1) + 1,
                    baseindex + 1,
                )
            )
    return f
```

| 行    | 描述                                                                                                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| 2...3 | 缓存{N<sub>x</sub>} 和 {N<sub>y</sub>} 值，程序里我们不允许在{X}和{y}方向有不同的值，所以它们是一样的。                       |
| 4     | 声明一个空列表以保存生成的面角点。                                                                                            |
| 5...6 | 两个嵌套循环用于遍历网格并为每一行/每一列组合定义一个面。也就是说，两个值*i*和*j*被用来定义每个面的A角的值。                  |
| 7     | 使用变量名称baseindex来代替没有意义的 "A"。这个值取决于*i*和*j*的值。*i*值决定了当前列的索引，*j*值表示当前的偏移量(行索引)。 |
| 8     | 使用上述逻辑定义新的四边形面角点(以左下角为起点的逆时针4点)。                                                                 |

当你为别人写工具时，写一个能用的工具通常是不够的。除了工作之外，一个程序还应该方便使用。它不应该让你输入会导致它崩溃的值（想想看，它根本就不应该崩溃），不应该花很长时间运行，应该提供合理的默认值。在这个程序中，用户必须输入一个可能非常复杂的函数，以及四个数值来定义{x}和{y}方向的数字域。这是一个相当大的输入量，而且有可能在程序的连续运行过程中需要做微小的调整。因此，记住最后一次使用的设置是很有意义的，这样它们就会成为下一次的默认值。在使用程序时，有许多存储持久性数据的方法，每一种都有自己的优势：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-settings.svg" width="100%"></div>

我们将使用 \*.txt 文件来存储数据，因为它只涉及很少的代码，而且在Rhino重启后仍然有效。 \*.txt 文件是文本文件，它以单一的格式存储字符串。

```Python linenums='1'
def SaveFunctionData(strFunction, fDomain, Resolution):
    file = open("MeshSettings_XY.txt", "w")
    file.write(strFunction)
    file.write("\n")
    for d in fDomain:
        file.write(str(d))
        file.write("\n")
    file.write(str(Resolution))
    file.close()
```

| 行    | 描述                                                                                                                                                                                         |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2     | 这是为这个程序编写的专用函数。参数包括它要存储的数据。open关键字创建将要修改的文件流。第一个参数指定一个没有路径的文件名，会把文件保存到程序所在的目录。第二个参数表示该文件流将执行写操作。 |
| 3...8 | 将所有的设置依次写到文件中。我们将按照特定的顺序写入它们， *-strFunction，fDomain* 值0到3，以及 *Resolution* 。后面程序读取时使用同样的顺序。                                                |
| 9     | 这个调用最终确定了对文件的修改，并关闭文件以进行其他操作。                                                                                                                                   |

\*.txt文件的内容应该看起来像这样：

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-inifile.svg" width="90%"></div>

从 \*.txt 文件中读取数据要稍微复杂一些，因为不能保证文件总是存在。事实上，在第一次运行这个程序时，设置文件还不存在，我们需要确保提供合理的默认值：

```Python linenums='1'
def loadfunctiondata():
    try:
        file = open("MeshSettings_XY.txt", "r")
        items = file.readlines()
        file.close()
        function = str(items[0])
        domain = [float(items[1]), float(items[2]),
            float(items[3]), float(items[4])]
        resolution = int(items[5])
    except:
        function = "math.cos(math.sqrt(x**2+y**2))"
        domain = [-10.0, 10.0, -10.0, 10.0]
        resolution = 50
    return function, domain, resolution
```

| 行      | 描述                                                                                                                                                                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2...10  | 这个函数需要处理两种可能的情况，第一种是第一次被调用，第二种是所有后续的调用。如果是第一次调用， *"MeshSettings_XY.txt"* 文件并不存在，所以我们需要返回默认值，并在之后创建这个设置文件。在第3到第5行程序尝试访问 *"MeshSettings_XY.txt"* 文件，一旦失败， *try...except* 语句会把程序执行移到第11到第13行。 |
| 3       | 显然，我们需要完全相同的文件名。如果该文件不存在，程序将抛出一个异常。不过不用担心。 *try...except* 语句将捕捉异常，并返回设定的默认值。                                                                                                                                                                     |
| 4       | 从 \*.txt 文件中读取数据字符串。                                                                                                                                                                                                                                                                             |
| 6...9   | 从 \*.txt 文件读取设置，按设置写入文件的顺序分配回各变量。                                                                                                                                                                                                                                                   |
| 11...13 | 如果抛出了一个异常，我们要返回一组默认值。默认值定义在这里。                                                                                                                                                                                                                                                 |

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-xyphidelta.svg){width=280 align=right}

现在已经处理了四个问题中的两个（网格拓扑结构，保存和加载持久性设置），是处理大问题的时候了。在 *CreateMeshVertices()* 运行过程中，我们调用了一个叫 *SolveEquation()* 的函数，尽管它还不存在。 *SolveEquation()* 必须对特定的{x,y}坐标用自定义的函数计算出一个{z}值，这我们以前没有做过。但要找到问题的答案非常容易。

"对于 *{x=0.5}* 和 *{y=2.7}* ， *{Sin(x)+Sin(y)}* 的值是多少？"
</div>

这需要在程序中先手动写出方程，然后再运行它。程序使用自定义方程，而这些方程在程序启动后才会被知道。这意味着，方程在程序运行时是字符串变量。

*eval* 语句在程序中运行另一个程序。*eval* 语句接收一个字符串，并试图将其作为一段代码来运行，需要嵌套在当前作用域内才有意义。这意味着你可以在 *eval* 中引用局部变量。如果要计算存储在字符串中的表达式，我们正好需要 *eval* 的这个神奇特性。我们只需要确保在使用 *eval* 之前设置好 *x、y、Θ* 和 *Δ* 变量。

我们需要解决的第四个大问题与无意义的用户输入有关（在程序员中流行的某个学派声称，应该假定 **_所有_** 用户输入都是无意义的）。自定义函数有可能不符合Python语法，在这种情况下，*eval* 语句将无法解析它。有可能是因为括号不匹配，也可能是因为错别字或无法预料的其他问题。但是即使函数的语法正确，它仍然可能因为其他数学问题而崩溃。

例如，如果你试图计算 $\sqrt{-4.0}$ 的值，程序会以"无效的过程调用或参数"错误信息崩溃。 $\log\left(-4.0\right)$ 也是相同的情况。这些函数崩溃的原因是不存在请求值的答案。其他类型的数学问题也会存在，比如大数字。例如，计算 $10^{1000}$ 得到 "溢出 "错误，因为结果超出了双精度值的范围。另一个最普遍犯的错误是 "除以0 "。下表列出了在Python中发生的最常见的错误：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-errorchart.svg" width="100%"></div>

参见 [Python 的内置异常列表](http://docs.Python.org/release/3.1.3/library/exceptions.html#bltin-exceptions) 以获得完整的异常列表和对每个异常的描述。

正如你所看到的，有相当多的地方会出错。尽管不能面面俱到，但我们应该尽量防止程序崩溃。我们可以通过确保用户输入的有效性，从而避免计算上的问题；但是让程序出错，并在错误发生后根据情况让程序作出反应，要容易得多。我们以前也用过错误捕捉机制，但那时只是偷懒，现在没有别的办法，必须要使用错误捕捉机制了。

try/except语句是Python中一种很好的错误处理技术。首先，用户使用"try"尝试执行一些语句，如果语句执行无误，那么这个语句就执行完毕，try语句结束。如果发生异常，我们就直接进入 "except "部分执行它内部的语句。如果异常与命名的异常相匹配，"except "段内的代码部分就会被执行，程序可以往下执行。如果发生的错误与命名的 "异常 "不匹配，就会抛出一个 "未处理的异常 "消息。注意：一个try语句可以有很多except子句，任何给定的except子句都可以有多个它要测试的异常。

```Python linenums='1'
def solveequation(function, x, y):
    D = 10
    angledata = rs.Angle((0, 0, 0), (x, y, 0))
    A = 0.0
    if angledata:
        A = angledata[0] * math.pi / 180
    try:
        z = eval(function)
    except:
        z = 0
    return z
```

上面这段魔法代码所做的事情真的是相当令人印象深刻。它将{x; y}坐标转换为极坐标{A; D}(角度和距离)。确保角度是一个实际值，以防{x}和{y}都变成了零。它通过解方程来寻找Z坐标，如果方程无法解开，就将{z}设为零。现在，所有艰苦的工作都完成了，剩下的就是写一个为这个程序提供接口的高级函数，我认为这不需要进一步解释：

```Python linenums='1'
def meshfunction_xy():
    zfunc, domain, resolution = loadfunctiondata()
    zfunc = (rs.StringBox( zfunc, zfunc, "Mesh function")).strip()
    if not zfunc:
        return

    while True:
        prompt = (
            "Function domain x{domain[0],domain[1]} y{domain[2],domain[3]} @resolution"
        )
        result = rs.GetString(
            prompt, "Insert", ("xMin", "xMax", "yMin", "yMax", "Resolution", "Insert")
        )
        if not result:
            return
        result = result.upper()
        if result == "XMIN":
            f = rs.GetReal("X-Domain start", domain[0])
            if f is not None:
                domain[0] = f
        elif result == "XMAX":
            f = rs.GetReal("X-Domain end", domain[1])
            if f is not None:
                domain[1] = f
        elif result == "YMIN":
            f = rs.GetReal("Y-Domain start", domain[2])
            if f is not None:
                domain[2] = f
        elif result == "YMAX":
            f = rs.GetReal("Y-Domain end", domain[3])
            if f is not None:
                domain[3] = f
        elif result == "RESOLUTION":
            f = rs.GetInteger("Resolution of the graph", resolution)
            if f is not None:
                resolution = f
        elif result == "INSERT":
            break

    verts = createmeshvertices(zfunc, domain, resolution)
    faces = createmeshfaces(resolution)
    rs.AddMesh(verts, faces)
    SaveFunctionData(zfunc, domain, resolution)
```

默认的函数$\cos\left(\sqrt{x^2 + y^2}\right)$已经相当漂亮了，但这里还有一些其他函数可以玩玩：

| 数学公式                                    | Python公式                                           | 结果                                                                                                   |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| $\cos\left(\sqrt{x^2 + y^2}\right)$         | math.cos(math.sqrt(x * x + y * y))                   | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-b.svg" width="100%"> |
| $\sin(x) + \sin(y)$                         | math.sin(x) + math.sin(y)                            | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-a.svg" width="100%"> |
| $\sin(D + A)$                               | math.sin(D+A)                                        | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-l.svg" width="100%"> |
| $Atn\left(\sqrt{x^2 + y^2}\right)$          | math.atan(x*x + y*y)<br>-or-<br>math.atan(D)         | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-d.svg" width="100%"> |
| $\sqrt{\|x\|} + \sin(y)^{16}$               | math.sqrt(math.fabs(x))<BR>+math.pow(math.sin(y),16) | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-e.svg" width="100%"> |
| $\sin\left(\sqrt{\min(x^2, y^2)}\right)$    | math.sin(min(math.pow([x*x, y*y]),0.5))              | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-f.svg" width="100%"> |
| $\left[\sin(x) + \sin(y) + x + y\right]$    | int(math.sin(x) + math.sin(y) + x + y)               | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-g.svg" width="100%"> |
| $\log\left(\sin(x) + \sin(y) + 2.01\right)$ | math.log(math.sin(x)<BR>+math.sin(y)+2.01)           | <img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshxy-h.svg" width="100%"> |

## 8.8.2 形状 vs. 图像

网格对象的顶点和面列表定义了它的形式（几何和拓扑结构），但网格也可以有局部显示属性。颜色和纹理坐标是其中的两个属性，我们可以通过RhinoScriptSyntax来控制。  颜色列表（通常被称为 "假色"）是一个可选的网格属性，它为网格中的每个顶点定义了单独的颜色。我所知道的Rhino指令中，唯一能产生网格假色数据的有分析指令 *(_DraftAngleAnalysis, _ThicknessAnalysis, _CurvatureAnalysis等等)* ，但不幸的是这些命令不允许输出分析网格的结果。在我们对假色网格做一些有用的事情之前，让我们先做一些简单的事情，比如给网格对象分配随机颜色：

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-meshfalsecolours.svg" width="75%"></div>

```Python linenums='1'
import rhinoscriptsyntax as rs
from random import random

def randommeshcolors():
    mesh_id = rs.GetObject("Mesh to randomize", 32, True, True)
    if not mesh_id: return

    verts = rs.MeshVertices(mesh_id)
    faces = rs.MeshFaceVertices(mesh_id)
    colors = []
    for vert in verts:
        rgb = random()*255, random()*255, random()*255
        colors.append(rgb)
    rs.AddMesh(verts, faces, vertex_colors=colors)
    rs.DeleteObject(mesh_id)

randommeshcolors()
```

| 行     | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7...11 | False-Color数组是可选的，但如果要使用它，是有规则的。如果指定一个假色数组，必须确保它与顶点数组的元素数量相等。每个顶点都需要有一个颜色。还必须确保假色数组中的每个元素都代表一个有效颜色。在Rhino中，颜色被定义为整数，用于存储红色、绿色和蓝色通道。这些通道被定义为{0; 255}范围内的数字，它们被混合成一个更大的数字，每个通道都被分配了自己的位置。这样做的好处是，所有的颜色都只是数字，而不是更复杂的数据类型，但缺点是这些数字对人来说通常没有意义：<br><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-colortable.svg" width="60%" float="right"><br><sup>1</sup> 最低的可能值<br><sup>2</sup> 最高的可能值。 |

随机颜色很漂亮，但没什么用处。所有的Rhino分析指令都会评估某个几何局部属性(曲率、垂直度、相交距离等)，但没有一个会考虑到周围环境。假设我们要写一个程序来检查网格和(多边)曲面的接近程度。Rhino中没有任何工具可以做到这一点。所以这实际上将是一个有用的程序，另外我们将确保这个程序是完全模块化的，以便可以很容易地调整它来分析其他属性。

我们需要一个函数，它的目的是生成一个数字数组(每个顶点一个)，以定义某种属性。这些数字会被转换为渐变颜色(最低的数字为红色，最高的数字为白色)，并作为假色数据应用到一个新的网格对象上。在我们的例子中，这个属性是指从某个顶点到(多边)曲面上最接近该顶点的点的距离:

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-boxcp.svg" width="60%"></div>

<div class="result" markdown>

![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-loggraph.svg){width=260 align=right}

网格上的顶点{A}在曲面上有一个与之相关的点{$A_{cp}$}，这两者之间的距离{$D_A$}是接近度的衡量标准。这个度量是线性的，也就是说，一个两倍远的顶点得到的接近度值是一倍远的两倍。线性分布由右图中的红线表示。实际上，使用对数尺度(绿线)更有直观意义，因为它在处理大范围数值时要好得多。想象一下，我们有一个网格，其排序后的接近值集合是这样的：

{0.0; 0.0; 0.0; 0.1; 0.2; 0.5; 1.1; 1.8; 2.6; ... ; 9.4; 1000.0}

正如你所看到的，几乎所有的变化都在{0.0; 10.0}的范围内，只有一个值是超大的。现在，如果我们使用线性方法，除了最后一个会解析为白色，其他所有的接近值都会解析为红色。这不是一个有用的梯度。当用对数来计算所有的接近值时，会得到一个更自然的分布：
</div>

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-gradienttable.svg" width="100%"></div>

只有一个问题，对数函数对0和1之间的输入返回负数。事实上，零的对数是负无穷大，这对接下来的所有数学计算都造成了破坏，因为无穷大远远超出了双精度实数的数字范围。而且，由于空间中两点之间的最小距离是零，我们不能只是直接计算对数而期望程序能正常运行。解决办法很简单，在计算对数之前，所有的距离值上加1.0，这样所有的结果都是漂亮的正数。

```Python linenums='1'
def VertexValueArray(points, id):
    return [DistanceTo(point, id) for point in points]

def DistanceTo(pt, id):
    ptCP = rs.BrepClosestPoint(id,pt)
    if ptCP:
        d = rs.Distance(pt, ptCP[0])
        return math.log10(d+1)
```

| 行    | 描述                                                                                                                                                                                                                                |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1...2 | *VertexValueArray()* 函数为每个顶点创建一个数字，然后组成列表。我们给它的是网格顶点(一个三维点的数组)和用于接近分析的(多重)曲面的对象ID。这个函数没有大动作，它只是用 *DistanceTo()* 函数对点的列表进行迭代，并返回一个结果的列表。 |
| 4...8 | *DistanceTo()* 计算从点pt到点pt在曲面id上的投影间的距离。其中pt是点的三维坐标，id是一个(多重)曲面对象的标识符。它还进行了对数转换，所以返回值不是实际距离。                                                                         |

下面是包含所有前端和色彩魔法的主函数：

```Python linenums='1'
import rhinoscriptsyntax as rs
import math

def ProximityAnalysis():
    mesh_id = rs.GetObject("Mesh for proximity analysis", 32, True, True)
    if not mesh_id: return

    brep_id = rs.GetObject("Surface for proximity test", 8+16, False, True)
    if not brep_id: return

    vertices = rs.MeshVertices(mesh_id)
    faces = rs.MeshFaceVertices(mesh_id)
    listD = VertexValueArray(vertices, brep_id)

    minD = min(listD)
    maxD = max(listD)
    colors = []
    for i in range(len(vertices)):
        proxFactor = (listD[i]-minD)/(maxD-minD)
        colors.append((255, 255*proxFactor, 255*proxFactor))
    rs.AddMesh(vertices, faces, vertex_colors=colors)
    rs.DeleteObject(mesh_id)
```

| 行      | 描述                                                                                 |
| ------- | ------------------------------------------------------------------------------------ |
| 1...3   | 原文import sys，实际并没有必要。因为后面给出的逻辑条件置换最大最小值根本不可能发生。 |
| 15...16 | 找到列表中最大和最小的值。                                                           |
| 17      | 创建颜色列表。                                                                       |
| 19      | 计算当前值在{红~白}梯度上的位置。                                                    |
| 20      | 根据 *proxFactor* 得出一个颜色。                                                     |