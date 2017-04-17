
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook",
                user="root", password="")


try:
    l = db.get_users_not_in_group(Group(id="98"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()

'''try:
    l = db.get_users_in_group(Group(id="98"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()'''

'''try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    pass # db.destroy()'''

'''try:
    users = db.get_users_list()
    for user in users:
        print(user)
    print(len(users))
finally:
    pass # db.destroy()'''
