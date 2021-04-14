import os
import helper
from getpass import getpass


user_db_path = "data/users_records/"


def create(user_account_number, first_name, last_name, email, password, balance):

    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file
    
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(balance)

    if helper.account_number_exist(user_account_number):

        return False

    if helper.email_exist(email):
        print("User already exists \n")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:

        file_contain_data = read(user_db_path + str(user_account_number) + ".txt")
        if not file_contain_data:
            delete(user_account_number)

    else:

        f.write(str(user_data));
        completion_state = True

    finally:

        f.close();
        return completion_state


def read(user_account_number):

    # find user with account number
    # fetch content of the file
    valid_account_number = helper.account_number_validation(user_account_number)

    try:

        if valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User account not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def update(user_account_number, updated_balance):
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true
    
    user_record_list = str.split(read(user_account_number), ',')
    
    user_data = user_record_list[0] + "," + user_record_list[1] + "," + user_record_list[2] + "," + user_record_list[3] + "," + str(updated_balance)

    f = open(user_db_path + str(user_account_number) + ".txt", "w")
    f.write(str(user_data))
    f.close()


def delete(user_account_number):

    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful        