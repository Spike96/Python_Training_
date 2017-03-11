# -*- coding: utf-8 -*-

import pytest
from users import Users
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.create_user(Users(f_name="Vasya", l_name="Vasko",
                          nickname="qwerty", email="vasya@mail.com"))
    app.logout()


def test_add_empty_user(app):
    app.login(username="admin", password="secret")
    app.create_user(Users(f_name="", l_name="",
                          nickname="", email=""))
    app.logout()