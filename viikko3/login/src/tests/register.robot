*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newusername
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password And Confirmation
    Set Username  matchinguser
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Click  button >> text=Register
    Register Should Succeed

Register With Mismatched Password And Confirmation
    Set Username  mismatchuser
    Set Password  kalle12345
    Set Password Confirmation  differentpass
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation must match

Register With Password That Contains Numbers
    Set Username  validnumberuser
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password That Contains Special Character
    Set Username  validspecialuser
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password That Consists Only Of Letters
    Set Username  lowercaselettersuser
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password cannot consist only of letters

Register With Password That Consists Only Of Uppercase Letters
    Set Username  uppercaselettersuser
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password cannot consist only of letters

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  newusername
    Set Password  1
    Set Password Confirmation  1
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle12345
    Set Password Confirmation  kalle12345
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}