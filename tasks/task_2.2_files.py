from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element_by_css_selector('input[name = "firstname"]')
    input_first_name.send_keys('Ivan')

    input_last_name = browser.find_element_by_css_selector('input[name = "lastname"]')
    input_last_name.send_keys('Ivanov')

    input_email = browser.find_element_by_css_selector('input[name = "email"]')
    input_email.send_keys('test@test.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_for_input.txt')

    input_file = browser.find_element_by_css_selector('input[name = "file"]')
    input_file.send_keys(file_path)

    button_submit = browser.find_element_by_css_selector('button.btn')
    button_submit.click()

finally:
    time.sleep(5)
    browser.quit()
