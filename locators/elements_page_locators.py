from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    SEARCH = (By.XPATH,"/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")


class LinksPageLocators:
    PYTHON = (By.XPATH,'/html/body/div[4]/main/div/div[2]/div[1]/ul/li[1]/a')
    JAVASCRIPTS = (By.XPATH,'/html/body/div[4]/main/div/div[2]/div[1]/ul/li[2]/a')
    JAVA = (By.XPATH,'/html/body/div[4]/main/div/div[2]/div[1]/ul/li[3]/a')
    HTML = (By.XPATH,'/html/body/div[4]/main/div/div[2]/div[1]/ul/li[4]/a')
    PHP = (By.XPATH,'/html/body/div[4]/main/div/div[2]/div[1]/ul/li[9]/a')
    CSS = (By.XPATH,'/html/body/div[4]/main/div/div[2]/div[1]/ul/li[10]/a')

class LinksNavigationLocators:
    PAGINATION = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[2]/div')
    PREVIOS = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[2]/div/span[1]')
    PAGEONE = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[2]/div/a[2]')
    PAGETWO = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[2]/div/a[1]')
    NEXT = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[2]/div/a[7]')

class SortMenuLocators:
    SORTOPTIONS = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details')
    BESTMATCH = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[1]')
    MOSTSTART = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[2]')
    FEWESTSTART = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[3]')
    MOSTFORKS = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[4]')
    FEWESTFORKS = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[5]')
    RECENTLY = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[6]')
    LEASTRECENTLY = (By.XPATH,'/html/body/div[4]/main/div/div[3]/div/div[1]/details/details-menu/div[2]/a[7]')