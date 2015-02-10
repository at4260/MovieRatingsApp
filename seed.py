import model
from model import User
import csv

def load_users(session):
    # use u.user
    f = open("./seed_data/u.user")
    for line in f:
        data = line.split("|")
        user_id = data[0]
        user_age = data[1]
        user_zipcode = data[4]
        my_new_user = User(age=user_age, zipcode=user_zipcode)
        session.add(my_new_user)
    session.commit()


def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    load_users(session)
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)
