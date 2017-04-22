
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook",
                user="root", password="")

'''def test_add_user_to_group(app, db):
    new_users = db.get_users_in_group()
    old_users = db.get_users_list()
    for new_user in old_users:
        if new_user not in new_users:
            app.users.add_user_to_group()
        elif new_user in new_users:
            pass
    old_users = db.get_users_in_group()
    new_users = db.get_users_in_group()
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)'''

def test_add_user_to_group(app):
    new_users = db.get_users_not_in_group()
    for new_u in new_users:
        if new_u in new_users:
            app.users.add_user_to_group()



