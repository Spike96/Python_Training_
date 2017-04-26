from model.users import Users
from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook",
                user="root", password="")


def delete_user_from_group(app):
    new_group = db.get_group_list()
    group = random.choice(new_group)
    if len(db.get_users_list()) == 0:
        app.users.create(Users(firstname="somebody", lastname="someone", email="vasya@mail.com",
                               homephone=12345, workphone=123456, mobilephone=1234567, address="somewhere"))
    elif len(db.get_group_list()) == 0:
        app.create(Group(name="New group for user"))
    elif len(db.get_users_in_group(group)) == 0:
        app.add_user_to_group()
    else:
        ui_list = db.get_users_in_group(group)
        random_user = random.choice(ui_list)
        app.users.delete_user_from_group()
        db_list = db.get_users_in_group(group)
        ui_list.remove(random_user)
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

