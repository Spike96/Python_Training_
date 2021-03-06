import pymysql.cursors
from model.group import Group
from model.users import Users


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password,
                                          autocommit = True)
        # self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_users_list(self):
        list_u = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, email, "
                           "address from addressbook where deprecated= '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, email, address) = row
                list_u.append(Users(id=str(id), firstname=firstname, lastname=lastname,
                                    email=email, address=address))
        finally:
            cursor.close()
        return list_u

    def destroy(self):
        self.connection.close()


    # def get_users_in_group(self):
    #     list_u_g = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute("select id from address_in_groups where deprecated= '0000-00-00 00:00:00'")
    #         for row in cursor:
    #             id = row
    #             list_u_g.append(Users(id=str(id)))
    #     finally:
    #         cursor.close()
    #     return list_u_g
    #
    # def get_users_not_in_group(self):
    #     list_u_g = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute("select id, group_id from address_in_groups where deprecated= '0000-00-00 00:00:00'")
    #         for row in cursor:
    #             (id, group_id) = row
    #             list_u_g.append(Group(id=str(id), group_id=str(group_id)))
    #     finally:
    #         cursor.close()
    #     return list_u_g
    #
    #

