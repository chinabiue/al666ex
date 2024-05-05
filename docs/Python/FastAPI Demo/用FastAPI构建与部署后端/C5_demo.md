---
title: 第五章 FastAPI + sqlmodel Demo 
date: 2024-04-08 22:42:42
categories: 
    - fastapi
---
## 程序结构
一个典型的FastAPI程序结构如下：

```{ .python .annotate }
.
├── demo                #(1)!
│   ├── app.py          #(2)!
│   ├── database        #(4)!
│   │   ├── database.py
│   │   └── __init__.py
│   ├── database.db
│   ├── __init__.py     #(3)!
│   ├── models.py       #(5)!
│   └── routers         #(6)!
│       ├── heroes.py
│       ├── __init__.py
│       └── teams.py
```

1. 项目总目录，包含所有源代码文件。
2. FastAPI应用程序的入口点。
3. 包含应用程序的初始化代码的文件。一般为空，代表此文件夹可做为模块使用。
4. 包含数据库连接定义的文件夹。
5. 包含数据模型定义的文件。
6. 包含路由定义的文件夹。

## 定义模型
一般从模型定义开始整个项目。
本程序设计了一个英雄模型和一个队伍模型。参考SQLModel官方示例，定义如下：

!!! note "Circular import"

    因为circular import问题，所有模型定义在models.py文件中。暂时没有方法分开。
    对于模型多的项目，建议每个模型定义在单独的文件中。但是要解决circular import问题很麻烦。

```{ .python .annotate }
from sqlmodel import SQLModel, Field, Relationship


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str = Field(...)
    age: int | None = Field(default=None)
    team_id: int | None = Field(default=None, foreign_key="team.id")


class HeroCreate(HeroBase):
    pass


class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None


class HeroRead(HeroBase):
    id: int
    team: "Team"


class Hero(HeroBase, table=True):
    id: int = Field(default=None, primary_key=True)

    team: "Team" = Relationship(back_populates="heroes")


############TEAM###############
class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str = Field(...)


class TeamCreate(TeamBase):
    pass


class TeamUpdate(SQLModel):
    name: str | None = None
    headquarters: str | None = None


class TeamRead(TeamBase):
    id: int
    heroes: list["Hero"]


class Team(TeamBase, table=True):
    id: int = Field(default=None, primary_key=True)

    heroes: list["Hero"] = Relationship(back_populates="team")

```