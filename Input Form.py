from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = 'C:\Program Files (x86)\chromedriver'
driver = webdriver.Chrome(PATH)

driver.get(('https://www.seleniumeasy.com/test/basic-first-form-demo.html'))

def single_input():
    single_input = driver.find_element_by_id('user-message')
    message = 'to jest wiadomość'
    single_input.send_keys(message)
    show_message = driver.find_element_by_xpath('//*[@id="get-input"]/button')
    show_message.click()

    #assert
    msg = driver.find_element_by_id('display')
    assert msg.text == message
    print("Single input ok")

single_input()

def two_input():
    input1 = driver.find_element_by_id('sum1')
    input2 = driver.find_element_by_id('sum2')
    num1 = 8
    num2 = 5
    input1.send_keys(num1)
    input2.send_keys(num2)
    get_total = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
    get_total.click()

    #assert
    result = driver.find_element_by_id('displayvalue')
    assert result.text == str(num1+num2)
    print("Two input ok")


two_input()

#end of testing
time.sleep(5)
driver.quit()