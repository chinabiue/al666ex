---
tags: Rhino-Python-Primer-101
icon: material/vector-curve
# categories: book
# authors:
#     - Alex
# date: 
#     created: 2022-02-03 21:48:14
#     updated: 2024-05-28 21:20:50
---

# 8.7 Nurbs曲线

圆和弧线都完美且整洁，但是它们不能用来画自由造型。画自由造型需要样条曲线。世界上最著名的样条曲线可能是贝塞尔曲线，它是由法国工程师 *Pierre Bézier* 于1962年在雷诺工作时研发的。大多数现今使用的计算图形样条曲线都是贝塞尔样条曲线的变种，是数学舞台上近年来最令人惊讶的后来者。其他在样条曲线领域作出开拓性工作的人有雪铁龙的 *Paul de Casteljau* 和通用的 *Carl de Boor* 。可以看出的事实是，所有这些人都来自于汽车制造业。随着引擎功率和道路质量的增长，汽车工业从20世纪中期开始面对各种新的问题，其中一个就是空气动力学。需要新技术去设计有平滑、流畅曲线的量产汽车，以取代老旧的相切、曲率造型汽车。他们需要数学上的精确，自由的几何造型。他们选择了样条曲线。

在开始讲Nurbs曲线之前(它的数学基础对一个编程入门者来说略复杂)，先给大家一个印象：样条曲线通常是如何工作的，特别是贝塞尔曲线。我会解释Casteljau算法，它是一种很直接的计算简单样条曲线特性的方法。在实际应用中，这个算法很少使用，因为它比其他替代方法表现差，但是由于它的视觉过程很直观，比较容易从它身上‘找到感觉’。

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-nurbsalgorithm.svg" width="85%"></div>
<!--more-->
限于4个控制点的样条曲线当然不是这项科学的最终演变。很快就有更先进的样条曲线定义出现了，NURBS曲线就是其中一个。(先澄清事实:NURBS代表Non-Uniform Rational [Basic/Basis] Spline，而不是像有些人想的那样是Bézier-Spline。实际上Rhino的帮助文件正确的指出了这一点，但是我怀疑有没有去阅读词汇表那一部分，我也是刚刚发现的。)贝塞尔曲线是NURBS曲线的子集，也就是说所有贝塞尔曲线都可以用NURBS曲线来表示，但是反之不亦然。其他现在还在使用的曲线(Rhinoi不支持)有：Hermite, Cardinal, Catmull-Rom, Beta 和 Akima 样条曲线，提到的曲线只是所有曲线的一部分。比如Bongo动画插件就使用的Hermite曲线，通过一组关键帧来平滑变形物体。

除了控制点位置以外，NURBS曲线还有其他特性比如阶数、节点向量和权重。我假设你已经知道权重的工作方式了(如果没有，请参考Rhino帮助文件[关于NURBS])，所以在这里不讨论这个话题。接下来要讨论的是，曲线阶数和节点向量之间的关系。

NURBS曲线都有一个代表其阶数的数字与其相关。曲线的阶数总是一个[1,11]区间内的正整数。曲线的阶数写为$D^N$。因此$D^1$是1阶曲线，$D^3$是3阶曲线。下一页的表展示了一组拥有同样控制多边形的，但是不同阶数的曲线。简而言之，曲线阶数决定了控制点的影响范围。阶数越高，范围越大。

回想一下本节的开始，一条2次贝塞尔曲线由4个控制点定义。与之不同的是，一条2次NURBS曲线可以由任意控制点定义(实际上是任意大于3的数字)，也就是说整条曲线是由许多线段连接而组成的。下图展示了一条有10个控制点的$D^3$曲线。所有不同的分段用颜色区分开来。你可以看到所有单独分段的形状都很简单：可以用传统的4点贝塞尔曲线方法去近似得到。现在你应该知道为什么NURBS和其他样条曲线被叫做“分段曲线”的原因了。

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-piecewisecurve.svg" width="100%"></div>

红色分段的外形完全由前4个控制点决定。实际上，因为这是一条$D^3$曲线，曲线的每一分段形状都由4个控制点决定。所以第2段(桔段)由{A; B; C; D}点决定。这些分段和传统贝塞尔曲线最大的不同是：这些分段在局部控制多边形附近终止。桔色段不会一直延伸到{D}点，而是会在{C}点附近终止，给接下来的绿色段让路。因为样条曲线的数学特性，桔色段和绿色段完美连接，在连接点4片它们有完全相同的位置、切线和曲率。

你可能已经猜到了，在分段上的白点就是这条曲线的节点向量。这条$D^3$曲线有10个控制点，12个节点(0~11)。这不是一个巧合，节点的数量与控制点和阶数有着直接的关系：

$$K_N = P_N + (D-1)$$

${K_N}$是节点数量，${P_N}$是控制点数量，${D}$是阶数。

上一页的图片中，在开始和结束的红色段和紫色段实际上已经接触了控制多边形顶点，因为我们为了让曲线延伸到顶点做了额外的努力。这种努力叫‘钳位’，通过在特定位置堆积很多节点就叫钳位。你可以看到，要让线段达到控制点需要堆积的点的数量等于曲线的阶数：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-curveknot.svg" width="100%"></div>

一条钳位曲线在开始和结束总是有节点的聚集(周期性曲线没有，这个后面再说)。如果曲线在中间部分有节点簇集，这会导致曲线和其中一个控制点重合，这样我们就有了一条锐角曲线。关于节点还有很多需要了解的，但是我建议继续探讨一些简单的NURBS曲线，从现在开始让Rhino来操心节点向量的事。
<div STYLE="page-break-after: always;"></div>

## 8.7.1 控制点曲线

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-filletcorners.svg){ width="190" align=right }
 <br>
Rhino里的 *_FilletCorners* 命令能在多重直线锐角处放置倒角。因为倒角是切线弧，所以要求角是平面角。因此所有平面曲线总是可以像右图那样进行倒角。

输入曲线{A}有9个$G_0$角(实心点)可以进行倒角操作，3个G1角(空心点)无需进行倒角。因为每一段曲线的长度都大于倒角半径的2倍，没有倒角互相干涉，可以预见到最终结果会如曲线{B}所示。

因为混合曲线是自由形体，允许任意扭曲和弯曲。有非平面的组成部分对它们来说并不是问题。我们今天的任务编写程序把多重直线倒角。我们不并准备处理多重曲线(带自由曲线分段)，因为那涉及了太多数学和逻辑问题，超过这个简单的曲线介绍内容。所以很不幸我们的程序不能处理非平面倒角问题。

 <br>
</div>

我们倒角程序的逻辑很简单：

- **对多重直接的所有分段依次迭代。**
- **对分段起点{A}，在距离A点长度{R}处放置一个额外的控制点${W_1}$。**
- **对分段终点{B}，在距离B点长度{R}处放置一个额外的控制点${W_2}$。**<br>
- **在${A; W_1; W_2; B}$中间，放置一个额外的控制点。**<br>
- **使用所有的新控制点插入一条$D^5$NURBS曲线。**<br>

或者，请看如下图示过程：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-blendcurved5.svg" width="100%"></div>

图1是输入曲线，锁定格点放置。最短边长度为1.0，最长边长度为6.0。如果我们要按0.75长度倒角(图2圆圈)，可能看到其中一个边的倒角半径重叠了。

图3展示了原来的控制点(实心点)和所有的倒角半径控制点(空心点),空心点以距离{R}最近端点放置。两个红色控制点距离各自两边端点为0.5(分段长度一半)。

最一张图，展示了所有控制点中间添加的控制点。一旦我们有了按顺序排列的所有控制点数组(按原多重直线顺序排列)，就可以通过 *rs.AddCurve()* 创建$D^5$曲线。


```Python linenums='1'
def blendcorners():
    polyline_id = rs.GetObject("Polyline to blend", 4, True, True)
    if not polyline_id: return
    vertices = rs.PolylineVertices(polyline_id)
    if not vertices: return
    radius = rs.GetReal("Blend radius", 1.0, 0.0)
    if radius is None: return

    between = lambda a,b: (a+b)/2.0
    newverts = []
    for i in range(len(vertices)-1):
        a = vertices[i]
        b = vertices[i+1]
        segmentlength = rs.Distance(a, b)
        vec_segment = rs.PointSubtract(b, a)
        vec_segment = rs.VectorUnitize(vec_segment)

        if radius<(0.5*segmentlength):
            vec_segment = rs.VectorScale(vec_segment, radius)
        else:
            vec_segment = rs.VectorScale(vec_segment, 0.5*segment_length)

        w1 = rs.VectorAdd(a, vec_segment)
        w2 = rs.VectorSubtract(b, vec_segment)
        newverts.append(a)
        newverts.append(between(a,w1))
        newverts.append(w1)
        newverts.append(between(w1,w2))
        newverts.append(w2)
        newverts.append(between(w2,b))
    newverts.append(vertices[len(vertices)-1])
    rs.AddCurve(newverts, 5)
    rs.DeleteObject(polyline_id)
```

大坑：生成的列表里Point3d和Vector3d混合，不能生成曲线。

| 行      | 描述                                                                                                                                                                                                             |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2...7   | 弹出提示让用户选择多重直线，获取多重直线顶点，然后再弹出提示用户输入倒角半径。因为David Rutten是唯一特许可以不检查None值的高手(我们不是他)，所以我们在每个语句后跟一句错误检查语句。                             |
| 9...10  | 有时，在循环内使用的某些操作的结果是不变的。像这样的情况，通过把这些操作提到循环之前，会大大加快程序的效率。between变量和 *newverts* 在第25行才会使用，但是把它们提前到循环之前，程序会更有效率。                |
| 11      | 开始对每个分段进行循环。                                                                                                                                                                                         |
| 12...13 | 保存*A*、*B* 的坐标，这样更容易引用。                                                                                                                                                                            |
| 15...21 | *vec_segment* 是一个从 *A* 指向 *B* 的缩放矢量，长度为 *radius* 。                                                                                                                                               |
| 23...24 | 计算 *W1* 和 *W2*。                                                                                                                                                                                              |
| 25...30 | 按顺序把所有点(除了 *B* 点)存入 *newverts* 列表。                                                                                                                                                                |
| 31      | 把多重直线最后一点存入 *newverts* 列表。在上面的每一次循环我们都略过了终点 *B* ，因为下一分段的起点 *A* 就是上一分段的 *B* 点，我们不需要重合的控制点。最后一分段没有下一分段了，所以这次我们就把 *B* 加入列表。 |
| 32...33 | 创建$D^5$曲线，删除原输入曲线。                                                                                                                                                                                  |

## 8.7.2 内插点曲线

当创建控制点曲线时很难让曲线通过特定点。即使通过调整控制点也不能容易的做到。这就是为什么像 *_Hbar* 这样的命令重要的原因了。然而，如果想要曲线通过很多点，可以使用内插点方法，而不是使用控制点方法。*_InterpCrv* 和 *_InterpCrvOnSrf* 命令允许创建通过任何数量3D点的曲线，这两个命令在RhinoScriptSyntax模块里都有对应函数实现。

为了示范内插点曲线，我们要写一个程序，在曲面生成结构线，而不是使用系统内置的曲面参数结构线，或者像别处说的‘等高线’。结构线，连接曲面空间有相同u或v值的所有点。因为曲面域值的演进不是线性的(在某些地方可能压缩，在某些地方可能拉伸，特别是在曲面紧绷的边缘附近)，所以结构线之间的距离也不能保证处处相同。

我们算法的描述非常直接，但是我敢保证实际的代码绝对是迄今为止最难搞的。

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-isocurves.svg" width="100%"></div>

我们的程序，对于任意基平面(图A)，抽取一定数量的结构线(图B)。然后，修剪每一条结构线至指定长度(图C)，连接所有终点，就生成了等距结构线(图D中的红线)。请注意，我们使用v方向的结构线生成u方向的等距结构线。用这个方法，结构线的分布并不均匀并不影响最终结果。另外请注意，此方法只适用于偏移曲面边，不像 *_OffsetCrvOnSrf* 可以偏移任意曲线。

对于步骤B和D，我们可以使用RhinoScriptSytnax模块的 *rs.ExtractIsoCurve()* 和 *rs.AddInterpCrvOnSrf()* 方法，但是步骤C需要更多的思考。其中一种可能性是，把抽取的结构线按一个指定长度分割，就可以得到一个点的列表，这个列表的第2个值就是我们需要的解决方案：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/python-dividecurvesearching.svg" width="100%"></div>

如上图示，曲线按5个单位长度分割。红点(集合的第2个数据)就是我们要找的答案。其他所有的点对这个程序来说没用，所以你可以想象得到，分割长度越短，就会产生越多没用的点。通常情况下我会毫不犹豫的使用 *rs.DivideCurveLength()* 这个方法。但是在这里，我要用这个机会向大家介绍一个在编程领域无所不在的、最流行和广泛的算法：二分查找法。

想象一个有10,000个整数的列表，你想找一个离16最近的数。如果列表是无序的(与之对应的是有序)，像这样：

!!! note ""

    {-2, -10, 12, -400, 80, 2048, 1, 10, 11, -369, 4, -500, 1548, 8, … , 13, -344}


你别无选择，开始一个一个比较，并保持一个记录点，记录迄今为止离16最近的数。如果16不在列表内，在你知道哪个数离16最近之前，你要比较10,000次。这就是大家所说的：最坏情况；最好情况就是只需要进行一次比较，如果你足够幸运， 16在列表第1位的话。

上面描述的方法叫列表搜索，对大量的数据集来说这是一个很低效的方法，因为在计算科学里，搜索大数据集是一个很常见的操作，所以有很多研究如何加快这个操作。现在搜索算法层出不穷，我们不得不把它们分类以理清状况。但是，基本上所有的高效搜索算法都依赖于输入列表的有序性，比如：

!!! note ""

    {-500, -400, -369, -344, -10, -2, 1, 4, 8, 10, 11, 12, 13, 80, … , 1548, 2048}


一旦有了有序列表，就有可能把最坏情况的表现提升几个数量级。比如，考虑一个稍微先进一点的列表搜索算法：一旦情况变坏，就立即终止搜索。和原来一样，从列表第1个元素{-500}开始比较，然后继续到第2个元素{-400}。因为{-400}比{-500}更靠近16，所以有理由相信列表下一个元素仍旧会更靠近16。这一机制会一直执行到列表元素{13}。13已经很靠近16，但是还有挣扎空间，我们仍然不能100%保证这就是最终结果({14; 15; 16; 17; 18}都比13更靠近，{19}和13一样靠近)。然而，列表下一个元素是{80}，这比13差得太多了。因为列表是按顺序排列的，我们可以确定{80}以后的每一个数字都会比{80}更差，所以我们可以安全的退出搜索，并得到13是最靠近的16的数字。如果最终结果在列表前端，搜索过程会特别高效；如果在末端，搜索过程会仅仅有一点点提升而已。但是平均上来说，有序列表搜索比无序列表搜索快2倍。

二分查找法表现得更好。让我们回到实际的问题上来看二分查找法是如何工作的：在曲线上找1个离曲线的起点定长的点。如下图，我们要找的点是黄标点，当然在开始查找的时候我们并不知道这个点在哪里。我们不从曲线的起点开始查找，而是从{tmin} 和 {tmax}的一半(曲线域的一半)开始。因为Rhino能提供某个特定子域的长度，我们可以计算出{tmin}到{1}的长度。结果是太长了，我们要找的结果在{tmin}和{1}之间。然后我们又把{tmin}和{1}对半分，得到点{2}。我们又计算{tmin}和{2}的长度，又一次得到结果还是太长了，这是最后一次太长了。我们继续对半剩下的域，直到我们找到点{6}，对我们的目的来说这个点已经够近了：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primerbinarycurvesearching.svg" width="100%"></div>

这是二分查找算法最简单的实现例子，它的算法复杂度为O(log n)，可以说是非常的快了，真的很快。更妙的是，当增大搜索的范围时，查找结果的时间并不会以同样的速率增大(列表查找就会增大)。相反，当集合越来越大的，查找结果的时间相对来说会越来越快。比如，如果把要搜索的列表增大2倍到20,000个元素，列表搜索算法会花2倍的时间查找结果，但是二分查找法的时间只增大了约1.075倍。

二分查找法的原理很容易理解(可能不会立即理解，但你最终会看到它的美)，但是任何实际的实现总会涉及一些烦人的、代码膨胀方面的情况。比如，在开始二分查找法操作之前，我们需要确认最终结果实际上存在于要查找的集合之内。以我们的情况来说，如果我们要在曲线{C}上寻找一点{P}，{P}点离曲线{C}的起点100.0单位，如果曲线{C}长度小于100.0单位，就不会有结果。同时，由于我们搜索的对象是曲线参数域，而不是一个整数列表，并没有一个保存所有可能点的列表去查找。如果要生成这个列表，你的电脑内存可能装不下。但是，我们知道的是理论上任意区间[{tmin},{tmax}]内的数都有可能是结果。最后，有可能并不存在一个精确的结果。我们真正能期望的是找到一个在精确长度公差范围内的结果。计算几何学的很多操作都受约束于公差，有时是因为速度问题(要计算一个精确结果需要时间很长)，有时是因为真的没有一个精确结果(单纯没有可用的数学方法，我们所能做的就是做出一组猜测，每个猜测都比上一个更好)。

