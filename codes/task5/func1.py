from selenium import webdriver
import time
# 验证课程的展示序号是否正确，
# 序号小的课程名作为第一个参数，
# 序号大的课程名作为第二个参数
# 整个课程列表作为第三个参数
def comInx(cname1, cname2, cList):
    idx = 0
    for i in cList:
        if i == cname1:
            idx1 = idx
        elif i == cname2:
            idx2 = idx
        idx += 1

    if idx1 < idx2:
        return 'PASS'
    return 'FAIL'

#删除所有的课程
def deleteAllCourses():
    driver = webdriver.Chrome(r'c:\wyy\webdrivers\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://localhost/mgr/login/login.html')

    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('button[onclick*="postLoginRequest()"]').click()
    time.sleep(3)

    driver.implicitly_wait(1)
    while True:
        eles = driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
        if len(eles)==0:
            break
        eles[0].click()
        driver.find_element_by_css_selector('button.btn-primary').click()
        time.sleep(1)

    driver.quit()



