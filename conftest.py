import os

import pytest
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture
def config(request, scope='session'):
    BROWSERS = ['Chrome', 'Firefox']

    # Read config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    browser = request.config.option.browser
    if browser is not None:
        config['browser'] = browser

    # Assert values are acceptable
    assert config['browser'] in BROWSERS
    assert isinstance(config['headless'], bool)
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
        b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make call wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()


@pytest.fixture
def assets_path():
    return os.path.join(os.getcwd(), "assets")
