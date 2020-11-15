import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default=None, help='Choose browser language: ru, es, fr and etc..')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
       # exepath = r'c:\\webdriver_geckodriver\\geckodriver.exe'

        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_language", user_language)
        fp.update_preferences()

        caps = DesiredCapabilities.FIREFOX.copy()
        caps["firefox_profile"] = fp.encoded
        caps["marionette"] = False

        print('\nstart browser for test..')
       # browser = webdriver.Firefox(executable_path=exepath, firefox_profile=fp, capabilities=caps)
        browser = webdriver.Firefox(firefox_profile=fp, capabilities=caps)

    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser
    print("\nquit browser..")
    browser.quit()
