
from pages.elements_page import TextBoxPage, LinksPage, NavigationPage, SortMenu


class TestSearch:  # тест поиска
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
            text_box_page.open()
            text_box_page.testboxsearchone()  # Тест поле поиска 1
            text_box_page.testboxsearchtwo()  # Тест поле поиска 2
            text_box_page.testboxsearchthree()  # Тест поле поиска 3
            text_box_page.testboxsearchfour()  # Тест поле поиска 4
            text_box_page.testboxsearchfive()  # Тест поле поиска 5
            text_box_page.testboxsearchsix()  # Тест поле поиска 6


class TestLinkLanguages:  # тест функционала переключения на определенный язык программирование при поиске

    def test_check_link(self, driver):
        check_link = LinksPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_link.open()
        check_link.check_new_tab_python()  # тест выбора языка python
        check_link.check_new_tab_javascript()  # тест выбора языка javascript
        check_link.check_new_tab_java()  # тест выбора языка java
        check_link.check_new_tab_html()  # тест выбора языка html
        check_link.check_new_tab_cplusplus()  # тест выбора языка C++
        check_link.check_new_tab_c()  # тест выбора языка C
        check_link.check_new_tab_jupyter_notebook()  # тест выбора языка Jupyter notebook
        check_link.check_new_tab_csharp()  # тест выбора языка C#
        check_link.check_new_tab_php()  # тест выбора языка php
        check_link.check_new_tab_css()  # тест выбора языка css


class TestNavigation:  # тест пагинации в результатах поиска

    def test_navigation_link(self, driver):
        check_navigation = NavigationPage(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_navigation.open()
        check_navigation.check_link_navigation_next()  # тест кнопки в пагинации next
        check_navigation.check_link_navigation_pageone()  # тест кнопки в пагинации pageone
        check_navigation.check_link_navigation_pagetwo()  # тест кнопки в пагинации pagetwo
        check_navigation.check_link_navigation_previos()  # тест кнопки в пагинации previos
class TestSort:  # тест сортировки

    def test_sort_menu(self, driver):
        check_sort = SortMenu(driver, 'https://github.com/search?q=code&ref=simplesearch')
        check_sort.open()
        check_sort.check_sort_menu_bestmatch()  #тест селектора сорт, выбор  bestmatch
        check_sort.check_sort_menu_moststart()  #тест селектора сорт, выбор  moststart
        check_sort.check_sort_menu_feweststart()  #тест селектора сорт, выбор  feweststart
        check_sort.check_sort_menu_mostforks()  #тест селектора сорт, выбор  mostforks
        check_sort.check_sort_menu_fewestforks()  #тест селектора сорт, выбор  fewestforks
        check_sort.check_sort_menu_recently()  #тест селектора сорт, выбор  recently
        check_sort.check_sort_menu_leastrecently()  #тест селектора сорт, выбор  leastrecently
