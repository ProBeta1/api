# Main API file

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# random required for generating the OTP
import random
import json

# importing important classes
import Email 
import Users

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# resp_json = [
#         {
#             "name": "blue candy",
#             "flavour": "sweet",
#             "givenby": "gagan1",

#         }, 
#         {
#             "name": "blue candy 2",
#             "flavour": "spicy",
#             "givenby": "gagan2"

#         },
#         {
#             "name": "pink candy",
#             "flavour": "sour",
#             "givenby": "gag",

#         }
#     ]






# Email sent on this route using get request
# OTP sent on that email. OTP also sent back as a response
@app.route('/verify', methods=['GET'])
@cross_origin()
def verify_email():
    email = request.args.get('email')
    otp_obj = Email.Email(email)
    otp_to_be_sent = otp_obj.generate_otp()
    del otp_obj
    # return otp_to_be_sent
    return str(otp_to_be_sent)


# Routes to deal with data will be added here
@app.route('/getdata', methods=['GET'])
@cross_origin()
def fetch_data():
    print("request in getdata")
    email = request.args.get('email')
    # returning temporary response for now
    user_obj_temp = Users.User(email)
    user_list = user_obj_temp.fetch_user_data()
    if user_list == -1:
        return json.dumps([{"givenby": "Add first Candy Name", "name": "Add who gave this candy"}])
    else:
        return jsonify(user_list)


@app.route('/add/candy', methods=['GET'])
def add_candy():
    # "name": "blue candy",
    #         "flavour": "sweet",
    #         "givenby": [
    #             "gagan1@gagan1.com",
    #         ],
    #         "thanked": "no",
    email = request.args.get("email")
    print("email recieved in add candy -> ", email)
    name = request.args.get("name")
    # flavour = request.args.get("flavour")
    givenby = request.args.get("given")
    print("name -> ", name)
    print("givenby -> ", givenby)
    # resp_json.append({
    #     "name": name,
    #     "flavour": flavour,
    #     "givenby": [givenby],
    # })
    temp_obj1 = Users.User(email)
    inp_resp = temp_obj1.insert_user_data(name, givenby)
    if inp_resp == 1:
        print("Insert success")
        return "1"
    print("resp json -> ", resp_json)
    print(resp_json)
    return jsonify(resp_json)



# @app.route('/delete/candy', methods=['GET'])
# def delete_candy():
#     index_to_be_deleted = request.args.get('index')
#     resp_json.pop(index_to_be_deleted)
#     return "1"



@app.route("/test")
def test_route():
    print("Test route reached")
    return "Test route"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')