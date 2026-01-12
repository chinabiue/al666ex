---
# title: 1.2. openNURBS(tm)内核/Rhino里的物体
tags: Rhino-Python-Primer-101
icon: material/bee-flower
# authors:
#     - Alex
# categories: book
# date: 
#     created: 2021-12-29 20:39:25
#     updated: 2024-05-28 20:16:42
---
# 8.2 Rhino里的物体

Rhino里的所有物体都由两个部分组成：几何部分和属性部分。几何类型有很多种，但是属性基本上都遵循同样的格式。属性用于存储信息，比如物体名称、颜色、图层、等级曲线密度、线型等等。对几何类型来说不是所有属性都有意义，比如说点就没有使用线型或材质属性，但并不影响它存储这些属性的能力。大多数属性或特性都很简单，可以随意读取和赋予给物体。

<div align=center><img width="90%" src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-rhinoobjects.svg"></div>

上表列出了插件开发者可以访问的大部分属性和特征。它们大部分封装在RhinoScriptSyntax模块中，某些特征在当前暂时不可访问，因为用户自定数据元素比较特殊。我们会在基本几何章节过后再细说用户数据。

下面一小段程序在对话框展示一个物体的一些属性。并没有什么值得激动的东西，所以就略过不一一解释每行了。




```py hl_lines="1 27"

import rhinoscriptsyntax as rs

def displayobjectattributes(object_id):
    source = "By Layer", "By Object", "By Parent"
    data = []
    data.append( "Object attributes for :"+str(object_id) )
    data.append( "Description: " + rs.ObjectDescription(object_id))
    data.append( "Layer: " + rs.ObjectLayer(object_id))
    data.append( "MaterialSource: " + str(rs.ObjectMaterialSource(object_id)))

    name = rs.ObjectName(object_id)
    if not name: data.append("<Unnamed object>")
    else: data.append("Name: " + name)

    groups = rs.ObjectGroups(object_id)
    if groups:
        for i,group in enumerate(groups):
            data.append( "Group(%d): %s" % i+1, group )
    else:
        data.append("<Ungrouped object>")

    s = ""
    for line in data: s += line + "\n"
    rs.EditBox(s, "Object attributes", "RhinoPython")


if __name__=="__main__":
    id = rs.GetObject()
    displayobjectattributes(id)
```

<div align=center><img width="85%" src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/rhino101/primer-objectattributedialog.png"></div>