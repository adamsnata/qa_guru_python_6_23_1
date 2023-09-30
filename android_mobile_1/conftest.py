import allure_commons
import allure
import pytest
from selene import browser, support
from appium import webdriver
from appium.options.android import UiAutomator2Options

import project
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def android_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
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

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(project.settings.browserstack_url, options=options)

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