
from model.users import Users
from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook",
                user="root", password="")


def test_add_user_to_group(app):
    if len(db.get_users_list()) == 0:
        app.users.create(Users(firstname="somebody", lastname="someone", email="vasya@mail.com",
                               homephone=12345, workphone=123456, mobilephone=1234567, address="somewhere"))
    elif len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group for user"))
    else:
        old_user = db.get_users_list()
        old_group = db.get_group_list()
        if old_group:
            new_group = db.get_group_list()
            group = random.choice(new_group)
            group_id = group.id
            if old_user:
                new_user = db.get_users_not_in_group(group)
                random_user = random.choice(new_user)
                id = random_user.id
                ui_list = db.get_users_in_group(group)
                app.users.add_user_to_group(id, group_id)
                db_list = db.get_users_in_group(group)
                ui_list.append(random_user)
                assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
















