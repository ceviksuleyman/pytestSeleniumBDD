from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I got navigated to Home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://tutorialsninja.com/demo/')


@when(u'I enter valid product say "HP" into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()
    context.driver.quit()


@when(u'I enter invalid product say "Honda" into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_message = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH,
                                       "//input[@id='button-search']/following-sibling::p").text.__eq__(
        expected_message)
    context.driver.quit()


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
