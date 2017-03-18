# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new_group", header="groups", footer="groups_0"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
