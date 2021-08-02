"""
1. Create a twilio account [https://www.twilio.com/login](https://www.twilio.com/login)
2. pip install twilio
"""

from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

call = client.calls.create(twiml='<Response><Say>hello</Say></Response>',
                           to='',
                           from_=''
                           )

print(call.sid)
