---
tags: Rhino-Python-Primer-101
icon: material/circle-multiple-outline
# categories: book
# authors:
#     - Alex
# date: 
#     created: 2022-01-15 11:16:23
#     updated: 2024-05-28 21:20:24
---
# 8.6 圆、椭圆和弧线

在Rhino里，用户不会直接面对参数化物体，但是openNURBS™内核里有一部分数学原型是参数化存储的。例如圆柱、球体、圆、旋转体和sum-surface。看下图突出显示显式(参数化)和隐式圆的区别：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-circleschart.svg" width="100%"></div>

当通过程序在Rhino中添加圆，我们可以指定平面+半径，也可以指定3个点(程序内部会转换为平面+半径)。你可能记得圆和正弦波与余弦波有着紧密的联系，就是那些可爱的波浪线。接下来我们要写一个程序，在指定半径球体上封装指定半径的圆。在我给出答案之前，花1分钟好好想想这个问题。

最明显的解决方法是：在球体的水平带上开始堆圆，暂时忽略竖直带产生的干扰。如果你也想到了这个方法，并开始自我感觉良好的话，那么我告诉你别读接下来两句话。这个方法已经被人用了又用，但是不知道什么原因，Dave Rusin被认为是这个方法的发明人。即便Rusin的算法算不上什么黑科技，但是在我最后给出代码之前，讨论一下这里面的数学问题还是有价值的，以免造成混乱，至少是减少混乱。

Rusin的算法是这样工作的：

- 算出球体上，从北极点到南极点可以等距堆多少个圆。
- 算出环绕圆可以堆出多少条这样的圆形带。
- 完成
<!--more-->
等一下，暂停。首先想一下球体是如何形成的。只有领悟了球体的特性，我们才能给它装上圆。在Rhino中，球体是旋转形成的，有两个极点和一条接缝：

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-uv-map.svg" width="100%"></div>

北极点(左图黑点)和南极点(左图白点)都位于球体主轴，接缝(粗边缘)连接这两点。实质上，球体是由一个长方形平面两边弯曲，左边和右边重合形成接缝，上边和下边压缩为一点(极点)。我们应该很熟悉这个坐标系，因为地球用的就是这一套。地球以纬度和经度角度划分，球体以纬度和经度弧度划分。球体纬度弧度的数字域从南极点-½π开始，在赤道达到0.0，在北极点终止于½π。经度弧度域开始和结束都位于接缝上，环绕球体一周从0.0至2π。现在你应该知道它为什么叫‘接缝’了：它是弧度域从最小值突然跳变为最大值的地方。

我们不能像右图上那样在长方形上封装小正方形，因为在极点附近它们会严重变形，实际上你也看得到在极点附近它们真的变形了。我们希望封装的圆保持完美，这意味着要和球体的收敛性做斗争。

<div class="result" markdown>
![](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-sphereuv.svg){ align=left width=180 }

假设我们要封装的圆半径远远小于球体半径，至少有两个圆我们可以毫不犹豫的加上：南北极点各放一个。有个额外的好处是，现在这两个圆完美覆盖了极点，只剩下那条烦人的接缝没有处理了。然后接下来要干的活是，确定需要多少个圆能直接覆盖掉这条接缝。接缝的长度是球体周长的一半(左图黄色箭头)。

放松时间到，我们已经收集了要封装填充这个球体需要的所有信息。算法的最后一步是，从每一个在接缝上的圆开始，围绕球体堆积圆。我们需要计算球体上圆位置纬度的周长，用这个周长除以小圆直径，找到等于或小于结果的最大整数。原理的数学公式是：

$$N_{count} = \left[\frac{2 \cdot R_{sphere} \cdot \cos{\phi}}{2 \cdot R_{circle}} \right]$$  
</div>

想要给人留下深刻印象请背下这个公式...

<hr>

