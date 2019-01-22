*** Settings ***
Library  course_mgr_web.py

*** Test Cases ***
用例3：验证当系统中没有课程的时候，是否能成功添加一个课程
    [Setup]    run keywords    login Web    AND    delete all courses
    add course    Chinese    语文课程     1
    courseList should contain    Chinese
    [Teardown]    run keywords    delete all courses
                            ...    AND    close_broser