import os
import database


user_db_path = "data/users_records/"


def email_exist(email):

    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(database.read(user), ',')
        if email in user_list:
            return True
    return False


def account_number_exist(account_number):

    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def authenticated_user(account_number, password):

    if account_number_exist(account_number):
        user = str.split(database.read(account_number), ',')

        if password == user[3]:
            return user

    return False


def account_number_validation(account_number):

    if account_number:

        try:
            int(account_number)

            if len(str(account_number)) == 10:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False


def input_validation(amount):

    if amount:

        try:
            int(amount)

            if int(amount) > 0:
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False