无论如何，下面是我写出来的二分查找法程序，内部工作原理我后面再处理：


```Python linenums='1'
def BSearchCurve(idCrv, Length, Tolerance):
    Lcrv = rs.CurveLength(idCrv)
    if Lcrv<Length: return

    tmin = rs.CurveDomain(idCrv)[0]
    tmax = rs.CurveDomain(idCrv)[1]
    t0 = tmin
    t1 = tmax
    while True:
        t = 0.5*(t1+t0)
        Ltmp = rs.CurveLength(idCrv, 0, [tmin, t])
        if abs(Ltmp-Length)<Tolerance: break
        if Ltmp<Length: t0=t
        else: t1 = t
    return t
```

| 行      | 描述                                                                                                                                                                                                                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1       | 请注意这不是完整的程序，这只是搜索函数。完整的程序在后面。这个函数接收3个参数：曲线ID，指定长度和公差。如果没有结果返回值为 *None* (比如，如果曲线长度小于指定长度 *Length* )，如果有结果就返回标记指定长度的参数域值。                                                                                            |
| 2       | 从Rhino获取曲线长度。                                                                                                                                                                                                                                                                                              |
| 3       | 确保曲线长度大于 *Length* 。如果小于指定长度，终止程序。                                                                                                                                                                                                                                                           |
| 5...6   | 保量曲线域值的最大与最小值。如果你对我两次调用 *rs.CurveDomain()* 的行为感到困惑，为什么不只调用一次把结果保存在数组里呢？恭喜你。不再次调用同一函数的确会快一点点。然而，因为第7和第8行并不在循环内，它们只会执行一次，并不影响大局。这个函数99%的执行时间分布在16~25行，如果热衷于追求速度，请对那几行代码下手。 |
| 7...8   | *t0*, *t1* 和 *t* 是用于定义当前子域的变量。*t0* 标记下限，*t1*标记上限。 *t* 位于 *t0* 和 *t1* 段中点。第一次循环是对整个线段执行的，所以 *t0* 和 *t1* 对应 *tmin* 和 *tmax*。                                                                                                                                    |
| 9       | 因为事先不知道二分查找法会运行多少次，所以这里弄一个无限循环。                                                                                                                                                                                                                                                     |
| 10      | 计算 *t* ，确保它总是位于 {*t0*, *t1*}之间的中点。                                                                                                                                                                                                                                                                 |
| 11      | 计算子曲线的长度，从曲线起点(*tmin*)开始，到我们当前的参数(*t*)结束。                                                                                                                                                                                                                                              |
| 12      | 如果长度接近指定长度，那么就完成任务，退出无限循环。 *abs()* -万一有人不知道-就是一个Python函数，返回一个数值的绝缘值(非负值)。这就是说参数 *tolerance* 在正负两个方向都有用，这是大家比较期望的运行方式。                                                                                                         |
| 13...14 | 这是奇迹发生的地方。是不是看起来基本无害？<BR>这里进行的操作是根据比较结果调整子域范围。如果子域{*tmin*, *t*}长度比 *Length* 短，那么我们希望接下为处理的子域是原域的上半部分(通过t0=t)。反之，如果子域{*tmin*, *t*}长度比 *Length* 长，我们需要原域和下半部分(t1=t)。<BR>看到了吗？代码比英语简洁多了。           |
| 15      | 返回查找到的结果 *t* 。                                                                                                                                                                                                                                                                                            |

