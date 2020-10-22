import time
from selenium import webdriver
from seleniumCookieInjection import cookieInjection

# 优化方案
# 1. 通过黑名单添加，避开外包公司
# 2. 通过关键词匹配率算法，优化决策准确率
# 3. 通过记录每个沟通过的人，记录在30分钟内回复的人，记录在30分钟内没有回复的人进行数据挖掘，回复率分析，用以优化回复率


def run(list, nowpage=0):
    if (nowpage > 1):
        nowpage = (nowpage - 1) * 29
    for x in range(0, len(list)):

        list[x].click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        driver.implicitly_wait(3)
        if (driver.find_element_by_class_name('btn-container').text == '立即沟通'):
            print("已投递人数", (nowpage + (x + 1)), "请及时给与别人回复")

            driver.find_element_by_class_name('btn-container').click()
            try:
                if (len(driver.find_element_by_class_name("dialog-container").text)<50):
                    raise Exception("到达人数上限")
            except Exception as err:
                if (err.__str__() == "到达人数上限"):
                    print("汪")
                    raise
        driver.close()
        driver.switch_to.window(handles[0])
        driver.implicitly_wait(3)


driver = webdriver.Chrome()
driver.maximize_window()
cookieInjection.loadingLocalCookie(driver,"https://www.zhipin.com/","D:\Python code\myobj\Boss.json")
url=input()
driver.get(url)

time.sleep(3)
run(driver.find_elements_by_class_name("job-primary"))

while (True):

    driver.find_element_by_class_name('next').click()
    run(driver.find_elements_by_class_name("job-primary"),eval(driver.find_element_by_class_name('page').find_element_by_class_name('cur').text))
    driver.implicitly_wait(3)


