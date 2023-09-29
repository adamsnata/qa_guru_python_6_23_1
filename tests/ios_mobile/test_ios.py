from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_add_single_row():
    with step('Type text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('Eminem' + '\n')

        with step('Verify added row'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('Eminem'))


