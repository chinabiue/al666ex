---
title: 自动更新 Gitee Pages
---
[原文地址](https://kaffa.im/update-gitee-pages-with-playwright.html)
!!! info

    2024.03.10 测试仍然可用。如果不喜欢浏览器弹出，请把13行(headless=False)设置为True。


直接copy运行了一下，没有效果。
根据运行电脑的做了以下设置，达到可运行的状态：运行程序达到自动点击gitee pages更新.

> 在命令行安装playwright以及浏览器

```bash
pip install playwright 
playwright install
```

> 更新了导入playwright的方式`from playwright.sync_api import sync_playwright`
<!-- more -->
page.wait_for_selector() 这一句始终没有找到一个好的条件来结束程序。

=== "**Tips One**"
    如果使用

    `page.wait_for_selector('span:text("已开启 Gitee Pages 服务，网站地址：")', timeout=12 * 1000, state='visible')`
    这一句span一开始就有了，在点击更新后会立即结束程序，看不到部署成功的提示。原则上可行但是并不完美。
=== "**Tips Two**"
    点击更新后会出现一条文本 *`正在部署，请耐心等待...`*，用它的消失来做为wait_for_selector()的条件，算是比较完美，它在部署成功后会消失，然后结束整个程序。
    
    但是程序也是一闪而过结束了，唯一确定的是更新按钮肯定点下去了。

    部署等几秒钟就成功了。


```Python hl_lines="5 6 7 30" linenums="1"
{! assets/py/gitee.py !}
```

!!! warning "Update"

    2024.05.01 在国际劳动节这天，所有gitee pages访问下线。

转至Cloudflare部署，不需要自己再写程序自动部署至gitee。

直接推送至github, 然后由Cloudflare自动部署至xxx.pages.dev。比以前更方便了。

部署很简单，参考[Cloudflare Pages](https://pages.cloudflare.com/)。