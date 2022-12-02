from selenium.webdriver import Keys
from locators.elements_page_locators import TextBoxPageLocators, LinksPageLocators, LinksNavigationLocators, \
    SortMenuLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):  # элементы для теста поиска
    locators = TextBoxPageLocators()

    def testboxsearchone(self):
        self.element_it_visible(self.locators.SEARCH).clear()  # чистит поле поиска
        self.element_it_visible(self.locators.SEARCH).send_keys('Js')  # вводит в поле поиска "Js"
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)  # нажимает клавишу Enter
    def testboxsearchtwo(self):
        self.element_it_visible(self.locators.SEARCH).clear()  # чистит поле поиска
        self.element_it_visible(self.locators.SEARCH).send_keys("Hello")  # вводит в поле поиска "Hello"
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)  # нажимает клавишу Enter
    def testboxsearchthree(self):
        self.element_it_visible(self.locators.SEARCH).clear()  # чистит поле поиска
        self.element_it_visible(self.locators.SEARCH).send_keys("1234")  # вводит в поле поиска "1234"
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)  # нажимает клавишу Enter
    def testboxsearchfour(self):
        self.element_it_visible(self.locators.SEARCH).clear()  # чистит поле поиска
        self.element_it_visible(self.locators.SEARCH).send_keys(".")  # вводит в поле поиска "."
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)  # нажимает клавишу Enter
    def testboxsearchfive(self):
        self.element_it_visible(self.locators.SEARCH).clear()  # чистит поле поиска
        self.element_it_visible(self.locators.SEARCH).send_keys("рецепт пирога")  # вводит в поле поиска "рецепт пирога"
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)  # нажимает клавишу Enter
    def testboxsearchsix(self):
        self.element_it_visible(self.locators.SEARCH).clear()  # чистит поле поиска
        self.element_it_visible(self.locators.SEARCH).send_keys("-1234")  # вводит в поле поиска "-1234"
        self.element_it_visible(self.locators.SEARCH).send_keys(Keys.ENTER)  # нажимает клавишу Enter


class LinksPage(BasePage):  # элементы для теста функционала переключения на определенный язык программирование при поиске
    locators = LinksPageLocators()
    def check_new_tab_python(self):  # Выбирает язык программирования PYTHON
        python_link = self.element_it_clickable(self.locators.PYTHON).click()
    def check_new_tab_javascript(self):  # Выбирает язык программирования javascript
        java_skript_link = self.element_it_clickable(self.locators.JAVASCRIPTS).click()
    def check_new_tab_java(self):  # Выбирает язык програмирования JAVA
        java_link = self.element_it_clickable(self.locators.JAVA).click()
    def check_new_tab_html(self):  # Выбирает язык програмирования HTML
        java_link = self.element_it_clickable(self.locators.HTML).click()
    def check_new_tab_cplusplus(self):  # Выбирает язык програмирования C++
        java_link = self.element_it_clickable(self.locators.CPLUSPLUS).click()
    def check_new_tab_c(self):  # Выбирает язык програмирования C
        java_link = self.element_it_clickable(self.locators.C).click()
    def check_new_tab_jupyter_notebook(self):  # Выбирает язык програмирования Jupyter notebook
        java_link = self.element_it_clickable(self.locators.JUPYTER).click()
    def check_new_tab_csharp(self):  # Выбирает язык програмирования C#
        java_link = self.element_it_clickable(self.locators.CSHARP).click()
    def check_new_tab_php(self):  # Выбирает язык програмирования PHP
        java_link = self.element_it_clickable(self.locators.PHP).click()
    def check_new_tab_css(self):  # Выбирает язык програмирования CSS
        java_link = self.element_it_clickable(self.locators.CSS).click()


class NavigationPage(BasePage):  # элементы для теста пагинации в результатах поиска
    locators = LinksNavigationLocators()
    def check_link_navigation_next(self):
        test_pagination = self.element_it_clickable(self.locators.NEXT).send_keys(Keys.END)  # проматывает страницу
        page_next = self.element_it_clickable(self.locators.NEXT).click()  # нажимает в пагинации кнопку NEXT
    def check_link_navigation_pageone(self):
        test_pagination = self.element_it_clickable(self.locators.PAGEONE).send_keys(Keys.END)  # проматывает страницу
        page_next = self.element_it_clickable(self.locators.PAGEONE).click()  # нажимает в пагинации кнопку PAGEONE
    def check_link_navigation_pagetwo(self):
        test_pagination = self.element_it_clickable(self.locators.PAGETWO).send_keys(Keys.END)  # проматывает страницу
        page_next = self.element_it_clickable(self.locators.PAGETWO).click()  # нажимает в пагинации кнопку PAGETWO
    def check_link_navigation_previos(self):
        test_pagination = self.element_it_clickable(self.locators.PREVIOS).send_keys(Keys.END)  # проматывает страницу
        page_next = self.element_it_clickable(self.locators.PREVIOS).click()  # нажимает в пагинации кнопку PREVIOS


class SortMenu(BasePage):  # элементы для теста сортировки
    locators = SortMenuLocators()
    def check_sort_menu_bestmatch(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_beatmatch = self.element_it_visible(self.locators.BESTMATCH).click()  # выбирает в селекторе BESTMATCH
    def check_sort_menu_moststart(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_moststart = self.element_it_visible(self.locators.MOSTSTART).click()  # выбирает в селекторе MOSTSTART
    def check_sort_menu_feweststart(self):
        sort_sortoptions = self.element_it_visible(
            self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_feweststart = self.element_it_visible(
            self.locators.FEWESTSTART).click()  # выбирает в селекторе FEWESTSTART
    def check_sort_menu_mostforks(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_mostforks = self.element_it_visible(self.locators.MOSTFORKS).click()  # выбирает в селекторе MOSTFORKS
    def check_sort_menu_fewestforks(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_fewestforks = self.element_it_visible(
            self.locators.FEWESTFORKS).click()  # выбирает в селекторе FEWESTFORKS
    def check_sort_menu_recently(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_recently = self.element_it_visible(self.locators.RECENTLY).click()  # выбирает в селекторе RECENTLY
    def check_sort_menu_leastrecently(self):
        sort_match = self.element_it_visible(self.locators.SORTOPTIONS).click()  # нажимает кнопку селектора сортировки
        sort_leastrecently = self.element_it_visible(self.locators.LEASTRECENTLY).click()  # выбирает в селекторе
