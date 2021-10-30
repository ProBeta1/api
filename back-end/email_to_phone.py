@app.route('/handle-email', methods=['POST'])
def handle_email():
    lookup = Lookup()
    try:
        envelope = simplejson.loads(request.form['envelope'])
        lines = request.form['text'].splitlines(True)
        sms = {
            'to': email_to_phone(request.form['to']),
            'from_': lookup.phone_for_email(envelope['from']),
            'body': lines[0]
        }
    except InvalidInput, e:
        return warn(str(e))

    try:
        rv = twilio_api.messages.create(**sms)
        return rv.sid
    except Exception as e:
        print "oh no"
        print str(e)
        error_message = "Error sending message to Twilio"
        return warn(error_message), 400
