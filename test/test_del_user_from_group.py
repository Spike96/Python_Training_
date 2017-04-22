
from model.users import Users
import random


def del_user_from_group(app, db, check_ui):
    if len(db.get_users_in_group) == 0:
        app.users.add_user_to_group(app)
    else:
        app.users.del_user_from_group()
    old_users = db.get_users_list()
    user = random.choice(old_users)
    app.users.delete_user_by_id(user.id)
    new_users = db.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(new_users, key=Users.id_or_max) == sorted(app.group.get_users_list(), key=Users.id_or_max)