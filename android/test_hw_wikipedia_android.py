import allure
from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy

def test_search_article_by_title_appium():
    with allure.step('Type "Appium"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_article_by_title_python():
    with allure.step('Type "Python"'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")
    with allure.step('Verify content found'):
        article = browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        article.should(have.text("Python"))
    with allure.step('Open article'):
        article.click()
    with allure.step('Error occured'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text'))