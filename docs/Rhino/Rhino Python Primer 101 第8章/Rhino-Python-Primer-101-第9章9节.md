---
tags: Rhino-Python-Primer-101
icon: material/ladybug
# categories: book
# authors:
#     - Alex
# date: 
#     created: 2022-01-20 21:30:07
#     updated: 2024-07-03 20:11:43
# icon: material/book
status: new
---
# :material-book:{.red} Rev3程序勘误
Rhino Python Primer 101这本书是官方出版的学习python编程在Rhino中应用的手册。

没有中文版，这不是问题，咱学英文；但是有一点比较坑的是，里面的程序没有经过仔细的校对，思路都是对的，但是只要一上手运行就会发现各种错误。
因为程序是很严谨的，就像书里自己也说了python大小写敏感，只要错了一个字母，就是运行不起来。这可恐怖了，加了两层buff，一是英文首先就不好理解了，再加上程序错误，极容易产生的情绪是学习一下就发现进行不下去了，很沮丧。

!!! info "🤳请看作者立的FLAG"
    
    All the example code in this primer can be copy-pasted directly into the _EditPythonScript dialog.<BR>
    本入门所有代码可直接复制粘贴至 *_EditPythonScript* 对话框。


但是我不怕困难，一学英语，二学编程。两手都要抓，两手都要硬。对学习过的程序，都需要运行一遍，以在电脑上运行通过为标准，对书中的程序进行一次大扫除。
首先运行环境是：
```python
import sys
print(sys.version)
```
!!! note ""
    
    `2.7.9 (IronPython 2.7.9 (2.7.9.0) on .NET 4.0.30319.42000 (64-bit))`<br>
    **Rhino 7.12**


以下是扫除过程。
<!--MORE-->
## 第1章 这是啥玩意儿
兴冲冲的学习起来，本书的第一个示例程序就给你一个下马威。你要是把下面这原书代码直接复制并绑定到一个按钮上(默认你已经会这样做了)。保证你运行不了：
```java
_SelNone
_Polygon _NumSides=6 w0,0,0 w10,0,0
_SelLast
-_Properties _Object _Name RailPolygon _Enter _Enter
_SelNone
_Polygon _NumSides=6 w10,0,0 w12,0,0
_SelLast
_Rotate3D w0,0,0 w10,0,0 90
-_Properties _Object _Name ProfilePolygon _Enter _Enter
_SelNone
-_Sweep1 _SelName RailPolygon _SelName ProfilePolygon _Enter _Enter _Closed=Yes Enter
```
直接运行会弹出个窗口，然后要你选择，无论你怎么选最后都生成不了书上这玩意。对新手极不友好，很多人就放弃了。书的作者可能，就完全没运行过自己写的这段宏，还不如不贴呢，打击了多少人的积极性。

<figure markdown>
  ![Hexagonaltorus](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/hexagonaltorus.svg){ width="400" }
  <figcaption>Polygon</figcaption>
</figure>

问题在哪呢？我来给出答案：问题在最后一行命令有巨大问题。

`-_Sweep1 _SelName RailPolygon _SelName ProfilePolygon _Enter _Enter _Closed=Yes Enter`

主要2个问题：

1. 作者自己也说了，'-'这个符号是让命令运行不弹出窗口与用户交互，可是他自己马上就食言了，甩出两个`_SelName`让窗口弹出，新手措手不及，不知道发生了什么。无论咋点也不成功。
   
2. `_Closed=Yes Enter`这在中文界面下行不通，Closed=Yes设置参数，并不是命令，前面并不需要加下划线`_`；需要加下划线`_`的Enter又不加。吐血。

3. 在程序界面语言为中文的情况下，只能使用命令简写让程序完全无误的运行，意思就是`_C`
   
4. 请在Top/Perspective/Front窗口下运行程序，在Right窗口运行程序不会起作用。

