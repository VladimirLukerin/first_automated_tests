from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_it_visible(self,locator,timeout=5):#Ждет пока элемент станет видимый
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def element_it_clickable(self,locator,timeout=5):#Ждет пока элемент станет видимый
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))