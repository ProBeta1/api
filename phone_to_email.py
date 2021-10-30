@app.route('/handle-sms', methods=['POST'])
def handle_sms():
    lookup = Lookup()
    try:
        email = {
            'text': request.form['Body'],
            'subject': 'Text message',
            'from_email': phone_to_email(request.form['From']),
            'to': lookup.email_for_phone(request.form['To'])
        }
    except InvalidInput, e:
        return warn(str(e)), 400

    message = sendgrid.Mail(**email)
    (status, msg) = sendgrid_api.send(message)
    if 'errors' in msg:
        template = "Error sending message to SendGrid: {}"
        errors = ', '.join(msg['errors'])
        error_message = template.format(errors)
        return warn(error_message), 400
    else:
        return ''
