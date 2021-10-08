from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingReponse()
    msg = resp.message()
    msg.body('Oi!')
    return str(resp)

if __name__ == '__main__':
    app.run()
