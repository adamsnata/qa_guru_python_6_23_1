from time import sleep

import pytest
from appium.options.android import UiAutomator2Options

from appium import webdriver
from selene import browser
import os


import project
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({

        'platformName': project.settings.android_platform,
        'platformVersion': project.settings.android_version,
        'deviceName': project.settings.android_device,

        'app': project.settings.app_url,

        'bstack:options': {
            'projectName': project.settings.project_name,
            'buildName': project.settings.build_name,
            'sessionName': project.settings.session_name,

            'userName': project.settings.browserstack_username,
            'accessKey': project.settings.browserstack_key
        }
    })

    browser.config.driver = webdriver.Remote(project.settings.browserstack_url, options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    attach.allure_attach_bstack_screenshot()

    session_id = browser.driver.session_id
    attach.allure_attach_bstack_video(session_id)
    browser.quit()
