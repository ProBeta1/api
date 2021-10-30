import random



class Email:
    def __init__(self, email):
        self.email = email
    def generate_otp(self):
        self.otp = random.randint(111111, 999999)
        email_send_check = self.email_otp()
        if email_send_check == -1:
            return -1
        else:
            return str(self.otp)
    def email_otp(self):
        # Implement Twilio Code to send OTP here
        pass


# function email_otp will contain the code to email the OTP