
from model.group import Group


def test_add_user_to_group(app, db):
    new_users = db.get_users_in_group()
    for new_user in new_users:
        if new_user is not new_users:
            app.users.add_user_to_group()
        elif new_users in new_users:
            pass
    old_users = db.get_users_in_group()
    new_users = db.get_users_in_group()
    assert sorted(old_users, key=Group.id_or_max) == sorted(new_users, key=Group.id_or_max)

