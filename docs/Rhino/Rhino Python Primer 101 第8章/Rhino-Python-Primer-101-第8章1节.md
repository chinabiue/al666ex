---
tags: Rhino-Python-Primer-101
icon: material/record-circle-outline
# authors:
#     - Alex
# categories: book
# date: 
#     created: 2021-12-29 20:39:25
#     updated: 2024-07-13 11:14:54
---

# 8.1 openNURB(tm)内核

现在已经熟悉了基本脚本语法，是时候进入 Rhino 真正的几何部分了。为了保持学习的兴趣，前面有很多例子已经使用了 Rhino 方法，但那些只是前菜。如果你坚持到了现在，那么从此刻开始你将正式进入让你变成 3D 极客的伟大旅程。

第3章说过，Rhino 的核心是 openNURB^TM^，它提供了大部分的几何图形支持和文件 I/O 功能。所有处理几何图形的插件都利用了这个丰富的资源，RhinoScriptSytnax 插件也不例外。虽然 Rhino 是一个`NURBS建模软件`，但是对其他类型的几何图形它也提供支持。这些支持部分向普通 Rhino 用户开放，部分只向编程人员开放。使用 Python 时，用户不会直接面对 openNURBS^TM^ 代码，因为 RhinoScriptSyntax 提供了外层封装，让使用者更方便调用。然而做为编程人员，需要有比普通用户更深入的理解，编程人员需要挖掘得更深入。
