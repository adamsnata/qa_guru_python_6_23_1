import os

import pytest
from allure_commons._allure import attach
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser

import configuration


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({

        'platformName': configuration.settings.android_platform,
        'platformVersion': configuration.settings.android_version,
        'deviceName': configuration.settings.android_device,

        'app': configuration.settings.app_url,

        'bstack:options': {
            'projectName': configuration.settings.project_name,
            'buildName': configuration.settings.build_name,
            'sessionName': configuration.settings.session_name,

            'userName': configuration.settings.browserstack_username,
            'accessKey': configuration.settings.browserstack_key
        }
    })

    browser.config.driver = webdriver.Remote(configuration.settings.browserstack_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.allure_attach_bstack_screenshot()

    session_id = browser.driver.session_id
    attach.allure_attach_bstack_video(session_id)
    browser.quit()
