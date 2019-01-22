*** Settings ***
Library  SeleniumLibrary
Library  Collections


*** Keywords ***
/login website
    [Arguments]     ${username}     ${password}
    Open Browser                  http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait    5
    Input Text                    id=username                   ${username}
    Input Text                    id=password                   ${password}
    click element                  css=button[onclick*="postLoginRequest()"]

goto Teacher Management
    click element                  css=a [ui-sref="teacher"]

create course
    [Arguments]         ${name}     ${desc}     ${idx}
    click element       css=button[ng-click*="showAddOne=true"]
    Input Text      css=input[ng-model*='addData.name']       ${name}
    Input Text      css=textarea[ng-model*='addData.desc']      ${desc}
    Input Text      css=input[ng-model*="addData.display_idx"]     ${idx}
    click element       css=button[ng-click*='addOne()']

get course list

    ${courseList}   create list
    ${eles}        Get Web Elements        css=tr>td:nth-child(2)
    :FOR    ${ele}      IN      @{eles}
    \       append to list      ${courseList}       ${ele.text}
    [Return]    ${courseList}