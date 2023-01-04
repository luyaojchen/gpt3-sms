from twilio.rest import Client
import os

account_sid = os.getenv("ACCOUNT_SID")
auth_token  = os.getenv("AUTH_TOKEN")
gpt_num = os.getenv("GPT_NUMBER")
my_num = os.getenv("PERSONAL_NUMBER")

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=my_num, 
    from_=gpt_num,
    body="hello!")

print(message.sid)