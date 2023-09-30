import allure_commons
import allure
import pytest
from selene import browser, support
from appium import webdriver
from appium.options.android import UiAutomator2Options

import configuration
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def android_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'platformVersion': configuration.config.android_version,
        'deviceName': configuration.config.android_device,

        'app': configuration.config.app_url,

        'bstack:options': {
            'projectName': configuration.config.project_name,
            'buildName': configuration.config.build_name,
            'sessionName': configuration.config.session_name,

            'userName': configuration.settings.browserstack_username,
            'accessKey': configuration.settings.browserstack_key
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(configuration.config.browserstack_url, options=options)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    attach.allure_attach_bstack_screenshot()

    session_id = browser.driver.session_id
    attach.allure_attach_bstack_video(session_id)
    browser.quit()
    # attach.attach_bstack_screenshot()
    # attach.attach_bstack_page_source()
    # session_id = browser.driver.session_id
    #
    # with allure.step('tear down app session'):
    #     browser.quit()
    #
    # attach.attach_bstack_video(session_id)