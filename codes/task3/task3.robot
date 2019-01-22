*** Settings ***
Library  course_mgr.py
Library  SeleniumLibrary    implicit_wait=10

*** Test Cases ***
用例1
    ${cList}    listCourse      1
    :FOR    ${one}     IN     @{cList}
     \       log to console     \n${one}
     should be true     $cList==['c','c++']     课程不等于['c','c++']


*** Test Cases ***
用例2
    #列出华为商城所有热销商品的名称

    open browser        https://www.vmall.com/index.html        chrome
    ${getText}=                  Get Text                css=div[class='span-968 fl']>ul[class='grid-list clearfix']
#    Should Contain                ${firstRet}             2018
    log to console      ${getText}
    close browser


*** Test Cases ***
用例3：验证当系统中没有课程的时候，是否能成功添加一个课程
      [Setup]     deleteAllLessons
                ${newID}       addCourse       python    python    2       1
                ${newCourse}    listCourse      3
                should be true    $newCourse==[{'desc': 'python', 'display_idx': 2, 'id': $newID, 'name': 'python'}]

      [Teardown]     deleteAllLessons
