# -*- coding: utf-8 -*-

from model.users import Users
from random import randrange


def test_delete_some_user(app):
    if app.users.count() == 0:
        app.users.create(Users(firstname="somebody", lastname="someone", email="vasya@mail.com",
                               homephone=12345, workphone=123456, mobilephone=1234567, address="somewhere"))
    old_users = app.users.get_users_list()
    index = randrange(len(old_users))
    app.users.delete_user_by_index(index)
    new_users = app.users.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index+1] = []
    assert old_users == new_users
