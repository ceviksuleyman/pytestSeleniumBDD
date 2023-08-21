import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigate to Register Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "CS" + time_stamp + "@gmail.com"
    for row in context.table:
        context.driver.find_element(By.ID, "input-firstname").send_keys(row["first_name"])
        context.driver.find_element(By.ID, "input-lastname").send_keys(row["last_name"])
        context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
        context.driver.find_element(By.ID, "input-telephone").send_keys(row["telephone"])
        context.driver.find_element(By.ID, "input-password").send_keys(row["password"])
        context.driver.find_element(By.ID, "input-confirm").send_keys(row["password"])


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then(u'Account should get created')
def step_impl(context):
    expected_message = "Your Account Has Been Created!"
    context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_message)


@when(u'I enter below details into all fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "CS" + time_stamp + "@gmail.com"
    for row in context.table:
        context.driver.find_element(By.ID, "input-firstname").send_keys(row["first_name"])
        context.driver.find_element(By.ID, "input-lastname").send_keys(row["last_name"])
        context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
        context.driver.find_element(By.ID, "input-telephone").send_keys(row["telephone"])
        context.driver.find_element(By.ID, "input-password").send_keys(row["password"])
        context.driver.find_element(By.ID, "input-confirm").send_keys(row["password"])
        context.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.driver.find_element(By.ID, "input-firstname").send_keys(row["first_name"])
        context.driver.find_element(By.ID, "input-lastname").send_keys(row["last_name"])
        context.driver.find_element(By.ID, "input-telephone").send_keys(row["telephone"])
        context.driver.find_element(By.ID, "input-password").send_keys(row["password"])
        context.driver.find_element(By.ID, "input-confirm").send_keys(row["password"])
        context.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    print(u'STEP: When I enter existing accounts email into email field')


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print(u'STEP: Then Proper warning message informing about duplicate account should be displayed')


@when(u'I dont enter anything into the fields')
def step_impl(context):
    print(u'STEP: When I dont enter anything into the fields')


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    print(u'STEP: Then Proper warning messages for every mandatory fields should be displayed')
