---
title: 生成艺术Generative art with samila
---
![Power by Samila](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/20.png)

生成艺术，就是计算机根据算法自动生成的艺术作品。

感觉挺好玩的，编程定好规则，就会自动生成一系列艺术作品。

这是一个python玩具： [Samila项目说明](https://al666ex.pages.dev/blog/2022/01/12/samila%E9%A1%B9%E7%9B%AE%E8%AF%B4%E6%98%8E/)

用tkinter做了一个简单的界面，使用Samila生成属于自己的独一无二的图片。

![可选颜色/seed/分辨率/投影方式](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/tkinter.png)
!!! info ""

    - 可选颜色156种

    - 种子影响最终生成图形形状，规律暂时不明

    - 分辨率解析：选1生成1000x1000图片，选2生成2000x2000图片，以此类推

    - 投影方式有6种，差别请亲自体验

<!-- more -->

变换参数可以生成的一些有意思的图片

![POLAR模式下](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/21.png)

![RECTILINEAR模式下](https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/22.png)


这个小程序的可玩性/可更改性有：

- 可以变换参数生成不同的图片
- 可以动手添加新函数，f3/f4/f5....以替换原函数生成新的完全不一样模式的图片
- 练习tkinter
- 这就是艺术？整挺美


完整的代码请参考。
```python
import math
import random
from tkinter import *
from tkinter.ttk import *
from samila.params import VALID_COLORS
from samila import GenerativeImage, Projection


def f1(x,y):
    result = random.uniform(-1,1) * x**2 - math.sin(y**3) + abs(y-x)
    return result

def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

def generate(spin,comb1,spin1,comb,txt):
    sed = spin.get()
    pro = Projection.__members__[comb1.get()]
    res = int(spin1.get())

    g = GenerativeImage(f1,f2)
    g.generate(seed=sed)
    g.plot(color=comb.get(),bgcolor="white",projection=pro)
    g.save_image(file_adr=f'{txt.get()}.png', depth=res)

def get_png_name(comb, comb1,file_name):
    file_name.set(value=comb1.get() + '-' + comb.get())

def main():
    win = Tk()
    win.title('生成随机图片')
    win.geometry('420x420')

    lbl = Label(win, text='选择参数',font=('Microsoft Yahei',12))
    lbl.grid(column=0, row=0, sticky='w')

    lbl_pro = Label(win, text='投影')
    lbl_pro.grid(column=0, row=5, sticky='w')
    comb1 = Combobox(win)
    comb1['values'] = tuple(Projection.__members__)
    comb1.current(1)
    comb1.grid(column=1, row=5, sticky='w')

    lbl_color = Label(win, text='颜色')
    lbl_color.grid(column=0, row=2, sticky='w')
    comb = Combobox(win)
    comb['values'] = tuple(VALID_COLORS)
    comb.current(random.randint(0,156))
    comb.grid(column=1, row=2, sticky='w')

    btn_file_name = Button(win, text='文件名称', command=lambda: get_png_name(comb, comb1,file_name))
    btn_file_name.grid(column=0, row=1, sticky='w')
    lbl_des = Label(win, text='请点击按钮生成，或手动输入')
    lbl_des.grid(column=2, row=1, sticky='w')
    file_name = StringVar(value=comb1.get() + '-' + comb.get())
    txt = Entry(win, width=23, textvariable=file_name)
    txt.grid(column=1, row=1, sticky='w')
    txt.focus()

    lbl_seed = Label(win, text='图像种子')
    lbl_seed.grid(column=0, row=3, sticky='w')
    var = IntVar()
    var.set(random.randint(0,10000000))
    spin = Spinbox(win, from_=0, to=10000000, width=21,textvariable=var)
    spin.grid(column=1, row=3, sticky='w')

    lbl_bar = Label(win, text='分辨率')
    lbl_bar.grid(column=0, row=4, sticky='w')
    var1 = IntVar()
    var1.set(1)
    spin1 = Spinbox(win, from_=0, to=10, width=21,textvariable=var1)
    spin1.grid(column=1, row=4, sticky='w')

    btn = Button(win, text='生成图片', command=lambda:[generate(spin,comb1,spin1,comb,txt)])
    btn.grid(column=1, row=6, sticky='w')

    win.mainloop()


if __name__ == '__main__':
    main()
```