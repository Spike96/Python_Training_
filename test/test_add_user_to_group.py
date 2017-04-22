
from model.users import Users


def test_add_user_to_group(app, db):
    if len(db.get_users_list()) == 0:
        app.users.create()
    else:
        app.users.add_user_to_group(app)
    old_users = db.get_users_in_group()
    new_users = db.get_users_in_group()
    old_users.append()
    assert sorted(old_users, key=Users.id_or_max) == sorted(new_users, key=Users.id_or_max)
