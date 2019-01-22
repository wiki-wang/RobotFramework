*** Settings ***
Library  SeleniumLibrary
Library  func1.py
Resource  res.robot
Test Setup      deleteAllCourses
Test Teardown       deleteAllCourses


*** Test Cases ***
添加课程

# 登录
    login website       auto        sdfsdfsdf

# 创建课程
    create course   ruby    ruby课程      2

# 验证步骤1
    ${cname}        Get Text    css=tr>td:nth-child(2)
    should be true   $cname=='ruby'

# 再次添加课程
    create course   ruby2    ruby课程      1
    sleep       3

# 验证步骤2：第二门课程添加成功
    ${courseList}   get course list
    should be true   'ruby2' in $courseList

# 验证步骤2：验证次序
    ${status}       comInx    ruby2    ruby    ${courseList}
    should be true      $status=='PASS'

    close browser
