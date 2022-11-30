import time

from pages.elements_page import TextBoxPage, LinksPage, NavigationPage, SortMenu


class TestSearch:  # тест поиска
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
            text_box_page.open()
            text_box_page.fill_fields()


time.sleep(5)


class TestLinkLanguages:  # тест функционала переключения на определенный язык программирование при поиске

    def test_check_link(self, driver):
        check_link = LinksPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_link.open()
        check_link.check_new_tab()


time.sleep(5)


class TestNavigation:  # тест пагинации в результатах поиска

    def test_navigation_link(self, driver):
        check_navigation = NavigationPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_navigation.open()
        check_navigation.check_link_navigation()


time.sleep(5)


class TestSort:  # тест сортировки

    def test_sort_menu(self, driver):
        check_sort = SortMenu(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_sort.open()
        check_sort.check_sort_menu()
