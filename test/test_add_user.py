# -*- coding: utf-8 -*-

from model.users import Users


def test_add_user(app):
    app.users.create(Users(f_name="Vasya", l_name="Vasko",
                           nickname="qwerty", email="vasya@mail.com"))


def test_add_empty_user(app):
    app.users.create(Users(f_name="", l_name="",
                           nickname="", email=""))
