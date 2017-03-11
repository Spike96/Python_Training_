# -*- coding: utf-8 -*-

import pytest

from fixture.application_user import Application
from model.users import Users


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


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
