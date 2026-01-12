---
title: cairosvg安装配置与批量转换svg to png
---

Gitee这几天发现个问题，文章里引用的SVG图片全部解析不出来。不好看不舒服。需要把SVG图片全转换成PNG图片再上传。发现cairosvg可以做这个事，安装配置不是那么简单。

### 1. 安装cairosvg
conda里默认的channel里并没有cairosvg，后面发现conda-forge里有。

```shell
conda config --add channels conda-forge     # 添加conda-forge源
conda install cairosvg                      # 安装主包
conda install cairo                         # 安装库
```
### 2. 安装[DLL依赖](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2021-01-30/gtk2-runtime-2.24.33-2021-01-30-ts-win64.exe)

### 3. 程序细节
程序很简单了，就是进入文件夹，迭代。把文件放入SVG文件夹同目录下，运行就OK了。
```python
import cairosvg
from pathlib import Path


def Svg2Png():
    SrcDir = Path('.').resolve()
    SvgList = [svg for svg in SrcDir.iterdir() if svg.suffix == ".svg"]
    for svgFile in SvgList:
        pngFile = svgFile.with_suffix(".png")
        if not pngFile.is_file():
            cairosvg.svg2png(url=str(svgFile), write_to=str(pngFile), scale=3)


Svg2Png()
```

### 4. 批量替换文件后缀
post里搜索替换所有`.svg`为`.png`。