---
title: Samila项目说明
---
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/logo.png" width=400 height=400>

# Samila
----------
## 目录		
- [概述](https://github.com/sepandhaghighi/samila#overview)
- [安装](https://github.com/sepandhaghighi/samila#installation)            
- [使用](https://github.com/sepandhaghighi/samila#usage)                  
- [数学细节](https://github.com/sepandhaghighi/samila#mathematical-details) 
- [问题 & Bug上报](https://github.com/sepandhaghighi/samila#issues--bug-reports)              
- [作者](https://github.com/sepandhaghighi/samila/blob/master/AUTHORS.md)
- [贡献](https://github.com/sepandhaghighi/samila/blob/master/.github/CONTRIBUTING.md)       
- [参考](https://github.com/sepandhaghighi/samila#references)                   
- [许可](https://github.com/sepandhaghighi/samila/blob/master/LICENSE)         
- [支持](https://github.com/sepandhaghighi/samila#show-your-support)            
- [更改日志](https://github.com/sepandhaghighi/samila/blob/master/CHANGELOG.md) 
- [行为准则](https://github.com/sepandhaghighi/samila/blob/master/.github/CODE_OF_CONDUCT.md) 

## 概述

<p align="justify">	
Samila是一个使用python语言的生成艺术生成器，通过数千个点你可以生成自己的艺术品。每一个单点的位置都通过带随机参数的公式确定。因为随机数的存在，每一张生成的图片看起来都不一样。
</p>

<!-- more -->
## 安装		


### 源码
- 下载 [版本 0.3](https://github.com/sepandhaghighi/samila/archive/v0.3.zip) 或者 [最新源码 ](https://github.com/sepandhaghighi/samila/archive/dev.zip)
- 运行 `pip install -r requirements.txt` 或 `pip3 install -r requirements.txt` (需要管理员权限)
- 运行 `python3 setup.py install`或`python setup.py install` (需要管理员权限)				

### PyPI
- 查看 [Python包用户指南](https://packaging.python.org/installing/)     
- 运行 `pip install samila==0.3`或`pip3 install samila==0.3` (需要管理员权限)

### Easy install

- 运行 `easy_install --upgrade samila` (需要管理员权限)


## 使用

### 基本使用方法
```py
>>> import random
>>> import math
>>> import matplotlib.pyplot as plt
>>> from samila import GenerativeImage
>>> def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot()
>>> g.seed
188781
>>> plt.show()
```
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/1.png">	

### 投影
```py
>>> from samila import Projection
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot(projection=Projection.POLAR)
>>> g.seed
829730
>>> plt.show()
```
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/2.png">	

* 支持的投影方法 : `RECTILINEAR`, `POLAR`, `AITOFF`, `HAMMER`, `LAMBERT`， `MOLLWEIDE`
* 默认投影为 `RECTILINEAR`

### 范围
```py
>>> g = GenerativeImage(f1,f2)
>>> g.generate(start = -2*math.pi,step=0.1,stop=0)
>>> g.plot()
>>> g.seed
234752
>>> plt.show()
```
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/3.png">	

### 颜色
```py
>>> g = GenerativeImage(f1,f2)
>>> g.generate()
>>> g.plot(color="yellow",bgcolor="black",projection=Projection.POLAR)
>>> g.seed
1018273
>>> plt.show()
```
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/4.png">	

* 支持颜色请查看 `VALID_COLORS` 列表
* `color` 和 `bgcolor` 参数支持`VALID_COLORS` 列表内的颜色名和RGB/RGBA格式

### 重复生成
```py
>>> g = GenerativeImage(f1,f2)
>>> g.generate(seed=1018273)
>>> g.plot(projection=Projection.POLAR)
>>> plt.show()
```
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/5.png">	

### NFT.storage
把生成图片直接上传至 [NFT.storage](https://NFT.storage)

```py
>>> g.nft_storage(api_key = YOUR_API_KEY)
{'status': True, 'message': 'Everything seems good'}
```

### 保存图片
保存生成图片

```py
>>> g.save_image(file_adr="test.png")
{'status': True, 'message': 'Everything seems good'}
```
保存高清图片

```py
>>> g.save_image(file_adr="test.png", depth=5)
{'status': True, 'message': 'Everything seems good'}
```

### 保存数据
保存生成图像数据

```py
>>> g.save_data(file_adr="test.json")
```
随后可以通过以下代码加载至`GenerativeImage`实例：

```py
>>> g = GenerativeImage(data=open('test.json', 'r'))
```

## 数学细节
Samila的原理很简单，只是对一个方形空间进行从笛卡尔坐标系到其他专用坐标系（比如[极坐标](https://en.wikipedia.org/wiki/Polar_coordinate_system)）的转换操作。

### 例
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/transformation.png">

比如在左边的方块，我们有一组符合以下定义的点：

$$S_1 = \{(x,y)| - \pi < x < \pi, -\pi < y < \pi \}$$

以下两个函数用于转换：
```py
>>> def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
```
$$ S_2 = \lbrace (f_1(x,y), f_2(x,y))|(x,y) \in S_1\rbrace $$

这里传入参数为极坐标 `Projection.POLAR` ，所以最后我们得到极坐标空间图:

```py
>>> g = GenerativeImage(f1,f2)
>>> g.generate(seed=10)
>>> g.plot(projection=Projection.POLAR)
```
$$ S_2' = \lbrace (r, \theta) = (Z * x^2 - \sin(y^2) + |y-x|, Z * y^3 - \cos(x^2) + 2x) | (x,y) \in S_1, Z \sim U(-1,1) \rbrace $$

<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/6.png">

## 问题 & Bug上报			

请直接写issue并详细描述。我们会尽快检查！

- 请参照issue模板完成提交
 
你也可以加入我们的discord频道：

<a href="https://discord.com/invite/94bz5QGZWb">
  <img src="https://img.shields.io/discord/900055829225562162.svg?style=for-the-badge" alt="Discord Channel">
</a>


## 参考			

<blockquote>1- Schönlieb, Carola-Bibiane, and Franz Schubert. "Random simulations for generative art construction–some examples." Journal of Mathematics and the Arts 7.1 (2013): 29-39.</blockquote>

<blockquote>2- <a href="https://github.com/cutterkom/generativeart">Create Generative Art with R</a></blockquote>

<blockquote>3- <a href="https://nft.storage/">NFT.storage : Free decentralized storage and bandwidth for NFTs</a></blockquote>
	

## 支持

<h3>给我们星标</h3>

如果觉得这个项目有帮助到你请给个 ⭐️ !

<h3>捐助项目</h3>	

真心希望你能喜欢我们的项目，能提供点支持吗？我们的项目不是也不会以赢利为目标。我们需要钱以继续维护这个项目;-) 。			