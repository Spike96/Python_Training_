from selenium.webdriver.support.ui import Select
from model.users import Users
import re


class UsersHelper:

    def __init__(self, app):
        self.app = app

    def create(self, users):
        wd = self.app.wd
        self.add_new_user()
        # fill in users form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(users.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(users.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(users.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(users.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(users.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(users.workphone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(users.email)
        # submit user creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.user_cache = None

    def add_new_user(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def add_user_to_group(self, id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_id(id)
        wd.find_element_by_name("to_group").click()
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_value(group_id)
        wd.find_element_by_xpath('//input[@name="add"]').click()
        wd.find_element_by_partial_link_text('group page').click()
        self.contact_cache = None

    def sort_by_group_by_id(self, group_id):
        wd = self.app.wd
        select = Select(wd.find_element_by_xpath('//select[@name="group"]'))
        select.select_by_value(group_id)

    def delete_user_from_group(self):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("group"))
        select.select_by_value("10")
        wd.find_element_by_xpath('//input[@name="selected[]').click()
        wd.find_element_by_xpath('//input[@name="remove"]').click()
        wd.find_element_by_partial_link_text('group page').click()
        self.contact_cache = None

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        # select some user
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.user_cache = None

    def delete_user_by_id(self, id):
        wd = self.app.wd
        self.select_user_by_id(id)
        # select some user
        # wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_name("selected[]")
        self.user_cache = None

    def select_user_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()
        # wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_users_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.user_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.user_cache.append(Users(firstname=firstname, lastname=lastname,
                                             all_emails_from_home_page= all_emails,
                                             all_phones_from_home_page=all_phones, id=id, address=address))
        return list(self.user_cache)


    def get_user_info_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_xpath('//td/*[@id="' + id + '"]/../..')
        cells = row.find_elements_by_tag_name("td")
        id = cells[0].find_element_by_tag_name("input").get_attribute("value")
        firstname = cells[2].text
        lastname = cells[1].text
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        return Users(id=id, firstname=firstname, lastname=lastname, address=address,
                     all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones)


    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        return Users(firstname=firstname, lastname=lastname, id=id, address=address, email=email,
                     homephone=homephone, workphone=workphone, mobilephone=mobilephone)


    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Users(homephone=homephone, workphone=workphone, mobilephone=mobilephone)








