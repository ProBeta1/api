import sqlite3
import copy
class User:
    def __init__(self, email):
        self.email = email
    # user_exists checks whether an user exists or not
    def user_exists(self):
        print("email in user_exists -> ", self.email)
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('''SELECT * FROM usercandy WHERE email=?''', (str(self.email), ))
        # rsp0 = cur.fetchone()
        # print(rsp0)
        # print("oneone -> ", oneone)
        # for u in oneone:
        #     print(u)
        resp1 = cur.fetchall()
        print("resp1 -> ", resp1)
        if len(resp1) == 0:
            print(f'empty resp1')
            # return 0 if empty
            return 0
        else:
            # return 1 if not empty
            print(f"not empty {resp1}")
            return 1 
    # if user does not exists, then this function is called
    # def create_new_user(self):
    #     pass
    def insert_user_data(self, candyname, givenby):
        try:
            print("inside insert user data")
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute(''' INSERT INTO usercandy(email, givenby, name) VALUES(?, ?, ?)''', (self.email, givenby, candyname, ))
            con.commit()
            print("insert good")
            con.close()
            return 1
        except Exception as e:
            print("Excpetion -> ", e)
            return -1

    # for fetching the data from the table

    def fetch_user_data(self):
        user_exists = self.user_exists()
        if user_exists == 1:
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('''SELECT * FROM usercandy WHERE email=?''', (self.email, ))
            resp1 = cur.fetchall()
            final_resp = []
            for u in resp1:
                temp_dict = copy.deepcopy({})
                temp_dict["name"] = u[2]
                temp_dict["givenby"] = u[1]
                final_resp.append(temp_dict)
            return final_resp
        else:
            print("User does not exists, cannot fetch data")
            return -1

#     def delete_user_data(self):
#         pass



# temp_obj1 = User('random@random.com')
# temp_obj1.user_exists()
# temp_obj1.fetch_user_data()

    #         "name": "blue candy",
    #         "flavour": "sweet",
    #         "givenby": "gagan1@gagan1.com",
    #         "thanked": "no",



# def db_setup():
#     con = sqlite3.connect('database.db')
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS usercandy(email TEXT, givenby TEXT, name TEXT)''')
#     con.close()

# db_setup()