以下是改正过的程序，一键运行稳如狗。
(这个做为试验，我分支了MCNEEL的github库，改正了这个问题，并且推送回MCNEEL,他们接受了这个pull request并合并到他们的仓库了。现在Rhino网上的教程部分是没有问题的了，和改正过的一样。就是不知道PDF他们有没有重新生成。)
第2页
```JAVA
_SelNone
_Polygon _NumSides=6 w0,0,0 w10,0,0
_SelLast
-_Properties _Object _Name RailPolygon _Enter _Enter
_SelNone
_Polygon _NumSides=6 w10,0,0 w12,0,0
_SelLast
_Rotate3D w0,0,0 w10,0,0 90
-_Properties _Object _Name ProfilePolygon _Enter _Enter
_SelNone
-_Sweep1 -_SelName RailPolygon -_SelName ProfilePolygon _Enter _Enter _C _Enter
```
## 第2章 Python基础
用python的方式，重复了第1章的错误，不做分析了，直接上改进过后能运行的代码。
第10页
```python
import rhinoscriptsyntax as rs

dblMajorRadius = rs.GetReal("Major radius", 10.0, 1.0, 1000.0)
dblMinorRadius = rs.GetReal("Minor radius", 2.0, 0.1, 100.0)
intSides = rs.GetInteger("Number of sides", 6, 3, 20)

strPoint1 = " w" + str(dblMajorRadius) + ",0,0"
strPoint2 = " w" + str(dblMajorRadius + dblMinorRadius) + ",0,0"

rs.Command ("_SelNone")
rs.Command ("_Polygon _NumSides=" + str(intSides) + " w0,0,0" + strPoint1)
rs.Command ("_SelLast")
rs.Command ("-_Properties _Object _Name Rail _Enter _Enter")
rs.Command ("_SelNone")
rs.Command ("_Polygon _NumSides=" + str(intSides) + strPoint1 + strPoint2)
rs.Command ("_SelLast")
rs.Command ("_Rotate3D w0,0,0 w1,0,0 90")
rs.Command ("-_Properties _Object _Name Profile _Enter _Enter")
rs.Command ("_SelNone")
rs.Command ("-_Sweep1 -_SelName Rail -_SelName Profile _Enter _Enter _C _Enter")
rs.Command ("-_SelName Rail")
rs.Command ("-_SelName Profile")
rs.Command ("_Delete")
```

## 第3章 脚本结构
无

## 第4章 操作符与函数
无

## 第5章 条件执行
以下程序无错误，但是有副作用。运行了无法停止，哈哈。请把程序关了重新打开。

第27页
```python
import rhinoscriptsyntax as rs
import datetime as dt

def viewportclock():
    now = dt.datetime.now()
    textobject_id = rs.AddText(str(now), (0,0,0), 20)
    if textobject_id is None: return
    rs.ZoomExtents(None, True)
    while True:
        rs.Sleep(1000)
        now = dt.datetime.now()
        rs.TextObjectText(textobject_id, str(now))

if __name__=="__main__":
    viewportclock()
```

## 第6章 元组、列表和字典
又一神作，一时半会反应不过来会陷入无限循环。我被Rhino问到我第242最喜欢的事情是什么的时候，关闭了程序。

这玩意有退出条件，但是很隐蔽`if answer is None: break`,如何在Rhino输入一个None值呢？

1. 直接回车
   
2. 按空格
   
3. 按退格
   
都不对，请按左上角`ESC`键，我大意了，没有闪。

第34页
```python
import rhinoscriptsyntax as rs

def myfavoritethings():
    things = []

    while True:
        count = len(things)
        prompt = "What is your {0}th most favorite thing?".format(count+1)
        if len(things)==0:
            prompt = "What is your most favorite thing?"
        elif count==1:
            prompt = "What is your second most favorite thing?"
        elif count==2:
            prompt = "What is your third most favourite thing?"

        answer = rs.GetString(prompt)
        if answer is None: break
        things.append(answer)
    if len(things)==0: return

    print "Your", len(things)+1, "favorite things are:"
    for i,thing in enumerate(things): print i+1, ".", thing
```

第35页，左边的程序并不会产生右图的结果。下面这个程序能生成比较像右边图。

<figure markdown>
  ![sin_cos](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/basic/sin_cos.png){ width="400" }
  <figcaption>sin_cos</figcaption>
</figure>

```python
import rhinoscriptsyntax as rs
import math

r = -1800
step = 5
for t in rs.frange(0,2*abs(r),step):
    x = r * math.cos(t/360*2*math.pi)
    y = r * math.sin(t/360*2*math.pi)
    z = r
    rs.AddPoint(x,y,z)
    r += step
```

#### 嵌套列表
这一节的程序，平滑曲线。错误一般般，主要就是生成曲线节点数与阶数有一个关系：

$$K_N = P_N + (D-1)$$

smoothcurve()这个函数漏掉了起点和终点，导致不符合公式以致于无法画出最后平滑的曲线。

```python
import rhinoscriptsyntax as rs

def smoothingvector(point, prev_point, next_point, s):
    pm = (prev_point+next_point)/2.0
    va = rs.VectorCreate(pm, point)
    vm = rs.VectorScale(va, s)
    return vm

def smoothcurve(curve_id, s):
    curve_points = rs.CurvePoints(curve_id)
    new_curve_points = []
    new_curve_points.append(curve_points[0])    # miss 1st point
    for i in range(1, len(curve_points)-1):
        vm = smoothingvector(curve_points[i], curve_points[i-1], curve_points[i+1], s)
        new_curve_points.append( rs.PointAdd(curve_points[i], vm) )
    new_curve_points.append(curve_points[-1])    # miss last point

    knots = rs.CurveKnots(curve_id)
    degree = rs.CurveDegree(curve_id)
    weights = rs.CurveWeights(curve_id,0)
    newcurve_id = rs.AddNurbsCurve(new_curve_points, knots, degree, weights)
    if newcurve_id: rs.DeleteObject(curve_id)
    return newcurve_id


def iterativeshortencurve():
    curve_id = rs.GetObject("Open curve to smooth", 4, True)
    if curve_id is None or rs.IsCurveClosed(curve_id): return

    min = rs.Distance(rs.CurveStartPoint(curve_id), rs.CurveEndPoint(curve_id))
    max = rs.CurveLength(curve_id)
    goal = rs.GetReal("Goal length", 0.5*(min+max) , min, max)
    if goal is None: return

    while rs.CurveLength(curve_id)>goal:
        rs.EnableRedraw(False)
        curve_id = smoothcurve(curve_id, 0.1)
        rs.EnableRedraw(True)
        if curve_id is None: break

iterativeshortencurve()
```
## 第7章 类
无

