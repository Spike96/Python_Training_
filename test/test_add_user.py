# -*- coding: utf-8 -*-

from model.users import Users


def test_add_user(app):
    old_users = app.users.get_users_list()
    users = Users(f_name="Vasya", l_name="Vasko", nickname="qwerty", email="vasya@mail.com")
    app.users.create(users)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
    old_users.append(users)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)


'''def test_add_empty_user(app):
    old_users = app.users.get_users_list()
    users = Users(f_name="", l_name="", nickname="", email="")
    app.users.create(users)
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(users)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)'''