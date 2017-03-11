from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def create_user(self, users):
        wd = self.wd
        # fill in users form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(users.f_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(users.l_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(users.nickname)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(users.email)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")

    def destroy(self):
        self.wd.quit()