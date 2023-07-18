import datetime
from behave import *
from selenium.webdriver.common.by import By
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigated to Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    account_page = AccountPage(context.driver)
    assert account_page.display_status_of_edit_your_account_information_option()


@when(u'I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(context, password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    assert context.login_page.display_status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")


@when(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")


@when(u'I enter invalid email and valid password say "{password}" into the fields')
def step_impl(context, password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)