```python linenums='1'
import rhinoscriptsyntax as rs
import math
def DistributeCirclesOnSphere():
    sphere_radius = rs.GetReal("Radius of sphere", 10.0, 0.01)
    if not sphere_radius: return
    circle_radius = rs.GetReal("Radius of circles", 0.05*sphere_radius, 0.001, 0.5*sphere_radius)
    if not circle_radius: return
    vertical_count = int( (math.pi*sphere_radius)/(2*circle_radius) )

    rs.EnableRedraw(False)
    phi = -0.5*math.pi
    phi_step = math.pi/vertical_count
    while phi<0.5*math.pi:
        horizontal_count = int( (2*math.pi*math.cos(phi)*sphere_radius)/(2*circle_radius) )
        if horizontal_count==0: horizontal_count=1
        theta = 0
        theta_step = 2*math.pi/horizontal_count
        while theta<2*math.pi-1e-8:
            circle_center = (sphere_radius*math.cos(theta)*math.cos(phi),
                sphere_radius*math.sin(theta)*math.cos(phi), sphere_radius*math.sin(phi))
            circle_normal = rs.PointSubtract(circle_center, (0,0,0))
            circle_plane = rs.PlaneFromNormal(circle_center, circle_normal)
            rs.AddCircle(circle_plane, circle_radius)
            theta += theta_step
        phi += phi_step
    rs.EnableRedraw(True)
DistributeCirclesOnSphere()
```

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-spherepack.svg" width="85%"></div>


