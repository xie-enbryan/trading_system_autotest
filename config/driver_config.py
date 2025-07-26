# from webdriver_manager.chrome import ChromeDriverManager



from selenium import webdriver

from common.tools import get_project_path,sep
# from common.tools import get_project_path, sep

class DriverConfig:
    def drvier_config (self):
        """
        设置浏览器驱动
        """
        options = webdriver.ChromeOptions()
        # 设置窗口大小
        options.add_argument("window-size=1920, 1080")
        # 去掉“chrome”正受到自动软件测试的控制提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL的问题
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        # options.add_argument("--incognito")
        # 设置为无头模式
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # 重点：关闭保存密码弹窗
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })

        options.add_argument("--disable-features=PasswordManager,PasswordLeakDetection,AutofillServerCommunication")

        # 使用一个临时profile
        #options.add_argument("--user-data-dir=/tmp/selenium_profile")

        # 实例化一个driver对象
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver