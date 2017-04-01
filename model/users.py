from sys import maxsize

class Users:

    def __init__(self, firstname=None, lastname=None, email=None, address=None, homephone=None,
                workphone=None,  mobilephone=None, all_phones_from_home_page=None, all_emails_from_home_page=None,
                 id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname, \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize