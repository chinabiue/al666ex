---
tags: Rhino-Python-Primer-101
icon: material/texture-box
# categories: book
# date: 
#     created: 2022-01-13 21:55:22
#     updated: 2024-05-28 20:49:29
# authors:
#     - Alex
---
# 8.5 平面

在Rhino中平面并不是真正的物体，它的功能主要是用来在3D世界空间定义坐标系。实际上，最好把平面想象成向量，它们只是数学结构而已。虽然在Rhino内部平面是用参数等式定义的，我发现把它当成一组轴来理解更好:

<div align=center><img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-planedefinition.svg" width="45%"></div>

平面由包含1个点和3个向量的数组组成，点构成平面的原点，3个向量代表3个轴。平面的定义有一些规则。因此，不是所有由1个点和3个向量的组合都是平面。如果使用RhinoScriptSyntax平面方法创建平面，你不会担心这一点，因为程序会处理好所有一切。平面的规则如下：

- 轴向量必须单位化(长度为1.0)。
- 所有轴必须互相垂直。
- x轴和y轴为逆时针方向。

上图展示了规则2和3。

```python
import rhinoscriptsyntax as rs
ptOrigin = rs.GetPoint("Plane origin")

ptX = rs.GetPoint("Plane X-axis", ptOrigin)
ptY = rs.GetPoint("Plane Y-axis", ptOrigin)

dX = rs.Distance(ptOrigin, ptX)
dY = rs.Distance(ptOrigin, ptY)
arrPlane = rs.PlaneFromPoints(ptOrigin, ptX, ptY)

rs.AddPlaneSurface(arrPlane, 1.0, 1.0)
rs.AddPlaneSurface(arrPlane, dX, dY)
```
<!--more-->

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-planecreation.svg){ align=right width=325 }

你会发现所有rhinoscriptsyntax模块中需要平面定义的方法都要确保平面规则得到满足，不管你定义的输入有多不充分。

右边图片展示了11行rs.AddPlaneSurface()调用生成的红色平面，而12行rs.AddPlaneSurface()的调用生成的黄色平面，它的尺寸等于你选择的原点到轴点的距离
</div>

平面与向量类似，通常只是结构元素，因此我们不会在平面定义上花太多时间。在后面的例子里我们会广泛使用平面，所以不用担心在它身上花的时间不够。下面是一个有趣例子，使用 *rs.AddPlaneSurface()* 方法在平面上放置所谓平面框架(曲面表面的UV框架网格):

```python linenums='1'
import rhinoscriptsyntax as rs

idSurface = rs.GetObject("Surface to frame", 8, True, True)
intCount = rs.GetInteger("Number of iterations per direction", 20, 2)

uDomain = rs.SurfaceDomain(idSurface, 0)
vDomain = rs.SurfaceDomain(idSurface, 1)
uStep = (uDomain[1] - uDomain[0]) / intCount
vStep = (vDomain[1] - vDomain[0]) / intCount

rs.EnableRedraw(False)
for u in range(int(uDomain[0]),int(uDomain[1]), int(uStep)):
    for v in range(int(vDomain[0]),int(vDomain[1]),int(vStep)):
        pt = rs.EvaluateSurface(idSurface, u, v)
        if rs.Distance(pt, rs.BrepClosestPoint(idSurface, pt)[0]) < 0.1:
            srfFrame = rs.SurfaceFrame(idSurface, [u, v])
            rs.AddPlaneSurface(srfFrame, 1.0, 1.0)
rs.EnableRedraw(True)
```

<div class="result" markdown>
![Image title](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primersurfaceframes.svg){ align=right width=325 }

框架就是用来指示几何方向的平面。曲线、曲面和有浮凸结构的网格都有框架指示其方向，对曲线来说是切线和曲率，对曲面和网络来说是[u]和[v]方向。

上面的例子简单的在给定曲面的[u]和[v]方向迭代，在所有经过的uv方向添加平面框架。
</div>

第5行和第6行用于确定平面在u和v方向的域，从域的值里我们得到步进值。

第11行和第12行组成2维迭代的主结构。对于嵌套for循环可以这样理解“迭代所有列，然后在每一列迭代所有行”。


第14行做了一些有趣的工作，并没有在图片中展示出来。当给定曲面是修剪过的曲面时，上面两行阻止程序在剪掉的区域添加平面。通过比较修剪前曲面的点与它投影到已修剪曲面的点，我们知道所讨论的[uv]坐标是否代表修剪表面上的实际点。

 *rs.SurfaceFrame()* 方法返回一个单位化的框架，它的轴点在曲面[u]和[v]方向。注意[u]和[v]方向并不要求互相垂直，但是我们只添加x和y轴互为90º的合法平面，因此我们忽略了v的方向。