在一条参数空间相对平均分布(即，在参数域没有突然的密度跳变)的曲线上我运行了这个程序，结果如下表所示。曲线总长为200.0mm,我希望找到125.00mm处的参数空间值。公差设置为0.0001 mm。你可以看到为了找到结果，经过了 *BSearchCurve()* 函数的18次运算。请注意此算法定位到正确值的速度，仅仅经过6步，误差就降至1%。理想情况下，每次运算过后精确度会是上次的2倍，但是在实际运行中可能不会总是有这么完美的进程。实际上如果仔细看表，你会看到有时新的猜测值会过冲以至于计算出的结果比上一次还差(比如#9 至 #10)。

我把相邻2步子域不变的情况用灰色标示出来。可以看到有时在同一方向多次调整是可能发生的。

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-subdivisionchart.svg" width="90%"></div>

现在请欣赏程序的其他部分：

```Python linenums='1'
def equidistanceoffset():
    srf_id = rs.GetObject("Pick surface to offset", 8, True, True)
    if not srf_id: return

    offset = rs.GetReal("Offset distance", 1.0, 0.0)
    if not offset: return

    udomain = rs.SurfaceDomain(srf_id, 0)
    ustep = (udomain[1]-udomain[0])/200
    rs.EnableRedraw(False)

    offsetvertices = []
    u = udomain[0]
    while u<=(udomain[1]+0.5*ustep):
        isocurves = rs.ExtractIsoCurve(srf_id, (u,0), 1)
        if isocurves:
            t = BSearchCurve(isocurves[0], offset, 0.001)
            if t is not None:
                offsetvertices.append(rs.EvaluateCurve(isocurves[0], t))
            rs.DeleteObjects(isocurves)
        u+=ustep

    if offsetvertices: rs.AddInterpCrvOnSrf(srf_id, offsetvertices)
    rs.EnableRedraw(True)
```

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-equidistantoffset-result.svg){width=305 align=right}
如果前面我已经解释得比较清楚了，上面的程序不需要过多解释。所有的代码都比较直白。<BR><BR>

右图展示的程序运行的结果，所有偏移值都乘以10。绿带区域(偏移80.0和90.0之间)的墨绿色线条长度都为10。
</div>

## 8.7.3 几何曲线特性

因为曲线是几何物体，它就拥有一些属性或特性，可以用来描述和分析它们。例如，曲线都有起点和终点坐标。当这两点的距离为0时，曲线是封闭的。同时，曲线都有控制点，如果所有的控制点都处于同一平面，那么这条曲线就是平面曲线。有些属性对曲线来说是全局属性，有些则属于局部属性。例如，平面性是全局属性，而切线向量就是局部属性。另外，基于曲线类型有类型专属的属性。现在为止我们学习过的曲线类型有：直线、多重直线、圆、椭圆、圆弧和Nurbs曲线：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-curvetypes.svg" width="100%"></div>

Rhino里最后一种曲线类型是多重曲线，就是所有其他曲线的混合类型。比如，多重曲线可以由一系列直线组成，这样的话多重曲线的表现就和多重直线相似。但是多重曲线也可以是直线、圆弧和不同阶数NURBS曲线的组合。因为多重曲线内分段要互相衔接(G0连接是多重曲线分段的连接要求)，它内部就不能包含封闭的分段。但是不管多重曲线有多复杂，它都可以用NURBS曲线来表示。所有以上类型曲线都可以用NURBS曲线来表示。

真正的圆和看起来像圆的NURBS圆之间的区别在于存储方式。比如，NURBS曲线没有半径属性，也没有其定义于之上的平面。可以通过计算导数和切向量和帧等来重建这些属性，但是无法直接简单的直接取得这些数据。简而言之，NURBS曲线缺少一些其他曲线类型有的全局属性。这不是个大问题，记住NURBS曲线有或没有某些属性不难。比较难搞的是处理那些不连续的局部属性。比如，想象有一条包含长度为0的线段的多重曲线。曲线开始的t参数空间和和结束的t参数空间值不一样，意味着基中一段子域长度为0。在这个域内是无法计算法线向量的：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-polycurvecompound.svg" width="100%"></div>

这条多重曲线包含5个子曲线段(分别是1条NURBS曲线，1条0长度直线，1条正常直线，1条90°圆弧和另1条NURBS曲线)，它们在t参数空间处互相衔接。它们没有互相正切连接，意味着如果要取得$t_3$处切线，你要么得到的是紫色段终点的切线，要么得到绿色段起点的切线。然而，如果要取得$t_1$和$t_2$中间的切线向量，很抱歉并没有。曲率数据域有更大的空白区，因为两段直线并不存在曲率：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-polycurvelocalevaluation.svg" width="100%"></div>

