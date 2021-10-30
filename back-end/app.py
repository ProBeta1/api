from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# random required for generating the OTP
import random
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

resp_json = [
        {
            "name": "blue candy",
            "flavour": "sweet",
            "givenby": [
                "gagan1@gagan1.com",
            ],
            "thanked": "no",
        }, 
        {
            "name": "blue candy 2",
            "flavour": "spicy",
            "givenby": [
                "gagan2@gagan2.com"
            ],
            "thanked": "no",
        },
        {
            "name": "pink candy",
            "flavour": "sour",
            "givenby": [
                "gag@ga.com",
                "abcd@abcd.com"
            ]
        }
    ]


class Email:
    def __init__(self, email):
        self.email = email
    def generate_otp(self):
        self.otp = random.randint(111111, 999999)
        self.email_otp()
        # 123456 is just a temp OTP I am returning
        return str(123456)
    def email_otp(self):
        # Implement Twilio Code to send OTP here
        pass





# Email sent on this route using get request
# OTP sent on that email. OTP also sent back as a response
@app.route('/verify', methods=['GET'])
@cross_origin()
def verify_email():
    email = request.args.get('email')
    otp_obj = Email(email)
    otp_to_be_sent = otp_obj.generate_otp()
    del otp_obj
    return otp_to_be_sent


# Routes to deal with data will be added here
@app.route('/getdata', methods=['GET'])
@cross_origin()
def fetch_data():
    email = request.args.get('email')
    # returning temporary response for now
    return jsonify(resp_json)


@app.route('/add/candy', methods=['GET'])
def add_candy():
    # "name": "blue candy",
    #         "flavour": "sweet",
    #         "givenby": [
    #             "gagan1@gagan1.com",
    #         ],
    #         "thanked": "no",
    name = request.args.get("name")
    flavour = request.args.get("flavour")
    givenby = request.args.get("given")
    thanked = request.args.get("thanked")
    resp_json.append({
        "name": name,
        "flavour": flavour,
        "givenby": [givenby],
        "thanked": "no",
    })
    print("resp json -> ", resp_json)
    print(resp_json)
    return jsonify(resp_json)

@app.route('/delete/candy', methods=['GET'])
def delete_candy():
    index_to_be_deleted = request.args.get('index')
    resp_json.pop(index_to_be_deleted)
    return "1"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')