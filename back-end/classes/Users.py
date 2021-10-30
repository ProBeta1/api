import sqlite3

class User:
    def __init__(self, email):
        self.email = email
    # user_exists checks whether an user exists or not
    def user_exists(self):
        pass
    # if user does not exists, then this function is called
    def create_new_user(self):
        pass
    def insert_user_data(self):
        pass
    def fetch_user_data(self):
        pass
    def delete_user_data(self):
        pass



    # "name": "blue candy",
    #         "flavour": "sweet",
    #         "givenby": [
    #             "gagan1@gagan1.com",
    #         ],
    #         "thanked": "no",



# def db_setup():
#     con = sqlite3.connect('database.db')
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS usercandy(email TEXT, givenby TEXT, name TEXT)''')
#     con.close()

# db_setup()