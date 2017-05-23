from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account = "hash_id_left_blank_for_security"
# Your Auth Token from twilio.com/console
token = "id_left_blank_for_security"
client = TwilioRestClient(account, token)

message = client.messages.create(to="+15550554549", from_="+14085550545",
    body="Hello from Python!")



print(message.sid)
