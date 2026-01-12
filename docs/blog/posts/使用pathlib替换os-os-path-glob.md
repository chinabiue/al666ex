---
title: 使用pathlib替换os/os.path/glob
---
!!! tip "总结"
    从Python3.6开始，pathlib.Path 对象几乎可以在任何已经使用路径字符串的地方工作。因此，如果你使用的是Python3.6（或更高版本），我认为没有理由不使用 pathlib。

    pathlib可以把以前比较繁复的路径工作处理得更简洁一点，请好好使用。


如果需要操作路径，在python3.6以前会经常使用os模块(mkdir、getcwd、chmod、stat、remove、rename 、rmdir、 chdir......)。现在比较推荐使用pathlib。pathlib模块用 path 对象上的方法替换了许多这些与文件系统相关的 os功能。

以下分段展示两个代码的不同实现方式，可以看出pathlib更简洁高效。
## 1. 新建文件夹与重命名
=== "原来方式：os.makedirs"
    ```python
    import os
    import os.path

    #创建了first/second目录
    os.makedirs(os.path.join('first', 'sencond'), exist_ok=True)
    #将 sau.txt 文件重命名为 first/sau.txt.bak,并移到first目录下
    os.rename('sau.txt', os.path.join('first', 'sau.txt.bak'))
    ```
=== "Path.mkdir 新建文件夹"
    使用 Path 对象执行相同的操作，由于采用链式调用的方法，pathlib 代码将路径放在第一位。
    ```python
    from pathlib import Path

    Path('first/second').mkdir(parents=True, exist_ok=True)
    ```
=== "Path.rename的当移动文件使用"
    前提是移动目的地的文件结构要已经存在，rename不会给你在移动过程中新建文件结构。

    ```python
    from pathlib import Path

    Path('sau.txt').rename('src/sau.txt.bak')
    ```
<!-- more -->
## 2. 匹配特定模式 
=== "老方式"
    ```python
    from glob import glob
    #找出所有后缀名为.csv的文件
    top_level_csv_files = glob('*.csv')
    all_csv_files = glob('**/*.csv', recursive=True)
    ```
=== "新方式： pathlib 模块同样包括类似 glob 的功能。通过对Path对象的操作，已经不再需要导入glob模块了。"
    ```python
    from pathlib import Path

    top_level_csv_files = Path.cwd().glob('*.csv')
    all_csv_files = Path.cwd().rglob('*.csv')
    ```

## 3. 读取文件夹里所有文本
=== "老式for循环"
    ```python
    from glob import glob

    file_contents = []
    #读取一个或多个文件夹内所有py文本内容
    for filename in glob('**/*.py', recursive=True):
        with open(filename) as python_file:
            file_contents.append(python_file.read())
    ```

=== "用 Path 对象的 read_text 方法配合列表推导式，一行代码解决问题："
    ```python
    from pathlib import Path

    file_contents = [
        path.read_text()
        for path in Path.cwd().rglob('*.py')
    ]
    ```

## 4. 写入文本
```python
#使用 open 上下文管理器写入文件
with open('.editorconfig', 'w') as config:
    config.write('# config goes here')
```

### 4.1 使用 Path 对象的 write_text 方法：
```python
Path('.editorconfig').write_text('# config goes here')
```

### 4.2 在 Path 对象上也可以使用 open 方法：
```python
from pathlib import Path

path = Path('.editorconfig')
with path.open(mode='wt') as config:
    config.write('# config goes here')
```
### 4.3 从 Python3.6 开始，可以将 Path 对象直接传递给内置的 open 函数：
在Python3.6以后，可以直接将Path 对象传递给内置的open函数、os、shutil 和 os.path 模块中的各种函数。
```python
from pathlib import Path

path = Path('.editorconfig')
with open(path, mode='wt') as config:
    config.write('# config goes here')
```

## 5. pathlib 缺失的几个功能

### 5.1 复制文件
如果需要复制文件，仍然需要使用shutil模块。
```python
from pathlib import Path
from shutil import copyfile

source = Path('old_file.txt')
destination = Path('new_file.txt')
copyfile(source, destination)
```
### 5.2 更改工作目录
如果程序依赖Path.cwd()函数的返回值切换工作目录，没有与 os.chdir 等效的 pathlib 功能。
如果需要更改当前工作目录，仍需要导入os模块：
```python
from pathlib import Path
from os

parent = Path('..')
os.chdir(parent)
```
### 5.3 os.walk

没有与 os.walk 函数等价的 pathlib 函数。碰到这种情况，只能现撸一个递归函数。
```python
from pathlib import Path

def walk(drkst):
''' dst为目标文件夹地址，Path对象'''
    all_address = [x for x in dst.iterdir()]
    file_names = [x for x in all_address if x.is_file()]
    folder_names = [x for x in all_address if x.is_dir()]

    if folder_names:
        for folder in folder_names:
            file_names += walk(folder)
    return file_names
```
## 6. 操作示例
- Pathlib解压文件夹下所有ZIP文件至指定文件夹
  
```{.python .annotate}
import zipfile as zf
from pathlib import Path
    '''迭代所有ZIP文件'''
def unzip():
    for file in Path('.').glob('*.zip'):
        order = str(file.stem)[:4]
        if not Path(order).is_dir():  #(1)!
            Path.mkdir(Path(order))
        else:
            pass
        with zf.ZipFile(file) as f:  #(2)!
            f.extractall(order)
```

1. 生成文件夹
2. 解压

<br>

- 列表生成式生成文件夹下所有文件夹/文件地址
  
```{.python .annotate}
def all_files_path(workpath):
    '''获取目标文件夹下所有子文件夹下文件内容列表，并且返回该列表'''
    sum_file_list = [] 
    forlder_list = [i for i in workpath.iterdir() if i.is_dir()]  #(1)!
    for folder in forlder_list:
        files_list = [file for file in folder.iterdir() if file.is_file()]  #(2)!
        sum_file_list.append(files_list)
    return sum_file_list
```

1. 目标文件夹下所有文件夹的列表.生成式
2. 每个文件夹下文件列表.生成式

<br>

- 获取文件名各部分
获取文件名(文件.以前的部分)

```python
file = Path('apple.py')
file.stem           # 'apple'
file.suffix         # '.py'
```
