*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newusername
    Set Password  kalle12345
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle12345
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  newusername
    Set Password  1
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle12345
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