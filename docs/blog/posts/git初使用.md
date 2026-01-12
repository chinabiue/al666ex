---
title: git for Windows 初使用
---
## 1. 本地工作
- 新建分支create new branch
	```bash
	git branch <new branch name>
	```
- 切换到新分支switch to branch

	有人使用checkout,暂时不明白checkout是一个什么操作，不是特别直观，所以使用switch，命令很直观，就是切换到想要的分支。
	```bash
	git switch <branch name>
	```

- 把上面两个命令合二为一，新建并切换到新分支。create and switch to new branch
	```bash
	git switch -c <new branch name>
	```
<!-- more -->
- 删除分支delete branch
  	```bash
	git branch -d <branch name>
	```
- 提交更改3件套 commit 3 step。先确认状态，然后添加所有，最后提交。
  ```bash
	git status
	git add *
	git commit -m 'description of commit'
  ```
- 如果本地移动了文件夹，会出现很多红色deleted需要提交，不可能一个一个用`git cm`去提交的，用以下命令，一次提交所有更改：
  ```
  git add -A
  ```
## 2. 远程工作
- 在dev分支上开发的简单流程。不涉及多人提交，单人的话可以这样工作。
	- 先切换到master
	```bash
	git switch master
	```
	- 从master生成开发分支dev
	```bash
	git switch -c dev
	```
	- 在开发分支上做事，做完事提交完成后，切换回master分支。
	```bash
	git switch master
	```
	- 在master上合并dev分支
	```bash
	git merge dev
	```
	- 如果一切无误，可以删除dev本地分支了
	```bash
	git branch -d dev
	```
    - 删除远程分支
    ```bash
    git push origin --delete <branch_name>
    ```
	- 然后可推送至远程仓库
	```bash
	git push origin master
	```
---
## 3. 软件设置
- git 配置文件位于用户文件夹下,文件名为 *.gitconfig* 。内容
  ```
  [user]
	  name = Cris
	  email = Criswu@chaoyang.com
  [gui]
	  encoding = utf-8
  [alias]
	  st = status
	  br = branch
	  cm = "commit -m"
	  sw = switch
	  ad = "add -A"
	  co = checkout
	  hist = log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short
  ```
  alias字段就可以定义命令的别名，以便快速输入。

---
- 生成SSH Key
最方便的方法是打开Git GUI，然后Help - Show SSH Key。
也不用打什么命令，把生成的SSH key粘贴到需要推送的托管网站，就可以推送了。

- GitHub,因为它经常假死，断连。国内可用的有[Codeup](https://www.aliyun.com/product/yunxiao/codeup)\ [Gitee](https://gitee.com/)\ [Coding.net](https://coding.net/)\ [Azure](https://azure.microsoft.com/zh-cn/services/devops/repos/)， 除了码云，分别是各大头部提供的服务，暂且可用。

## 4. 设置多个远程仓库
配置软件上瘾的话，可以同时配置多个远程仓库。以下例子就同时配置了刚才提到的4个仓库。
### 4.0 克隆远程仓库至本地（作为主仓库，其他仓库的内容都以主仓库为主）
新建一个文件夹，在文件夹下打开git bash执行以下命令
```bash
git clone git@gitee.com:path/to/project.git
```
克隆下来的仓库自动会命名为origin，咱改了它。
```
git remote rename origin gitee
```

### 4.1 添加远程仓库
在需要添加仓库的服务商内设置好SSH，建立好项目(自行读文档设置，应该很容易），把项目地址都添加上。
```bash
git remote add codeup git@codeup.aliyun.com:path/to/project.git
git remote add tx git@e.coding.net:path/to/project.git
git remote add ms git@ssh.dev.azure.com:v3/path/to/project
```

第一次推送。因为本地文件夹已经有gitee克隆下来的项目文件，使用以下命令推送至各个代码库。
```bash
git push codeup main
git push tx main
git push ms main
```
至些，所有代码库内容一致。

### 4.2 同步细节的设置
要达到所有仓库内容一致，每次同步都需要打4条命令这是不可取的。

- 首先，要确定以哪个仓库为主仓库。确定本地内容与远程仓库内容一致，绑定一个默认的仓库即达到目的。
  
  只要使用以下命令一次，即可设置为默认仓库,命令意思为：推送本地内容至gitee(设置你想要的那一个远程仓库)的main分支并设定本地内容跟踪远程内容。
  ```bash
  git push -u gitee main
  ```
  所以以后推送，可以使用简单的推送/拉取命令，推送拉取的内容都会自动设定仓库为gitee，而不用指定仓库，指定分支。
  ```bash
  git pull
  git push
  ```

- 然后，在项目文件夹个新建以下push.sh文件
  
  ```sh
  echo  
  echo **************GITEE********************
  git push gitee main
  echo **************GITEE********************
  echo  
  echo **************CODEUP*******************
  git push codeup main
  echo **************CODEUP*******************
  echo  
  echo **************TENCENT******************
  git push tx main
  echo **************TENCENT******************
  echo  
  echo **************MICROSOFT****************
  git push ms main
  echo **************MICROSOFT****************
  echo  
  ```
  以后推送时在git bash执行以下命令运行运行push.sh文件
  ```
  ./push.sh
  ```
  会自动按顺序推送至设置好的4个仓库。即使忘了使用sh文件推送，使用了默认的`git push`也没有关系，默认会推送至gitee。当你想起来时，去执行一遍sh文件，所有仓库又同步了:)

!!! info "多读文档"
	把读文档当做一种乐趣。上手一个新东西最可靠的方法就是读文档。去网上搜索来的东西都是人家吃过以后再消化再拉出来的东西，大部分可用，需要去分辨。但是软件或库本身的文档，确是第一引用源，官方第一手且很大概率上完全没有错。