当使用曲线属性比如切线向量、曲率或垂直框架时，我们必须始终小心，不要盲目地继续前进，而不检查属性的不连续性。Rhino中的 *_CurvatureGraph* 命令正确处理了这个情况。它适用于所有曲线，意味着它必须有能力检测并忽略那些没有曲率的线性和0长度线段。

 *_CurvatureGraph* 命令不能做到的一件事就是插入曲率图像物体，你只能看到曲率预览图而不能把它们插入文件。我们要写一个程序，把曲率图做为一组直线和内插点曲线的集合插入到文件当中。我们会碰到这一章里提到的几个问题。

为了避免 *G* 连续性的问题，我们一小段一小段的分别画曲率图。如果你左脑还好使的话应该记得：每一段节点跨度的外形是由某个数学函数(就是多项式)决定的，在大多数情况下是完全平滑的。一小段一小段分别处理的方法就需要把曲线打断至基本元素段，如左图示：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-polycurvecurvaturegraph.svg" width="100%"></div>

这是一条有7个部分的多重曲线：直线{A; C; E}，圆弧{B; D}和NURBS曲线{F; G}。当把多重曲线转换成NURBS曲线时，得到一个包含62个子线段(节点跨度)的5阶NURBS曲线。因为这条曲线是由其他曲线连接而成，所以在每个单独连接处会有锐角点。如果在曲线内部有一组节点聚集在一起，那一点就定义为锐角点，意味着在那一点曲线实际上穿过了它的控制点。因此，锐角点有可能成为原本平滑曲线中的尖锐转折，但是在上图的曲线中所有锐角点都是G1连接，所以没有很大转折点出现。右图用白圈标示出所有锐角点。你可以看到锐角点也出现在了曲线{B,D}的中部，这些锐角点在组合曲线之前就已经存在了。这条曲线总共有10个锐角点，每个锐角点是5个节点域的聚集(这是1条$D^5$曲线)。因此我们有总共40个0长度节点分段。请不要担心数学方面的问题，这里的重点是我们要针对0长度分段做些准备，以便在遇到它们的时候略过它。

另外一个会遇到的问题就是上一页说到的属性求值问题。在节点转换的过程中，曲率值可能会从一个值跳变到另一个值。只要在节点参数附近对曲率求值，我们就需要知道我们的方向是从左到右还是从右到左。

我敢保证所有这些听起来都超级复杂。实际上，这些概念与方法也真的超级复杂，但是这些复杂性是有其存在意义的。理解程序在理想状态下的工作原理已经远远不够了，从现在开始，你应该去理解为什么没有理想状态，以及这个事实对编程的影响。

既然已经了解模仿 *_CurvatureGraph* 命令需要的基础了，我们不妨从最基本的开始。首先我们需要写一个函数，这个函数能在曲线分段上创建曲率图，然后我们通过节点参数子域不断调用函数，以生成整个曲线的曲率图：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-spancurvaturegraph.svg" width="90%"></div>

我们的函数需要知道曲线的ID，子域{$t_0$; $t_1$},在子域上的采样点数，以及曲率图的比例。返回值应该是插入到文件中建立曲率图的一系列物体ID。就是如上图示中的所有垂直于曲线的红色线段与连接它们的黑色虚线。

```Python linenums='1'
def addcurvaturegraphsection(idCrv, t0, t1, samples, scale):
    if (t1-t0)<=0.0: return
    tstep = (t1-t0)/samples
    points = []
    objects = []
    for t in rs.frange(t0,t1+(0.5*tstep),tstep):
        if t>=t1:t = t1-1e-10
        cData = rs.CurveCurvature(idCrv, t)
        if not cData:
            points.append(rs.EvaluateCurve(idCrv, t))
        else:
            c = rs.VectorScale(cData[4], scale)
            a = cData[0]
            b = rs.VectorSubtract(a, c)
            objects.append(rs.AddLine(a,b))
            points.append(b)

    objects.append(rs.AddInterpCurve(points))
    return objects
```

| 行      | 描述                                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------- |
| 2       | 检查空段，在锐角点处会有空段。                                                                          |
| 3       | 确定循环的步长参数(子域长度 / 采样数)。                                                                 |
| 5       | *objects()* 用于保存生成的垂直线和连接线的ID。                                                          |
| 6       | 定义循环条件，为了确保总是处理到参数域最右端，给右端添加半个步长。                                      |
| 7       | 确保 *t* 不超过 *t1* ，因为如果超过了，会给出下一条线段的曲率。                                         |
| 10      | 在曲率值不连续的情况下，不需要添加直线，而是把曲线上当前 *t* 对应的坐标添加到点列表，用于生成黑色虚线。 |
| 12...16 | 计算A和B的坐标，B点加入点列表用于生成黑色虚线，并生成代表曲率的A至B点的直线。                           |

