import allure_commons
import allure
import pytest
from selene import browser, support
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils import allure_helper
import project


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
            'accessKey': project.settings.browserstack_accesskey
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(project.settings.browserstack_url, options=options)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure_helper.attach_bstack_screenshot()
    allure_helper.attach_bstack_page_source()
    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    allure_helper.attach_bstack_video(session_id)