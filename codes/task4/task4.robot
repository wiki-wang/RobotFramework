*** Settings ***
Library  course_mgr_web.py

*** Test Cases ***
用例4：检查添加课程功能
    [Setup]    run keywords    login Web    AND    delete all courses
    add course    Chinese    语文课程     2
    courseList should contain    Chinese

    add course    Maths    数学课程     1
    courseList should contain    Maths    Chinese
    [Teardown]    run keywords    delete all courses
                            ...    AND    close_broser
