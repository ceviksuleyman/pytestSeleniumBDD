from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigated to Login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, "input-email").send_keys(email)
    context.driver.find_element(By.ID, "input-password").send_keys(password)


@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I should get logged in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    context.driver.quit()


@when(u'I enter invalid email and valid password say "{password}" into the fields')
def step_impl(context, password):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "CS" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__eq__(expected_message)
    context.driver.quit()


@when(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context, email, password):
    context.driver.find_element(By.ID, "input-email").send_keys(email)
    context.driver.find_element(By.ID, "input-password").send_keys(password)


@when(u'I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(context, password):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "CS" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
