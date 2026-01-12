---
tags: Rhino-Python-Primer-101
icon: material/vector-point
# authors:
#     - Alex
# categories: book
# date: 
#     created: 2021-12-29 21:11:26
#     updated: 2024-07-03 20:27:19
---
# 8.3 点和点云

点生万物。点不过就是一个坐标值的列表。列表里值的数量对应其所处空间的维度。空间通常用字母R和一个数字上标表示，上标指示空间的维度。（`R`源于真实(real)世界，意味着空间是连续的。我们应该记住，数字化表示的任何东西总是有间隙的，即使、便我们很少面对它们。）

3D空间，或者说 $R^3$ 空间里的点，自然就有3个坐标，通常称为[x,y,z]。$R^2$空间里的点只有2个坐标，叫 [x,y]或者 [u,v]，取决于我们谈论的是什么样的2维空间。$R^1$空间里的点用1个单值表示。虽然我们倾向于认为1维点不算'点'，但是并没有数学上的差别；所有的点都适用同样的规则。1维点通常称为'参数'，用[t]或[p]表示。

<div align=center><img width="90%" src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-rhinospaces.svg"></div>

左边的图片展示的是$R^3$世界空间，连续并且无限。在这个空间，点的X坐标值是点向X轴(红实线)的投影(红点线)。在Rhino中，点始终以世界坐标指定。
<!--more-->
$R^2$世界的空间(没有画出来)和$R^3$世界空间一样，唯一的不同在于2维世界没有Z轴。它也是连续且无限的。然而$R^2$参数空间如中图所示，被约束于一个有限曲面中。它仍然是连续的，比如可以假想曲面上有无限的点，但是这些点中任意两点的最大距离非常有限。$R^2$参数坐标只有在其没有超过某个范围时才有意义。在图中的例子里，在[u]和[v]方向都被限制于0.0至1.0之间，但是也可以设置为其他任意有限的区间。坐标为[1.5, 0.6]的点位于这个曲面之外某处，因此它是无效的。

因为曲面位于定义这个特定参数空间的$R^3$世界空间内，我们总是能把其上的参数坐标转换为3D世界坐标。比如，曲面上的点[0.2, 0.4]与世界坐标上的点[1.8, 2.0, 4.1]是同一点。一旦曲面转换或变形，$R^3$空间内对应[0.2, 0.4]的点坐标也会跟着改变。请注意这个方式反过来说并不成立，我们能把任意$R^2$参数坐标转换成3D世界坐标，但是仍然有很多3D世界坐标并不在曲面上，因此这些不在曲面上的点并不能转换成$R^2$参数坐标。但是我们总是能把3D世界坐标通过最近点关系投影到曲面之上。后面会细说这一点。

如果觉得以上知识点难以理解，请相像一下自己和自己在空间中的位置，可能有所帮助。我们通常倾向于使用本地坐标系统描述自己的位置；“我坐在电影院第7排第3个座位”，“我住在公寓4楼24号房”，“我在后座”。其中的某些坐标和世界坐标系(纬度，经度，海拔)并不一致，另外一些坐标使用了不同的参考点。如果你坐的车子在路上开着，在世界坐标系中你的位置就一直在改变，即使你在‘后座坐标系’中一直保持不动。

让我们从$R^1$到$R^3$空间的转换开始。以下程序会在文件里添加500个色点，所有点都是通过在$R^1$参数空间里的一条曲线物体定长取样而来：

```python linenums='1' hl_lines="30"
import rhinoscriptsyntax as rs

def main():
    curve_id = rs.GetObject("Select a curve to sample", 4, True, True)
    if not curve_id: return

    rs.EnableRedraw(False)
    t = 0
    while t<=1.0:
        addpointat_r1_parameter(curve_id,t)
        t+=0.002
    rs.EnableRedraw(True)

def addpointat_r1_parameter(curve_id, parameter):
    domain = rs.CurveDomain(curve_id)


    r1_param = domain[0] + parameter*(domain[1]-domain[0])
    r3point = rs.EvaluateCurve(curve_id, r1_param)
    if r3point:
        point_id = rs.AddPoint(r3point)
        rs.ObjectColor(point_id, parametercolor(parameter))

def parametercolor(parameter):
    red = int(255 * parameter)
    if red<0: red=0
    if red>255: red=255
    return (red,0,255-red)

if __name__=="__main__":
    main()
```

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-curveparameterspace.svg" width="45%"></div>

虽然没有什么好理由，但是我们从最下面一个函数说起：

<table>
<tr>
<th>行</th>
<th>描述</th>
</tr>
<tr>
<td>24</td>
<td>标准开箱即用函数声明，接受一个double数值参数。本函数应该返回一个颜色元组，当参数从0到1逐渐增大时，颜色从蓝到红渐变。在区间{0.0~1.0}之外的数值会被截断。</td>
</tr>
<tr>
<td>25</td>
<td>被函数返回的代表红色的数值在这里声明，赋值为传入参数的255倍。代表颜色的数据必须位于于区间[0,255]，如果试图用区间之外的数值代表颜色，会引发运行时错误。</td>
</tr>
<tr>
<td>26...27</td>
<td>在这里我们保证程序正确的运行。</td>
</tr>
<tr>
<td>28</td>
<td>计算渐变颜色数值。如果传入参数0，得到的颜色是蓝(0,0,255)；如果传入参数1，得到的颜色是红(255,0,0)。所以中间代表绿色的数值总是0，而红和蓝加起来总是255。</td>
</tr>
</table>

现在开始讲解函数*addpointat_r1_parameter*。和函数名所表示的意思一致，此函数会基于曲线物体的参数坐标在3D世界空间里添加1个单点。为了正常运行，函数必须知道我们指的是哪一条曲线，并且还要知道采样参数。在这里我们并不给函数传送绑定于曲线域(也可以是任意东西)的实际的参数,我们传送给函数'单位参数'1。

即我们假设曲线域为0至1。函数封装了内部的运算，此运算把我们传入的基于单位的0-1之间的数值转换成实际参数。

基于我们调用此函数次数非常多(添加每个点调用一次)，实际上把所有重型运算写在函数里并不明智。实际上我们只需要执行一次‘单位参数 + 实际参数’的开销，所以把它放到更高层的函数里去更有意义。但是这里程序执行得仍然很快，暂时没有必要去搞优化。

| 行      | 描述                                                                                                                                                                               |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 14      | 函数声明。                                                                                                                                                                         |
| 15...16 | 获取曲线域并检查是否为*Null*。如果ID并不代表一条合适的曲线物体，获得的曲线域将会是*Null*。 <br>*rs.CurveDomain()* 方法会返回一个2个double型的数组，代表曲线上的最小和最大的t参数。 |
| 18      | 把R1坐标的单位参数转换成实际域坐标。                                                                                                                                               |
| 19      | 在指定参数处评估曲线。rs.EvaluateCurve()接收一个$R^1$坐标，返回一个$R^3$坐标。                                                                                                     |
| 21      | 添加默认参数点。                                                                                                                                                                   |
| 22      | 设置自定颜色。 这会自动改变物体颜色源属性。                                                                                                                                        |

本例中螺旋线上$R^1$点的分布不是特别直观，因为在$R^3$空间看来它大约是按等长等分了曲线。但是如果在一些并不那么规则的曲线上运行这个程序，就会更容易看出曲线参数空间到底是什么东西：

<div align=center ><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-curvestructure.svg" width="100%"></div>

让我们来看一个使用到所有参数空间的例子:

```python linenums='1'
import rhinoscriptsyntax as rs

def main():
    surface_id = rs.GetObject("Select a surface to sample", 8, True)
    if not surface_id: return

    curve_id = rs.GetObject("Select a curve to measure", 4, True, True)
    if not curve_id: return

    points = rs.DivideCurve(curve_id, 500)
    rs.EnableRedraw(False)
    for point in points: evaluatedeviation(surface_id, 1.0, point)
    rs.EnableRedraw(True)

def evaluatedeviation( surface_id, threshold, sample ):
    r2point = rs.SurfaceClosestPoint(surface_id, sample)
    if not r2point: return

    r3point = rs.EvaluateSurface(surface_id, r2point[0], r2point[1])
    if not r3point: return

    deviation = rs.Distance(r3point, sample)
    if deviation<=threshold: return

    rs.AddPoint(sample)
    rs.AddLine(sample, r3point)

if __name__=="__main__":
    main()
```
<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-surfaceparameterspace.svg){ align=right width=300 }

这个程序比较曲线上的一系列点到它们平面投影之间的距离。如果距离大于1个单位，就添加一个点和一条直线。

首先，$R^1$点被转换至$R^3$空间坐标，这样才能投影到曲面之上，然后返回$R^2$空间坐标[u,v]。
$R^2$点同样也需要转换至$R^3$空间，因为需要计算曲线上$R^1$点到曲面上$R^2$点之间的距离。只有两个点处于同一维度空间，才能测量距离，所以需要把它们全转换至$R^3$空间。
</div>

告诉你这是小菜一碟...

| 行      | 描述                                                                                                                             |
| ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 10      | 使用*rs.DivideCurve()* 方法一次性取得曲线上所有点的$R^3$坐标。此操作节省了大量时间。                                             |
| 24      | *rs.SurfaceClosestPoint()* 返回一个双精度实数数组，代表在曲面上({u,v}坐标)离样点最近的R2点                                       |
| 27      | *rs.EvaluateSurface()* 返回R2参数坐标转换后的R3坐标                                                                              |
| 30...38 | 计算两点之间的距离并按条件添加几何体。此函数在距离小于1时返回值为True,在大于1时返回值为False, 如果程序出现问题，返回值则为Null。 |

再强调一次。我们把曲线上$R^1$参数坐标投影至3D空间(步骤A)，然后把$R^3$坐标投影至曲面，以获得最近点的$R^2$坐标(步骤B)。我们在$R^2$空间计算曲面，得到3D世界空间的$R^3$坐标(步骤C)，最后我们计算两个$R^3$点的距离，以确定最终偏差：

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-surfaceparameterspacediagram.svg" width="60%"></div>