## 第8章 几何体
核心篇章，重灾区，越是重要的地方出错越多。因为程序复杂性上升了一个程度。
### 8.4 线段与多重直线
这一节程序写得很好，没有什么性质方面的错误。但是有作者一再指出的基本错误：Python大小写敏感错误。

前面两个函数采用了驼峰命名法，后面又全部用小写单词命名，粗心。要想程序运行，把前面两个函数名全改成小写。这里就不贴出来了。

从函数与变量命名的方式，可以明显的感觉到，这本书的作者是几个人，前面挺正式的介绍变量命名方式，后面全部弃用，开始放飞自我式命名；函数的命名，有驼峰法，有全小写的，应该出自几个不同的高手。

#### 8.7.1 控制点曲线
给曲线倒角的程序，运行不了。因为计算两点之间中间点使用的匿名函数 *between* ，把Vector3d对象和Point3d对象直接相加，程序不认。
w1、w2生成的是Vector3D对象也不是Point3d点对象。把所有的对象统一转换为Point3d对象，就能使程序正常运行。如下：


```python
import rhinoscriptsyntax as rs


def blendcorners():
    polyline_id = rs.GetObject("Polyline to blend", 4, True, True)
    if not polyline_id:
        return
    vertices = rs.PolylineVertices(polyline_id)
    if not vertices:
        return
    radius = rs.GetReal("Blend radius", 1.0, 0.0)
    if radius is None:
        return
    
    between = lambda a, b: rs.CreatePoint((a + b) / 2.0)
    newverts = []
    for i in range(len(vertices) - 1):
        a = vertices[i]
        b = vertices[i + 1]
        segment_length = rs.Distance(a, b)
        vec_segment = rs.PointSubtract(b, a)
        vec_segment = rs.VectorUnitize(vec_segment)

        if radius < (0.5 * segment_length):
            vec_segment = rs.VectorScale(vec_segment, radius)
        else:
            vec_segment = rs.VectorScale(vec_segment, 0.5 * segment_length)

        w1 = rs.CreatePoint(rs.VectorAdd(a, vec_segment))
        w2 = rs.CreatePoint(rs.VectorSubtract(b, vec_segment))
        newverts.append(a)
        newverts.append(between(a, w1))
        newverts.append(w1)
        newverts.append(between(w1, w2))
        newverts.append(w2)
        newverts.append(between(w2, b))
    newverts.append(vertices[len(vertices) - 1])
    rs.AddCurve(newverts, 5)
    rs.DeleteObject(polyline_id)


blendcorners()
```

#### 8.7.3 几何曲线特性

书里这个程序，存在两个问题：

1. 用于保存用户生成物体的列表 *preview* 是一个嵌套列表，如果不更改删除方式，除了默认参数可以运行，用户输入任何自定参数时，会走到删除 *preview* 内列表这一步报错，因为 *rs.DeleteObjects()* 分析 *preview* 列表内的元素并不是有效的Rhino物体。
2. 在接收用户参数这一步，并不能处理用户随意输入的无效信息。

更改后的程序如下：

```Python
def createcurvaturegraph():
    curve_ids = rs.GetObjects("Curves for curvature graph", 4, False, True, True)
    if not curve_ids:
        return

    samples = 10
    scale = 100.0

    preview = []
    while True:
        rs.EnableRedraw(False)
        for p in preview:
            for item_list in p:
                rs.DeleteObjects(item_list)
        preview = []
        for id in curve_ids:
            cg = addcurvaturegraph(id, samples, scale)
            preview.append(cg)
        rs.EnableRedraw(True)

        result = rs.GetString(
            "Curvature settings", "Accept", ("Samples", "Scale", "Accept")
        )
        if not result:
            for p in preview:
                for item_list in p:
                    rs.DeleteObjects(item_list)
            break
        result = result.upper()
        if result == "ACCEPT":
            break
        elif result == "SAMPLES":
            numsamples = rs.GetInteger(
                "Number of samples per knot-span", samples, 3, 100
            )
            if numsamples:
                samples = numsamples
        elif result == "SCALE":
            sc = rs.GetReal("Scale of the graph", scale, 0.01, 1000.0)
            if sc:
                scale = sc
        else:
            rs.Prompt('Please input/select a correct parameter:')
            rs.Sleep(750)
            continue
```

