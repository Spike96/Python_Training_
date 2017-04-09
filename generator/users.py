from model.users import Users
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 4
f = "data/users.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Users(firstname="", lastname="", email="", homephone="", workphone="",
                  mobilephone="", address="")] + [
    Users(firstname=random_string("fname ", 7), lastname=random_string("lname ", 10),
          email=random_string("email ", 12), homephone=random_string("home ", 6),
          workphone=random_string("work ", 6), mobilephone=random_string("mobile ", 9),
          address=random_string("", 8))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f_out:
    f_out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))