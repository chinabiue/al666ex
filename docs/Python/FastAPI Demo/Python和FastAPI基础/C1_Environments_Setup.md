---
title: 第一章 环境设置 
date: 2024-04-06 22:19:42
categories: 
    - fastapi
---
FastAPI开发需要一些先决条件。环境设置是

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
$ python3 -m venv ~/.venv/demo
```
### 激活虚拟环境

```bash
$ source ~/.venv/demo/bin/activate
```

### 安装FastAPI需要的依赖

```bash
(demo) $ pip install -r requirements.txt
```
以下为requirements.txt文件内容
```txt
annotated-types==0.6.0
anyio==4.3.0
asttokens==2.4.1
bcrypt==4.1.2
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
decorator==5.1.1
dnspython==2.6.1
email-validator==2.1.0.post1
executing==2.0.1
fastapi==0.109.2
greenlet==3.0.3
h11==0.14.0
httpcore==1.0.4
httptools==0.6.1
httpx==0.27.0
idna==3.6
iniconfig==2.0.0
ipython==8.22.1
itsdangerous==2.1.2
jedi==0.19.1
Jinja2==3.1.3
joblib==1.3.2
MarkupSafe==2.1.5
matplotlib-inline==0.1.6
numpy==1.26.4
orjson==3.9.15
packaging==23.2
parso==0.8.3
passlib==1.7.4
pexpect==4.9.0
pluggy==1.4.0
prompt-toolkit==3.0.43
ptyprocess==0.7.0
pure-eval==0.2.2
pydantic==2.6.2
pydantic-extra-types==2.5.0
pydantic-settings==2.2.1
pydantic_core==2.16.3
Pygments==2.17.2
pytest==8.0.2
python-dotenv==1.0.1
python-multipart==0.0.9
PyYAML==6.0.1
requests==2.31.0
scikit-learn==1.4.1.post1
scipy==1.12.0
six==1.16.0
sniffio==1.3.0
SQLAlchemy==2.0.27
sqlmodel==0.0.16
stack-data==0.6.3
starlette==0.36.3
threadpoolctl==3.4.0
traitlets==5.14.1
typing_extensions==4.9.0
ujson==5.9.0
urllib3==2.2.1
uvicorn==0.27.1
uvloop==0.19.0
watchfiles==0.21.0
wcwidth==0.2.13
websockets==12.0
```

至此环境设置完毕。