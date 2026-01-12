---
title: Windows 10 使用VIM写python的基本设置
---
尽可能的少安装插件，使用原生vim的功能进行python小程序的方便编写。
如果不需要自动完成括号，只需要安装一个插件:jedi-vim用于函数提示就可以了。
自动完成括号应该也可以使用vim script完成，但是，没那功夫，有功夫直接使用vscode更好。

### 0.预备工作
确保

* python 可以在CMD顺利运行
* python 是64位

!!! warning

    安装文件是32或64位应该很重要。至少我使用32位VIM配合64位Python是不成功的。别折腾。


### 1. 安装VIM

#### 1.1 下载VIM
可以使用choco安装。
另一选择是下载64位VIM，请直接去[Github](https://github.com/vim/vim-win32-installer/releases/) 界面下载最新的[Nightly版本](https://github.com/vim/vim-win32-installer/releases/download/v9.0.0292/gvim_9.0.0292_x64.exe) 。<-这是我下载的版本
不去[官网下载](https://www.vim.org/download.php) 的原因是：因为windows版本不是主要维护对象，上官网直接给你推一个32和64位通用的版本，下载安装以后会遇到很多困难，出了问题并没有什么信息可以参考。
#### 1.2 安装
点击安装，除了选择完全安装以外，全部都是默认设置，安装完成。安装完成，走一遍vimtutor，确保自己能在先期存活下来再干别的事。

### 2. 配置VIM

#### 2.0 复制配置文件
进入VIM安装目录，把`_vimrc`文件复制一份到当前用户文件夹下面。这个文件就是所有配置的基础。

#### 2.1 更改配色
默认白色背景太刺眼，先上来使用一个深色的背景再进行其他操作。打开刚才的`_vimrc`文件，假设已经能在VIM里自由的编辑了。在文件最后一行，空一行，输入以下语句：
```vim
colorscheme desert
```
本条语句使用内置的`desert`配色，基本上可以接受这配色再干活。需要更改后面可以设置自己喜欢的配色。
<!-- more -->
#### 2.2 使用按键组合`jk`代替`ESC`退出键/映射跳出括号快捷方式方便编辑
ESC在左上方不是很好按，打开刚才的`_vimrc`文件，在最后一行空一行，输入以下语句：
```py
" 映射ESC键到'jk'
inoremap jk <ESC>
inoremap JK <ESC>

" 映射dd到跳出括号
inoremap DD <C-\><C-n>:call search('[>)\]}"'']', 'W')<CR>a
inoremap dd <C-\><C-n>:call search('[>)\]}"'']', 'W')<CR>a

```

#### 2.3 配置python功能
在VIM输入 `:python3 import this`，基本上可以肯定的是会得到如下图提示错误：
![error py3](https://gitee.com/al666ex/RhinoPython101/raw/master/images/giteepages/VIM_PYTHON3.PNG)
因为没有配置好python功能，
```
let &pythonthreedll='D:\miniconda3\envs\vsc\python310.dll'
let &pythonthreehome='D:\miniconda3\envs\vsc'
```
在 \_vimrc 输入以上设置，注意指向你安装版本的dll文件，python3.9就和我一样，python3.10就是python310.dll。配置成功后就正确的在VIM输出了python之蚕：
![天蚕](https://gitee.com/al666ex/RhinoPython101/raw/master/images/giteepages/VIM_PYTHON_OK.PNG)

#### 2.4 配置写程序基本功能
以下几行配置分别管理语法高亮、TAB键缩进、，请写在`_vimrc`最后。
```
" python coding
set nu
syntax on
set tabstop=4
set expandtab
set shiftwidth=4
```
在写程序的过程中，可以按CTRL+N/CTRL+P选择出现在文件里的自定义变量。到这里基本上可以实现写程序了。还差最后2点：自动提示和运行程序。
写好程序可以使用`:!python t.py`验证一下功能是否正常，请把t.py换成你写的程序名。

#### 2.5 安装插件管理器vim-plug并安装自动完成插件jedi-vim
下载[vim-plug文件](https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim) ,放入用户文件夹的`vimfiles`下的`autoload`文件夹，如果没有就新建一个。

然后在`_vimrc`文件最后加入如下配置
```
call plug#begin()
Plug 'davidhalter/jedi-vim'
Plug 'jiangmiao/auto-pairs'
call plug#end()
```
保存退出重新进入VIM，输入以下命令启动插件安装：
```
:PlugInstall
```

配置一下使用TAB键呼出补全
```
let g:jedi#completions_command = "<TAB>"
```

最后写一个程序试试，一切基本OK。
![]()

#### 2.6 设置格式化/一键运行python
使用black自动格式化代码，如果没用，请在CMD运行`pip install black`
```py
" auto-format with black
" 设置空格作为<leader>健
let mapleader=" "  
map <leader>i :call Format()<CR>
func! Format()
    exec "w"
    if &filetype == 'python'
        exec "silent !python -m black -q -v %"
    endif
    exec "w"
endfunc
set autoread 
```

一键在vim内打开CMD并运行
```py
" one key run
map <leader>e :call Runp()<CR>
func! Runp()
    exec "w"
    if &filetype == 'python'
        exec "!python -i %"
    endif
endfunc
```

### 3.最终文件
```PY
"选择颜色主题
colorscheme desert
set guifont=Consolas:h13:cANSI:qDRAFT
set autoread 

" 映射ESC键到'jk'
inoremap jk <ESC>
inoremap JK <ESC>

" 映射dd到跳出括号
inoremap DD <C-\><C-n>:call search('[>)\]}"'']', 'W')<CR>a
inoremap dd <C-\><C-n>:call search('[>)\]}"'']', 'W')<CR>a

"python编程设置
set nu
syntax on
set tabstop=4
set expandtab
set shiftwidth=4

let &pythonthreedll='D:\miniconda3\envs\vsc\python310.dll'
let &pythonthreehome='D:\miniconda3\envs\vsc'

" jede自动补全呼出
let g:jedi#completions_command = "<TAB>"

call plug#begin()
Plug 'davidhalter/jedi-vim'
Plug 'jiangmiao/auto-pairs'
"Plug 'ervandew/supertab'
"Plug 'iamcco/markdown-preview.vim'
"Plug 'vim-airline/vim-airline'
call plug#end()

let g:AutoPairsMapBS = 0

" 自动格式化并保存
let mapleader=" "  
map <leader>i :call Format()<CR>

func! Format()
    exec "w"
    if &filetype == 'python'
        exec "silent !python -m black -q -v %"
    endif
    exec "w"
endfunc    

" 运行程序快捷方式
map <leader>e :call Runp()<CR>
func! Runp()
    exec "w"
    if &filetype == 'python'
        exec "!ipython -i %"
    endif
endfunc

```