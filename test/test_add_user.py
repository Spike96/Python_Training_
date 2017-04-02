# -*- coding: utf-8 -*-

from model.users import Users
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Users(firstname="", lastname="", email="", homephone="", workphone="",
                  mobilephone="", address="")] + [
    Users(firstname=random_string("fname ", 7), lastname=random_string("lname ", 10),
          email=random_string("email ", 12), homephone=random_string("home ", 6),
          workphone=random_string("work ", 6), mobilephone=random_string("mobile ", 9),
          address=random_string("", 8))
    for i in range(4)
]


@pytest.mark.parametrize("users", testdata, ids=[str(x) for x in testdata])
def test_add_user(app, users):
    old_users = app.users.get_users_list()
    app.users.create(users)
    assert len(old_users) + 1 == app.users.count()
    new_users = app.users.get_users_list()
    old_users.append(users)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)








'''def test_add_empty_user(app):
    old_users = app.users.get_users_list()
    users = Users(f_name="", l_name="", nickname="", email="", homephone="", address="")
    app.users.create(users)
    new_users = app.users.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(users)
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)'''