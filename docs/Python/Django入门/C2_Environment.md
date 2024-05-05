---
title: 第二章 环境设置 
date: 2024-05-04 12:04:42
categories: 
    - django
---
Django开发需要一些先决条件。环境设置是

## WSL2 Debian on Windows 10
自行安装好WSL Debian或其他顺手的操作系统。
<!-- termynal -->
```
$ uname -a
Linux PC-20231120WDXG 5.15.146.1-microsoft-standard-WSL2 #1 SMP Thu Jan 11 04:09:03 UTC 2024 x86_64 GNU/Linux
```
## Python 设置

### Python虚拟环境设置
虚拟环境的好处是可以给每个项目指定依赖，互不干扰。

```bash
$ python3 --version
Python 3.11.2
```

```bash
$ python3 -m venv ~/.venv/django
```
### 激活虚拟环境

```bash
$ source ~/.venv/django/bin/activate
```

### 安装Django需要的依赖

```bash
(django) $ pip install -r requirements.txt
```
以下为requirements.txt文件内容
```txt
annotated-types==0.6.0
asgiref==3.8.1
Django==5.0.4
django-ninja==1.1.0
pydantic==2.7.1
pydantic_core==2.18.2
sqlparse==0.5.0
typing_extensions==4.11.0
```
### 需要用到命令行命令


``` {.yaml .annotate}
1) cd #(1)!
2) cd .. #(2)!
3) ls #(3)!
4) mkdir #(4)!
5) touch #(5)!

```

1. 切换到目录
2. 切换到上一级目录
3. 列出当前目录下的文件
4. 创建一个目录
5. 创建一个文件

### IDE
本示例IDE选择VSCode。


至此环境设置完毕。

