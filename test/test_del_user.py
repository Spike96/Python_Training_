# -*- coding: utf-8 -*-

from model.users import Users


def test_delete_first_user(app):
    if app.users.count() == 0:
        app.users.create(Users(f_name="somebody", l_name="someone",
                               nickname="qwerty", email="vasya@mail.com"))
    app.users.delete_first_user()
