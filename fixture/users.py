from model.users import Users


class UsersHelper:

    def __init__(self, app):
        self.app = app

    def create(self, users):
        wd = self.app.wd
        self.add_new_user()
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

    def add_new_user(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def delete_first_user(self):
        wd = self.app.wd
        # select first user
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_users_list(self):
        wd = self.app.wd
        users = []
        for element in wd.find_elements_by_css_selector('[name="entry"]'):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            users.append(Users(f_name=text, l_name=text, nickname=text, email=text, id=id))
        return users