现在需要写一个功能函数，把上面的函数应用到整条曲线上去。没有高科技，就是基于曲线物体的节点向量进行迭代：

```Python linenums='1'
def addcurvaturegraph( idCrv, spansamples, scale):
    allGeometry = []
    knots = rs.CurveKnots(idCrv)
    for i in range(len(knots)-1):
        tmpGeometry = addcurvaturegraphsection(idCrv, knots[i], knots[i+1], spansamples, scale)
        if tmpGeometry: allGeometry.append(tmpGeometry)
    rs.AddObjectsToGroup(allGeometry, rs.AddGroup())
    return allGeometry
```

| 行  | 描述                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------- |
| 2   | *allGeometry* 存储调用 *AddCurvatureGraphSection()* 生成的所有物体ID。                                |
| 3   | *knots* 是NURBS曲线 *idCrv* 所有的节点向量。                                                          |
| 5   | 需要迭代所有节点区间，意味着需要迭代节点向量内所有节点(除了最后一个)。因此最后需要减1。               |
| 6   | 调用 *addcurvaturegraphsection()* ，保存所有结果至 *tmpGeometry* 。                                   |
| 7   | 如果 *AddCurvatureGraphSection()* 结果不为 *None*, 把 *tmpGeometry* 里所有项目保存至 *allGeometry* 。 |
| 8   | 把所有创建的物体加入群组。                                                                            |

我们要写的最后一段代码比我们所学的要更深入一点。到现在为止，在进行任何操作之前，我们总是会弹出提示，要求用户输入数据。实际上，在提供默认值做为选项的同时，显示预览会用户友好得多。

UI代码往往非常强大，但很少是复杂的。写起来很烦人，因为它看起来总是一模一样。为了给脚本创建一个可靠的命令行界面，您必须执行以下操作：

- 预留保存预览图形的空间
- 用有效的值初始化所有设置
- 使用默认设置创建所有预览图形
- 显示命令行选项
- 解析结果(无论是转义、输入，还是选项或数值)
- 通过所有选项进行分支
- 如果选项项是设置(以区分于其他操作比如‘取消’或‘接受’)，弹出设置提示
- 删除所有预览图形
- 使用新设置，生成新预览图形

```Python linenums='1'
def createcurvaturegraph():
    curve_ids = rs.GetObjects("Curves for curvature graph", 4, False, True, True)
    if not curve_ids:
        return

    samples = 10
    scale = 100

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

| 行      | 描述                                                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 2       | 弹出提示选择曲线，可接受任意数量曲线，本程序可处理多条曲线。                                                                                |
| 6...7   | 默认设置：缩放系数为100.0，区间采样数为10。                                                                                                 |
| 9       | *preview()* 是包含ID的嵌套列表。 *idCurves* 里每条曲线对应一个子列表，内含新建物体的ID。                                                    |
| 10      | 因为允许用户无限次改变设置，所以我们的UI代码需要一个无限循环。                                                                              |
| 12...14 | 首先，如果存在预览图形，先全部删除。                                                                                                        |
| 16...18 | 然后，插入新的预览图形。                                                                                                                    |
| 21      | 一旦新的预览图形就位，显示命令行选项。 *rs.GetString()* 方法后面的数组是将要显示的命令行选项列表。                                          |
| 24...28 | 如果用户终止(按下ESC)，删除所有预览图形并退出子程序。                                                                                       |
| 29...41 | 如果用户点击了一个选项， *result* 会保存选项名字。IronPython最棒的地方是处理选择的方式，用 *If...elif* 语句。                               |
| 30      | 如果用户选择"Accept"，在不删除预览图形的情况下，退出子函数。                                                                                |
| 32...37 | 如果用户选择"Samples"，需要向用户拿到新采样数。如果在这个嵌套提示内用户按下了ESC，不需要退出整个程序(Rhino默认行为模式)，回退到上一个提示。 |
| 38...41 | 如果用户选择"Scale"，需要向用户拿到新缩放系数。如果在这个嵌套提示内用户按下了ESC，不需要退出整个程序(Rhino默认行为模式)，回退到上一个提示。 |
| 42...45 | 如果用户输入其他东西，提示用户并重新进入循环。                                                                                              |
