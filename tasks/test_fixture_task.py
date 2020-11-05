import time
import math
from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1','https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1','https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1','https://stepik.org/lesson/236905/step/1'])
def test_get_correct_answer(browser, link):
    browser.get(link)
    time.sleep(5)

    textarea = browser.find_element_by_css_selector('textarea')

    answer = math.log(int(time.time()))
    browser.implicitly_wait(10)
    textarea.send_keys(str(answer))

    send_btn = browser.find_element_by_css_selector('button.submit-submission')
    send_btn.click()

    time.sleep(3)
    attempt_message = browser.find_element_by_css_selector('div.attempt__message div pre').text

    assert attempt_message == 'Correct!', attempt_message
