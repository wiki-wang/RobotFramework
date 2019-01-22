from selenium import webdriver
import time

class course_mgr_web:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.driver = None

    def login_Web(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/mgr/login/login.html')
        self.driver.find_element_by_id('username').send_keys('auto')
        self.driver.find_element_by_id('password').send_keys('sdfsdfsdf')
        self.driver.find_element_by_css_selector('button[onclick = "postLoginRequest()"]').click()


    def delete_all_courses(self):
        self.driver.find_element_by_css_selector('a[ui-sref="course"]').click()
        time.sleep(2)
        self.driver.implicitly_wait(2)
        while True:
            eles = self.driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
            if not eles:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector('button[class ="btn btn-primary"]').click()
            if len(eles) == 1:   #只剩一个删除按钮时，直接退出循环
                break
            time.sleep(2)
        self.driver.implicitly_wait(10)

    def add_course(self,name,desc,idx):
        self.driver.find_element_by_css_selector('a[ui-sref="course"]').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('input[ng-model="addData.name"]').clear()
        self.driver.find_element_by_css_selector('input[ng-model="addData.name"]').send_keys(name)

        self.driver.find_element_by_css_selector('textarea[ng-model="addData.desc"]').clear()
        self.driver.find_element_by_css_selector('textarea[ng-model="addData.desc"]').send_keys(desc)

        self.driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]').send_keys(idx)

        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()




    def courseList_should_contain(self, *names):
        self.driver.find_element_by_css_selector('a[ui-sref="course"]').click()
        time.sleep(2)
        eles = self.driver.find_elements_by_css_selector('tbody>tr>td:nth-child(2)>span')
        courseNames = [ele.text for ele in eles]
        assert list(names) == courseNames, '{} != {}'.format(list(names),courseNames)


    def close_broser(self):
        self.driver.quit()





# if __name__ == '__main__':
#     course_mgr = course_mgr_web()
#     course_mgr.login_Web()
#     course_mgr.delete_all_courses()
#     course_mgr.add_course('Chinese','语文','1')
#     course_mgr.courseList_should_contain('Chinese')
#     course_mgr.close_broser()


