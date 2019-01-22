*** Settings ***
Library  SeleniumLibrary        implicit_wait=10


*** Test Cases ***
百度搜索松勤
    Open Browser                  http://www.baidu.com    chrome
    Set Selenium Implicit Wait    5
    Input Text                    id=kw                   松勤\n
    ${firstRet}=                  Get Text                id=1
    Should Contain                ${firstRet}             松勤网
    close browser
