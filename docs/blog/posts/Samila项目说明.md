---
title: Samila项目说明
tags: python
categories: [coding]
authors:
    - Alex
date: 2022-01-12 21:38:20
---
<img src="https://cdn.jsdelivr.net/gh/chinabiue/img@latest/giteepages/logo.png" width=400 height=400>

# Samila
<!-- 
<div align="center">
<img src="https://gitee.com/al666ex/samila/raw/master/otherfiles/logo.png" width=400 height=400>
<br/>
<h1>Samila</h1>
 <br/>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://codecov.io/gh/sepandhaghighi/samila">
  <img src="https://codecov.io/gh/sepandhaghighi/samila/branch/master/graph/badge.svg" />
</a>
<a href="https://badge.fury.io/py/samila"><img src="https://badge.fury.io/py/samila.svg" alt="PyPI version" height="18"></a>
<a href="https://discord.com/invite/94bz5QGZWb">
  <img src="https://img.shields.io/discord/900055829225562162.svg" alt="Discord Channel">
</a> 
</div> 
-->
----------
## 目录		
| 1                                                                         | 2                                                                                           | 3                                                                             |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [概述](https://github.com/sepandhaghighi/samila#overview)                 | [问题 & Bug上报](https://github.com/sepandhaghighi/samila#issues--bug-reports)              | [参考](https://github.com/sepandhaghighi/samila#references)                   |
| [安装](https://github.com/sepandhaghighi/samila#installation)             | [依赖](https://github.com/sepandhaghighi/samila#dependencies)                               | [更改日志](https://github.com/sepandhaghighi/samila/blob/master/CHANGELOG.md) | [作者](https://github.com/sepandhaghighi/samila/blob/master/AUTHORS.md) |
| [使用](https://github.com/sepandhaghighi/samila#usage)                    | [贡献](https://github.com/sepandhaghighi/samila/blob/master/.github/CONTRIBUTING.md)        | [许可](https://github.com/sepandhaghighi/samila/blob/master/LICENSE)          |
| [数学细节](https://github.com/sepandhaghighi/samila#mathematical-details) | [行为准则](https://github.com/sepandhaghighi/samila/blob/master/.github/CODE_OF_CONDUCT.md) | [支持](https://github.com/sepandhaghighi/samila#show-your-support)            |

## 概述

<p align="justify">	
Samila是一个使用python语言的生成艺术生成器，通过数千个点你可以生成自己的艺术品。每一个单点的位置都通过带随机参数的公式确定。因为随机数的存在，每一张生成的图片看起来都不一样。
</p>


<!-- <table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/samila"><img src="https://www.openhub.net/p/samila/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/samila"><img src="http://pepy.tech/badge/samila"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/samila"><img src="https://img.shields.io/github/stars/sepandhaghighi/samila.svg?style=social&label=Stars"></a></td>
	</tr>
</table> -->



<!-- <table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
    <tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/samila/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/samila/workflows/CI/badge.svg?branch=dev"></td>
	</tr>
</table> -->


<!-- <table>
	<tr> 
		<td align="center">Code Quality</td>
		<td><a href="https://www.codacy.com/gh/sepandhaghighi/samila/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/samila&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/14df8ed5f8434aaea85889555b0182a9"/></a></td>
		<td><a href="https://codebeat.co/projects/github-com-sepandhaghighi-samila-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/01e6aa48-4cc2-4d9c-8288-c9fb490ad371" /></a></td>
		<td><a href="https://www.codefactor.io/repository/github/sepandhaghighi/samila"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/samila/badge" alt="CodeFactor" /></a></td>
	</tr>
</table> -->


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

$$S_1 = \{(x,y)\}| - \pi < x < \pi, -\pi < y < \pi$$

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


## 依赖

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/samila/requirements/?branch=master"><img src="https://requires.io/github/sepandhaghighi/samila/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/samila/requirements/?branch=dev"><img src="https://requires.io/github/sepandhaghighi/samila/requirements.svg?branch=dev" alt="Requirements Status" /></a></td>
	</tr>
</table>


## 参考			

<blockquote>1- Schönlieb, Carola-Bibiane, and Franz Schubert. "Random simulations for generative art construction–some examples." Journal of Mathematics and the Arts 7.1 (2013): 29-39.</blockquote>

<blockquote>2- <a href="https://github.com/cutterkom/generativeart">Create Generative Art with R</a></blockquote>

<blockquote>3- <a href="https://nft.storage/">NFT.storage : Free decentralized storage and bandwidth for NFTs</a></blockquote>
	

## 支持

<h3>给我们星标</h3>

如果觉得这个项目有帮助到你请给个 ⭐️ !

<h3>捐助项目</h3>	

真心希望你能喜欢我们的项目，能提供点支持吗？我们的项目不是也不会以赢利为目标。我们需要钱以继续维护这个项目;-) 。			

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>