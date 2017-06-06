from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account = "your_SID"
# Your Auth Token from twilio.com/console
token = "your_token"
client = TwilioRestClient(account, token)

message = client.messages.create(to="+your_number", from_="+other_number",
    body="Hello from Python!")



print(message.sid)
