import pytest 
import json
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service


CONFIG_PATH = 'tests/config.json'
SUPPORTED_BROWSERS = ['chrome', 'firefox']
driver = None

@pytest.fixture(scope = 'session')
def config(): 
    with open(CONFIG_PATH) as config_file: 
        data = json.load(config_file)
    return data

@pytest.fixture(scope = 'session')
def config_browser(config):
    if 'browser' not in config: 
        raise Exception('The config file does not contain browser')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]} is not a supported browser')
    return config['browser']
 
@pytest.fixture
def browser(config_browser):
    global driver
    if config_browser == 'chrome': 
        op = webdriver.ChromeOptions()
        op.add_argument('--ignore-certificate-errors')
        op.add_argument('--ignore-ssl-errors')
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = op)
    elif config_browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())) 
    #elif config['browser'] == 'edge':
        # not yet implemented 
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    
    yield driver

    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    dateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+"_"+dateString+".png"
            file_name = file_name.split(".py_", 1)[1]
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="file:../Project_Jupiter_Toys/tests/screenshots/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot("..\\Project_Jupiter_Toys\\tests\\screenshots\\" +name)
