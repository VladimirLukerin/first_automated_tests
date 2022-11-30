<<<<<<<<< Temporary merge branch 1
import time
=========

>>>>>>>>> Temporary merge branch 2

from pages.elements_page import TextBoxPage, LinksPage, NavigationPage, SortMenu


class TestSearch:  # тест поиска
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
            text_box_page.open()
<<<<<<<<< Temporary merge branch 1
            text_box_page.fill_fields()


time.sleep(5)
=========
            text_box_page.testboxsearchone()
            text_box_page.testboxsearchtwo()
            text_box_page.testboxsearchthree()
            text_box_page.testboxsearchfour()
            text_box_page.testboxsearchfive()
            text_box_page.testboxsearchsix()



>>>>>>>>> Temporary merge branch 2


class TestLinkLanguages:  # тест функционала переключения на определенный язык программирование при поиске

    def test_check_link(self, driver):
        check_link = LinksPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_link.open()
        check_link.check_new_tab()


<<<<<<<<< Temporary merge branch 1
time.sleep(5)
=========

>>>>>>>>> Temporary merge branch 2


class TestNavigation:  # тест пагинации в результатах поиска

    def test_navigation_link(self, driver):
        check_navigation = NavigationPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_navigation.open()
        check_navigation.check_link_navigation()


<<<<<<<<< Temporary merge branch 1
time.sleep(5)
=========

>>>>>>>>> Temporary merge branch 2


class TestSort:  # тест сортировки

    def test_sort_menu(self, driver):
        check_sort = SortMenu(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_sort.open()
        check_sort.check_sort_menu()
