from playwright.sync_api import sync_playwright
import time

# 请输入你的用户名/密码/及gitee pages网址
USERNAME = 'ccccc42@google.com'
PASSWORD = '31415926pi'
GITEE_PAGES_URL = 'https://gitee.com/your/repo/pages'


def main():
    with sync_playwright() as p:
        for browser_type in [p.chromium]:
            browser = browser_type.launch(headless=False)
            page = browser.new_page()
            page.goto('https://gitee.com/login')
            page.click('input[name="user[login]"]')
            page.fill('input[name="user[login]"]', USERNAME)
            page.click('input[name="user[login]"]')
            page.fill('input[name="user[password]"]', PASSWORD)
            page.click("input[value='登 录']")
            time.sleep(3)
            page.goto(GITEE_PAGES_URL)
            page.on("dialog", lambda dialog: dialog.accept())
            page.click(".update_deploy")
            page.on("dialog", lambda dialog: dialog.accept())
            # text = "已开启 Gitee Pages 服务，网站地址："
            # state="attached", "detached", "hidden", "visible"
            # page.wait_for_selector('span:text("正在部署，请耐心等待...")', timeout=12 * 1000, state='hidden')
            time.sleep(7)
            page.wait_for_selector(
                'span:text("正在部署，请耐心等待...")',
                timeout=10 * 1000,
                state='hidden',
            )
            print('OK')
            browser.close()


if __name__ == '__main__':
    main()