| 行              | 描述                                                                                                                                                                                                                                                                                                                                   |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1...6           | 收集自定变量并确保数值有效。小于0.01单位的球体和圆半径大于球体半径1/2都是无效的。                                                                                                                                                                                                                                                      |
| 8               | 计算两极点间圆的数量。 *int()* 函数接收浮点数，返回浮点数的整数部分。因此它总是向下舍入。                                                                                                                                                                                                                                              |
| 11...12 16...17 | phi和theta (Φ 和 Θ)通常用于表示球面空间的角度，通过符号形状不难看出来。我们也可以分别称它们为纬度和经度。                                                                                                                                                                                                                              |
| 13              | phi循环从-½π 到 ½π，需要运行 *VerticalCount* 次。                                                                                                                                                                                                                                                                                      |
| 14              | 此行计算在球体当前纬度上能放置圆的数量。计算方法和前面一致，除了需要计算当前纬度环绕球体一周的长度：2π·R·Cos(Φ)                                                                                                                                                                                                                        |
| 15              | 如果计算结果发现在某个纬度结果为0(就是在-½π和½π处)，我们会遇到麻烦，因为在第17行使用了这个结果作为分母。谁都知道分母不能为0。但是在这两点我们知道至少可以放下一个圆。                                                                                                                                                                  |
| 18              | 这个循环本质上和第13行是一样的，不同点在于它使用的步进(theta_step)和数字范围({0.0 <= theta < 2π}。这里需要注意的点是theta的范围从0开始，但是不包括2π。如果 *theta* 的取值达到2π的话，在接缝处会产生一个重复的圆。阻止循环达到特定值的最好方法是把特定值减去一个值，在本程序我通过直接减掉一个超小的值(1e-8 = 0.00000001)达到这个目的。 |
| 19...21         | *circle_center* 保存要添加圆的中心点。<br>*circle_normal* 保存圆所在的平面的法线<br>*circle_plane* 保存生成的平面定义。                                                                                                                                                                                                                |
| 19              | 这一行需要很大的计算量，在这里不提供证明过程和工作过程。这是把球面坐标Φ 和 Θ转换为笛卡尔坐标x,y,z的标准方法。详细信息请参考 [MathWorld.com](http://mathworld.wolfram.com/)                                                                                                                                                             |
| 20              | 一旦找到球体上对应当前 Φ 和 Θ 值的点，确定这一点的法线就是小小菜一碟了。球面上任何一点的法线就是当前点到球体中心点向量的反向量。这就是第20行的功能，我们把新找到的{x,y,z}点减去球体原点(在本例中总是(0,0,0))。                                                                                                                         |
| 21...22         | 我们可以从平面上一个单点和一个法线向量定义一个平面，然后用一个平面和半径值定义一个圆。牛逼。                                                                                                                                                                                                                                           |


## 8.6.1 椭圆

椭圆本质上和圆差不多，只是椭圆需要两个半径。因为椭圆只有两个镜像对称平面，而圆具有旋转对称性（即无限数量的镜像对称平面），在椭圆的情况下，基平面的方向确实很重要。仅由原点和法向量指定的平面可以自由地围绕该向量旋转，而不会破坏任何初始约束。

下面的程序非常清楚地演示了基平面和椭圆的方向对应性。参考标准曲率分析图，如左图所示：

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-curvaturespline.svg" width="80%"></div>

通过图片可以对样条曲线中不同曲率的范围有一个清晰的印象，但它不能很好地传达曲率的螺旋扭曲。近似线性的样条曲线部分往往具有扭曲的曲率，因为它们是从一个明确定义的折弯到另一个折弯的过渡。左图中的箭头表示这些扭曲区域，但仅从曲率图中很难推断出这一点。下面的程序将使用曲率信息通过一组椭圆放样曲面，这些椭圆已定向到局部样条几何的曲率平面。椭圆在曲线的折弯平面中具有较小的半径，而在垂直于折弯平面的半径较大。由于我们不会使用曲率的强度，而只会使用其方向，因此小细节将变得非常明显。


```python linenums='1'
def FlatWorm():
    curve_object = rs.GetObject("Pick a backbone curve", 4, True, False)
    if not curve_object: return

    samples = rs.GetInteger("Number of cross sections", 100, 5)
    if not samples: return

    bend_radius = rs.GetReal("Bend plane radius", 0.5, 0.001)
    if not bend_radius: return

    perp_radius = rs.GetReal("Ribbon plane radius", 2.0, 0.001)
    if not perp_radius: return

    crvdomain = rs.CurveDomain(curve_object)

    crosssections = []
    t_step = (crvdomain[1]-crvdomain[0])/samples
    t = crvdomain[0]
    for t in rs.frange(crvdomain[0], crvdomain[1], t_step):
        crvcurvature = rs.CurveCurvature(curve_object, t)
        crosssectionplane = None
        if not crvcurvature:
            crvPoint = rs.EvaluateCurve(curve_object, t)
            crvTangent = rs.CurveTangent(curve_object, t)
            crvPerp = (0,0,1)
            crvNormal = rs.VectorCrossProduct(crvTangent, crvPerp)
            crosssectionplane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNormal)
        else:
            crvPoint = crvcurvature[0]
            crvTangent = crvcurvature[1]
            crvPerp = rs.VectorUnitize(crvcurvature[4])
            crvNormal = rs.VectorCrossProduct(crvTangent, crvPerp)
            crosssectionplane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNormal)

        if crosssectionplane:
            csec = rs.AddEllipse(crosssectionplane, bend_radius, perp_radius)
            crosssections.append(csec)
        t += t_step

    if not crosssections: return
    rs.AddLoftSrf(crosssections)
    rs.DeleteObjects(crosssections)
```

| 行      | 描述                                                                                                                                                                                                                                                                                                                                   |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 16      | *crosssections* 用于保存所有椭圆的ID。我们需要保存所有添加的椭圆，以便后续输入为 *rs.AddLoftSrf()* 方法的参数。 *crosssectionplane* 会保存每个单独椭圆的基平面数据，已添加的平面不需要被记住，所以可以使用新产生的平面覆盖掉旧值。<BR>你可能注意到我违反了[2.3.5 使用变量]章节的很多命名惯例。如果你有反对意见，请自己更正这些小问题。 |
| 19      | 我们以等参数间隔沿曲线向前走。这可能不是最好的方法，因为如果曲线是多重直线的话，在子线段上可能参数空间变化非常剧烈。这只是一个示例，所以我想保持代码尽量少，就使用这个不完美的方法了。前面例子里的循环我们使用了同样的技巧，以确保域的最大值不被包含在计算之内。通过减小循环终止条件最大值减去一个很小的数，避免了生成重复圆的问题。   |
| 20      | *rs.CurveCurvature()* 方法返回和曲率分析相关的整组数据。但是它会在线性线段上失效(在线性线段上，曲率半径为无限大)。                                                                                                                                                                                                                     |
| 22...27 | 因此，在上述方法失效的情况下，需要按都老式方法收集标准信息。同时也需要一个 *crvPerp* 向量，因为没有任何返回值。我们可以使用最后一个返回的数据，或者在当前失效曲线分段外寻找一个本地平面，但是我用最简单的办法，直接使用z轴向量。                                                                                                       |
| 28...32 | 如果在t处曲线有曲率，就可以在返回曲率数据里取出需要的信息。                                                                                                                                                                                                                                                                            |
| 33      | 建立椭圆平面。                                                                                                                                                                                                                                                                                                                         |
| 35...37 | 向文件内添加椭圆，并将椭圆曲线ID加入 *crosssections* 列表。                                                                                                                                                                                                                                                                            |
| 40...42 | 建立通过所有椭圆的放榜曲面，然后删除椭圆曲线。                                                                                                                                                                                                                                                                                         |


## 8.6.2 弧线

因为弧线和圆没有太大区别，我想在这里介绍一些额外的知识，不失为一个好主意。这个额外的东西就是程序员所说的“递归”，毫无疑问它是我生活中最令人兴奋的玩意(我不经常出门)。递归是自我重复的过程。循环迭代重复执行相同的代码，递归函数调用自己，因此也重复执行相同的代码，但这个递归的过程是分层次的。实际上，递归并不简单。递归函数的成功案例之一是它们在二叉树中的实现，二叉树是当今世界许多搜索和分类算法的基础。我允许自己在递归的问题上走一点弯路，因为我非常希望你能体会到这个技术的简单性所带来的力量。不幸的是，递归是那些只有在你了解它的工作原理后，才会变得清晰可用的东西。

想象三维空间中的一个盒子，在其体积内包含了许多点。这个盒子内含一种单一的递归行为模式。递归函数对一个单一的条件语句求值：{当盒子体积内包含的点的数量超过一定的阈值时，就将其细分为8个更小的盒子，否则就将自己添加到文件中}。使用简单的If...Else语句很难实现这个功能。接下来，因为新创建的盒子也具有这种行为模式，它迸发出一连串的递归，产生如下图的效果：

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-threshold.svg" width="80%"></div>

在这个情况下，输入是一团大点云，形状像球体的上半部分。点云内部存在一个密集点，其点的密度高于平均水平。由于细分的逼近模式，递归级联的结果生成了这些美丽的盒子堆栈。试图在不使用递归的情况下实现这一结果，将需要大量的步骤和很多很多行的代码。
在我们能够进入酷的部分之前，我们必须写一些支持性的函数，这些函数--我不想说--再次涉及到测角术（角度数学）。

问题：使用起点、终点和起始方向添加一条弧线。正如你所知道的，在Rhino中可以直接用鼠标来完成这个操作。事实上，在Rhino中有14种不同的方法可以手动绘制弧线，但通过脚本添加弧线只有两种方法

- rs.AddArc(Plane, Radius, Angle)
- rs.AddArc3Pt(Point, Point, Point)

第一种方法与使用平面和半径添加圆非常相似，只是增加了扫掠角的参数。第二种方式也类似于使用3点系统添加圆，不同的是，弧线终止于第一和第二点之间。只给定A、B点位置以及起始切线向量，并没有直接的方法来添加弧线。我们必须写一个函数，将所需的起点-终点-方向方法转化为3点方法。在我们处理数学问题之前，让我们回顾一下它工作方式：

<div class="result" markdown>
![](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-arcs.svg){ width="200" align=left }

我们从两个点{A}和{B}以及一个矢量定义{D}开始。我们需要的是红色曲线，但现在我们还不知道怎么画这条线。请注意，如果{D}与{A}到{B}的直线平行或反平行，这个问题就没有解决办法。如果你想在Rhino中画一条这样的弧线，是不可能画出来的。因此，我们需要在函数中添加一些代码，当遇到无法解决的输入时就中止程序。  

我们要找到结果弧线{M}中间点的坐标，然后我们才可以使用{A}、{B}和{M}的3点方法画出弧线。如左图示，弧线中点在与基线中点{C}垂直的线上。

弧线的中点也恰好位于向量{D}和基线向量的二等分线上。通过将两个向量单位化和相加，我们很容易在三维空间中找到两个向量的二等分线。在左图中，平分线已经指向了正确的方向，但仍然没有正确的长度。

我们可以用标准的 "Sin-Cos-Tan直角三角形规则 "计算出正确的长度：

我们要解决的三角形在右下角有一个90º角，a是基线和平分线之间的角度，三角形底边的长度是{A}和{B}之间距离的一半，我们需要计算斜边的长度（{A}和{M}之间）。
</div>


a与三角形边长之间的关系是:

$$\cos({\alpha})=\frac{0.5D}{?} \gg \frac{1}{\cos({\alpha})}=\frac{?}{0.5D} \gg \frac{0.5D}{\cos({\alpha})} = ?$$  

现在我们有了计算斜边长度所需的方程式。唯一剩下的问题是cos(a)。在关于矢量数学的段落中（6.2点和矢量），简要介绍了矢量点积是计算两个矢量之间角度的方法。当我们使用单位化的向量时，点积的余弦给我们提供了它们之间的角度。这意味着点乘法返回这些向量之间的角度的余弦。这是一个非常幸运的转折，因为这个角度的余弦正是我们要找的东西。换句话说，点积使我们不必完全使用余弦和反余弦函数。因此，{A}和{M}之间的距离是以下算式的结果：

`(0.5 * rs.Distance(A, B)) / rs.VectorDotProduct(D, Bisector)`

```python linenums='1'
def AddArcDir(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase) == 0.0:
        return

    if rs.IsVectorParallelTo(vecBase, vecDir):
        return

    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)

    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)

    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5 * rs.Distance(ptStart, ptEnd)) / dotProd

    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, ptEnd, rs.PointAdd(ptStart, vecBisector))
```

| 行      | 描述                                                                                                                                                                                                                                                            |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1       | *ptStart* 参数表示弧线的起点， *ptEnd* 表示终点，*vecDir* 表示 *ptStart* 的方向。这个函数的功能和*rs.AddArc3Pt()*方法类似。它接受一组参数，如果成功，则返回创建的曲线对象的标识符。如果没有添加任何曲线，该函数不会返回任何东西--也就是说，返回值将是 *None* 。 |
| 2       | 创建基线向量（从{A}到{B}），用{B}减去{A}。                                                                                                                                                                                                                      |
| 3       | 如果{A}和{B}是重合的，那么第2行的减法将导致一个长度为0的向量，不可能有解。实际上，有无限多的解决方案，所以我们也不知道该选哪一个。                                                                                                                              |
| 6       | 如果vecDir与基线向量平行（或反平行），那么根本不可能有解决方案。                                                                                                                                                                                                |
| 9...10  | 确保到目前为止所有的向量定义都是单位化的--也就是说，它们的向量长度值都是1。                                                                                                                                                                                     |
| 12...13 | 创建二等分向量，并将其单位化。                                                                                                                                                                                                                                  |
| 15      | 计算平分线和方向向量之间的点积。由于平分线正好在方向向量和基线向量的中间（事实上，这是它存在的意义），我们也可以计算它和基线向量之间的点积。                                                                                                                    |
| 16      | 计算ptStart与所需圆弧中心点之间的距离。                                                                                                                                                                                                                         |
| 18      | 调整（单位化的）平分向量的大小以匹配这个长度。                                                                                                                                                                                                                  |
| 19      | 使用起点、终点和中点参数创建弧线，返回ID。                                                                                                                                                                                                                      |

<div class="result" markdown>
![](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-arctree.svg){width=365 align=right}

我们要用这个函数来写一个递归的树生成器，树枝由输出弧线组成。树的形状由一组5个变量决定，由于递归范式的灵活性，很容易给树增加更多的行为模式。这个例子中实现树增长算法非常简单，不允许有很大的变化。

五个基本参数是：

1. 增殖系数  
2. 树枝长度  
3. 树枝长度突变  
4. 树枝角度  
5. 树枝角突变 
</div>


增殖系数是一个数字范围，表示每个分支末端生长树枝数量的最小值和最大值。这是一个完全随机的事情，这就是为什么它被称为"系数"而不是 "数字"。稍后会有更多关于随机数的内容。你可能已经猜到，树枝长度和树枝长度突变分别控制树枝的长度，和每一代树枝的长度的变化。树枝角度和树枝角度突变以类似的方式工作。

实际递归算法不会处理树枝的增加和弧线形状。这个功能由一个辅助函数完成的，在我们开始生成树之前，必须先写好这个函数。添加新树枝时遇到的问题是，我们希望树枝能平滑地连接到它们的父分支上。我们已经有了能画出切线连续弧线的程序，但还没有挑选终点的机制。在目前的植物生长方案中，树枝的生长由两个因素控制的：长度和角度。然而，由于一个树枝的末端可能有不止一个树枝在生长，所以需要有一定量的随机变化，以确保树枝看起来各不相同。

<div class="result" markdown>
![](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-branchpropagation2.svg){ width="325" align=right } 
<br>
旁边的插图显示了用于树枝增殖的算法。红色曲线是分支弧线，我们需要在末端填充任意数量的树枝弧线。点{A}和向量{D}是由分支的形状决定的，但在长度和角度的限制范围内，我们可以自由地随机选择点{B}。所有可能的终点集合位于黄色锥体内。我们将使用一串向量方法来得到随机点{B}在黄色锥体内的位置：
<br>

1. 创建一个与{D}平行的新向量{T}。<br>
   
2. 调整{T}的大小，使其长度在{Lmin}和{Lmax}之间。<br>
   
3. 突变{T}，使之与{D}有一点偏差<br>
   
4. 围绕{D}旋转{T}，使其方向随机化<br>

</div>

<hr>

```python linenums='1'
def RandomPointInCone(origin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize(direction)
    vecTwig = rs.VectorScale(
        vecTwig, minDistance + random.random() * (maxDistance - minDistance)
    )
    MutationPlane = rs.PlaneFromNormal((0, 0, 0), vecTwig)
    vecTwig = rs.VectorRotate(vecTwig, random.random() * maxAngle, MutationPlane[1])
    vecTwig = rs.VectorRotate(vecTwig, random.random() * 360, direction)
    return rs.PointAdd(origin, vecTwig)
```

| 行    | 描述                                                                                                                                                                                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | *origin* 就是点{A}。<BR> *direction* 就是向量{D}。<BR> *minDistance* 和 *MaxDistance* 表示锥体长度方向的限值。<BR> *maxAngle* 指定锥体的方向范围(单位是度，不是弧度)。                                                           |
| 2...3 | 创建一个与 *Direction* 平行的新向量，并调整其大小至 *MinDistance* 和*MaxDistance* 之间。我在这里使用 *random()* 函数，它是一个Python的伪随机数前端。它总是返回一个介于0和1之间的随机值。                                         |
| 6     | 为了让 *vecTwig* 产生突变，需要用到一个平行向量。因为这里只有一个向量，我们不能直接使用 *rs.VectorCrossProduct()* 方法来产生这个向量，所以我们会构建一个平面并使用它的x轴。这个向量方向随机，但是总是和 *vecTwig* 保持垂直关系。 |
| 7     | 通过围绕平面x轴旋转一个随机角度，让 *vecTwig* 产生突变。                                                                                                                                                                         |
| 8     | 通过围绕 *Direction* 向量旋转，再次让 *vecTwig* 产生突变。这一次随机角度限定于0至360度之间。                                                                                                                                     |
| 9     | 创建由 *Origin* 和 *vecTwig* 推断出来的点。                                                                                                                                                                                      |

维基百科提到关于递归主题的定义中，有一个是："为了理解递归，人们必须首先理解递归"。这显然只是为了搞笑，但实际上这也是一个明确无误的事实。下面的程序完全符合递归的定义，同时也相当短。它会产生视觉上有趣的效果，但是很明显它只是一个简陋的植物生成器。要想完美模仿现实中的树，可以通过试错法进行探索。这个程序可能比本入门手册中的任何其他示例程序都更值得玩味。你可以按照你认为合适的方式，修改、变更、改变、扭曲和弯曲它，看会产生什么样的结果。

任何合法递归函数都必须遵守一套规则：


1.	在程序结束前，必须至少对自己进行一次调用。<br>
2.	即使不对自己进行任何调用，也必须有一种退出方式<br>

如果不满足第一个条件，该函数就不能被称为递归，如果不满足第二个条件，它就会调用自己，直到时间停止（或者说直到你的计算机中的调用栈内存耗尽）。

见证奇迹的时刻到了!

仅仅21行代码就能描述一整棵树的生长。


```python linenums='1'
def RecursiveGrowth(ptStart, vecDir, props, generation):
    minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation = (
        props
    )

    if generation > maxGenerations:
        return

    # Copy and mutate the growth-properties
    newProps = props
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    if maxTwigAngle > 90:
        maxTwigAngle = 90

    # Determine the number of twigs (could be less than zero)
    newProps = (
        minTwigCount,
        maxTwigCount,
        maxGenerations,
        maxTwigLength,
        lengthMutation,
        maxTwigAngle,
        angleMutation,
    )
    maxN = int(minTwigCount + random.random() * (maxTwigCount - minTwigCount))
    for n in range(1, maxN):
        ptGrow = RandomPointInCone(
            ptStart, vecDir, 0.25 * maxTwigLength, maxTwigLength, maxTwigAngle
        )
        newTwig = AddArcDir(ptStart, ptGrow, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            RecursiveGrowth(ptGrow, vecGrow, newProps, generation + 1)
```

| 行      | 描述                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1       | 函数参数说明。除了比较明显的两个参数 *ptStart* 和 *vecDir*，此函数还接收另外2个参数：1个元组和1个代数计数器。元组包含所有生长参数。因为多达7个参数，所以我不想一个一个输入就打包成元组。另外这样也比较方便更改参数，而不是每次更改参数就要去更改函数的调用。代数计数器参数是整数，告诉函数现在产生是第几代树枝。通常情况下，递归函数不需要知道它的深度，但是在这个程序里是个例外，因为代数是递归函数的结束条件。 |
| 2       | 为了可读性，我们对元组进行解包。在赋值侧，7个变量按顺序排列。参数元组包含以下值：<BR><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-data-table.svg" width="100%" float="right">                                                                                                                                                                                                      |
| 6       | 如果当前代数超过了最大允许代数限制(在参数元组第3个数，解包并赋值给maxGenrations)，函数会终止并跳出。因此，在递归继承上它会回退一步。                                                                                                                                                                                                                                                                             |
| 10      | 在这里我们复制了一份参数元组。在后面可以看到，如果我们生成新的树枝，那些树枝会调用新的突变参数，但是在当前 函数实例中，我们要求固定的参数。                                                                                                                                                                                                                                                                      |
| 11...12 | 对复制参数进行突变。即，用最大树枝长度乘以树枝长度突变值，对角度进行同样的处理。为了确保角度不至于失控，我们把角度突变限制于90度以内。                                                                                                                                                                                                                                                                           |
| 26      | *maxN* 为整数，表示即将生成树枝的数量。*maxN* 是从最小值与最大值之间随机挑选的( *Props(0)* 和 *Props(1)* )。*random()* 函数返回0和1之间的随机数，意味着maxN可以是这两个限值之间的任何一个数。                                                                                                                                                                                                                    |
| 28      | 在这里我们使用已经定型的参数选择一个随机点。这里的长度约束是介于1/4长度最大值与最大值之间。在整个宇宙里，没人告诉你要选择0.25这个数，完全是随机乱选的。但是它对最终生成树的外形有很大影响。意味着并没有办法精确的指定树枝的长度。这里有很大的变化空间与实验性。                                                                                                                                                  |
| 31      | 创建属于这条分支的弧线。                                                                                                                                                                                                                                                                                                                                                                                         |
| 32      | 如果 *ptStart* 和 *ptGrow* 之间的距离是0.0，或者如果 *vecDir* 与 *ptStart* >> *ptGrow* 平行，那么就不能成功添加弧线。我们需要及时发现这个问题。                                                                                                                                                                                                                                                                  |
| 33      | 我们需要知道新创建的弧线末端的切线。曲线的域由两个值组成（下限和上限）。 *rs.CurveDomain(newTwig)(1)* 将返回域的上限。这些调用以下函数结果相同：<BR>`crvDomain = rs.CurveDomain(newTwig)`<BR>`vecGrow = rs.CurveTangent(newTwig, crvDomain[1])`                                                                                                                                                                  |
| 34      | 沃了个去！老铁！一个函数调用了它自己！这就是递归函数！我们成功了！<BR>需要搞清楚的是，这次调用是不同的。我们输入了新的参数给这次调用，意味着这个新函数实例，与当前函数实例的执行会有不同的结果。                                                                                                                                                                                                                 |

可以用迭代（For 循环）的方式来写这个树形生成器。生成的树看起来差不多，但是代码会有很大不同（可能会多出很多行）。分支的添加顺序很可能也会不同。下面的树是典型的数字生成树，左边的树是用迭代法生成的，右边的树是用递归法生成的。注意分支顺序的不同。如果你仔细分析一下上一页的递归函数，你就会发现这种差异来自哪里...

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer_iterativetree_vs_recursivetree.svg" width="80%"></div>

不同设置组合的一个小小比较表。请注意生成的树有很高的随机性。

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-treechart.png" width="100%"></div>
