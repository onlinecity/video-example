from flask import Flask
from flask import request
from requests_oauthlib import OAuth1Session

app = Flask(__name__)


# Route for receiving messages.
@app.route('/receiver', methods=['GET', 'POST'])
def receiver():
    if request.method == 'POST':
        req = request.get_json(force=True)
        msg = req['message'].split(' ')
        if msg[1].lower() == 'register':
            __sendReply__(req['msisdn'], 'Thanks for your registration')
        elif msg[1].lower() == 'cancel':
            __sendReply__(req['msisdn'], 'We are sorry to see you go')
        else:
            __sendReply__(
                req['msisdn'],
                f'You wrote {req["message"]}: accepted input is, '
                'register or cancel'
            )
        return ''
    return 'Hello, World'


# Function to send a sms message.
def __sendReply__(number, message):
    key = 'Your-API-Key'
    secret = 'Your-API-Secret'
    api = OAuth1Session(key, client_secret=secret)
    req = {
        'sender': 'TestService',
        'message': message,
        'recipients': [{'msisdn': number}],
    }
    res = api.post('https://gatewayapi.com/rest/mtsms', json=req)
    res.raise_for_status()


if __name__ == '__main__':
    app.run()
