def find_username(username, db):
    if (user := db.find_one({"username": username})) is not None:
        return user


def find_email(email, db):
    if (user := db.find_one({"email": email})) is not None:
        return user
