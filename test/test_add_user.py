# -*- coding: utf-8 -*-

from model.users import Users


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.users.create(Users(f_name="Vasya", l_name="Vasko",
                           nickname="qwerty", email="vasya@mail.com"))
    app.session.logout()


def test_add_empty_user(app):
    app.session.login(username="admin", password="secret")
    app.users.create(Users(f_name="", l_name="",
                           nickname="", email=""))
    app.session.logout()
