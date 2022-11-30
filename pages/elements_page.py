import time

from selenium.webdriver import Keys

from locators.elements_page_locators import TextBoxPageLocators, LinksPageLocators, LinksNavigationLocators, \
    SortMenuLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_fields(self):

        time.sleep(2)
        self.element_it_visible(self.locators.SEARCH).clear()
        time.sleep(2)
        self.element_it_visible(self.locators.SEARCH).send_keys('Js')
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_it_visible(self.locators.SEARCH).clear()
        time.sleep(2)
        self.element_it_visible(self.locators.SEARCH).send_keys("Hello")
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)
        time.sleep(2)
        self.element_it_visible(self.locators.SEARCH).clear()
        time.sleep(2)
        self.element_it_visible(self.locators.SEARCH).send_keys("1234")
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)
        time.sleep(2)


class LinksPage(BasePage):

    locators = LinksPageLocators()

    def check_new_tab(self):
        python_link = self.element_it_visible(self.locators.PYTHON).click()
        time.sleep(3)
        java_skript_link = self.element_it_visible(self.locators.JAVASCRIPTS).click()
        time.sleep(3)
        java_link = self.element_it_visible(self.locators.JAVA).click()
        time.sleep(3)
        java_link = self.element_it_visible(self.locators.HTML).click()
        time.sleep(3)
        java_link = self.element_it_visible(self.locators.PHP).click()
        time.sleep(3)
        java_link = self.element_it_visible(self.locators.CSS).click()


class NavigationPage(BasePage):

    locators = LinksNavigationLocators()

    def check_link_navigation(self):

        test_pagination = self.element_it_visible(self.locators.NEXT).send_keys(Keys.END)
        time.sleep(1)
        page_next = self.element_it_visible(self.locators.NEXT).click()
        time.sleep(3)
        test_pagination = self.element_it_visible(self.locators.PAGEONE).send_keys(Keys.END)
        time.sleep(3)
        page_next = self.element_it_visible(self.locators.PAGEONE).click()
        time.sleep(3)
        test_pagination = self.element_it_visible(self.locators.PAGETWO).send_keys(Keys.END)
        time.sleep(3)
        page_next = self.element_it_visible(self.locators.PAGETWO).click()
        time.sleep(3)
        test_pagination = self.element_it_visible(self.locators.PREVIOS).send_keys(Keys.END)
        time.sleep(3)


class SortMenu(BasePage):
    locators = SortMenuLocators()

    def check_sort_menu(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_beatmatch = self.element_it_visible(self.locators.BESTMATCH).click()
        time.sleep(1)
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_moststart = self.element_it_visible(self.locators.MOSTSTART).click()
        time.sleep(1)
        sort_sortoptions = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_feweststart = self.element_it_visible(self.locators.FEWESTSTART).click()
        time.sleep(1)
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_mostforks = self.element_it_visible(self.locators.MOSTFORKS).click()
        time.sleep(1)
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_fewestforks = self.element_it_visible(self.locators.FEWESTFORKS).click()
        time.sleep(1)
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_recently = self.element_it_visible(self.locators.RECENTLY).click()
        time.sleep(1)
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()
        time.sleep(1)
        sort_leastrecently = self.element_it_visible(self.locators.LEASTRECENTLY).click()
