from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver=webdriver.Chrome()
    return driver



def pytest_addoption(parser):  # this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # this will return thr browser value to setup method


#################Pytest HTML Report###################################


def pytest_configure(config):
    config._metadata['Project Name'] = 'Ecommerce demo '
    config._metadata['Module'] = 'Customer '
    config._metadata['Tester'] = 'Mohit K '


    #hook for delete /Modify Enviroment info to HTML Reports

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)