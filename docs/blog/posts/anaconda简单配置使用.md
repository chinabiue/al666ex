---
title: anaconda简单配置使用
tags: python
categories: [coding]
authors:
    - Alex
date: 2022-08-09 10:13:09
---

!!! info ""

    Anacoda是Python的一个集合包，主要用于数据处理与机器学习。
    它集成了众多你需要的包，可以方便的对包进行管理。
    可以减少安装配置新包的时间。如果喜欢可以使用；如果不喜欢就不要使用，可以直接安装python包，通过pip安装新包。

## 1. Anaconda和miniconda的选择

### 1.1 如果符合以下条件，请选择Anaconda:🐍
- conda或Python新手
- 倾向于方便性，一次性自动安装配置好Python和超过1500个科学包
- 有点悠闲时间和磁盘空间 - 十几分钟和最少3GB（本人3个虚拟环境，17G）
- 不想麻烦每次手动安装需要的包
- 希望使用官方审查过操作性与可用性的包

### 1.2 如果符合以下条件，请选择miniconda:
- 不介意每次手动安装需要的包
- 没有时间与空间一次安装完所有的包
- 想快速上手使用Python和conda，喜欢自己定制软件的过程

<!-- more -->
## 2.换miniconda源
* 打开CMD执行命令，生成用户目录下的conda配置文件`.condarc`
```
conda config --set show_channel_urls yes
```
* 打开文件编辑。以下是一个使用中的文件内容。
```
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
ssl_verify: true
```

* 清除索引

```
conda clean -i
```

* 更新

```bash
conda update conda
conda update --all
```

* 给虚拟环境env安装新包，使用`conda install -n [env] [package_name]`,比如给虚拟环境vsc安装 ipython   

```bash
conda install -n vsc ipython
```

## 3. 使用
创建新环境
```bash
conda create -n [你的名字]
```

!!! warning "安装miniconda后CMD闪退/无法运行解决办法"
    删除注册表 
    HKEY_CURRENT_USER\Software\Microsoft\Command Processor\AutoRun 的值**if exit**
