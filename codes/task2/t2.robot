*** Settings ***
Library     SeleniumLibrary     implicit_wait=10

*** Test Cases ***
用例1

        ${var1}     convert to integer      100
        ${var2}     set variable        5
        should be true      ${var1}*int(${var2}) == 500



*** Test Cases ***
用例2
    open browser        http://www.baidu.com        chrome
    Input Text                    id=kw                   北京时间\n
    ${firstRet}=                  Get Text                css=p.op-beijingtime-datebox>span.op-beijingtime-date
    Should Contain                ${firstRet}             2019
    close browser
