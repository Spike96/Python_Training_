from sys import maxsize

class Users:

    def __init__(self, f_name, l_name, nickname, email, id=None):
        self.f_name = f_name
        self.l_name = l_name
        self.nickname = nickname
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.f_name, self.l_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.f_name == other.f_name, \
               self.l_name == other.l_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize