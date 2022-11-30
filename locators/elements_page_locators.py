from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    SEARCH = (By.CSS_SELECTOR, "body > div.logged-out.env-production.page-responsive > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu--logged-out.p-responsive.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.pt-7.pb-4.top-0 > div > div > div.d-lg-flex.min-width-0.mb-2.mb-lg-0 > div > div > form > label > input.form-control.js-site-search-focus.header-search-input.jump-to-field.js-jump-to-field")


class LinksPageLocators:
    PYTHON = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(1) > a')
    JAVASCRIPTS = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(2) > a')
    JAVA = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(3) > a')
    HTML = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(4) > a')
    CPLUSPLUS = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(5) > a')
    C = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(6) > a')
    JUPYTER = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(7) > a')
    CSHARP = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(8) > a')
    PHP = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(9) > a')
    CSS = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-3.float-left.px-md-2 > div.border.rounded-2.p-3.mb-3.d-none.d-md-block > ul > li:nth-child(10) > a')

class LinksNavigationLocators:
    PAGINATION = (By.XPATH, '/html/body/div[4]/main/div/div[3]/div/div[2]/div')
    PREVIOS = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a.previous_page')
    PAGEONE = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a:nth-child(2)')
    PAGETWO = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a:nth-child(3)')
    NEXT = (By.CSS_SELECTOR, 'body > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.paginate-container.codesearch-pagination-container > div > a.next_page')

class SortMenuLocators:
    SORTOPTIONS = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > summary')
    BESTMATCH = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(1)')
    MOSTSTART = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(2)')
    FEWESTSTART = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(3)')
    MOSTFORKS = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(4)')
    FEWESTFORKS = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(5)')
    RECENTLY = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(6)')
    LEASTRECENTLY = (By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive > div.application-main > main > div > div.col-12.col-md-9.float-left.px-2.pt-3.pt-md-0.codesearch-results > div > div.d-flex.flex-column.flex-md-row.flex-justify-between.border-bottom.pb-3.position-relative > details > details-menu > div.select-menu-list > a:nth-child(7)')