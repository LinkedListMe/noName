import json

class cookieInjection:
    @classmethod
    def loadingLocalCookie(self, driver, Internet, cookiePath):
        """
        
        @param driver:
        @param Internet: 需要注入的网址
        @param cookiePath: Json文件在本地的地址
        """
        driver.get(Internet)
        driver.delete_all_cookies()
        with open(cookiePath, "r") as f:
            jsonCookies = json.loads(f.read())

        for cookie in jsonCookies:
            driver.add_cookie({
                'domain': cookie['domain'],
                'httpOnly': cookie['httpOnly'],
                'name': cookie['name'],
                'path': cookie['path'],
                'secure': cookie['secure'],
                'value': cookie['value']
            })
        driver.refresh()

    @classmethod
    def downloadCookies(self, driver, localPath):  # 下载Cookie到本地
        """
        @param driver:
        @param localPath: 将浏览器的cookies缓存到本地的一个文件中去
        """
        with open(localPath+'.json', "w") as f:
            print()
            f.write(json.dumps(driver.get_cookies()))
