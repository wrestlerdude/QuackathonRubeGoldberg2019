from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC0c2725100c71d488ac82e6f23c868caf'
auth_token = '5d4111ca006788f69fe1d2dee8c969fb'
client = Client(account_sid, auth_token)

string = raw_input("Please Input string: ")
string2 = raw_input("Please Input string: ")

# send a Whatsapp
message = client.messages.create(
                              body= string,
                              from_='+447447741765',
                              to='+447999560777'
                          )

# send an SMS
message2 = client.messages.create(
                              body= string2,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+34658764781'
                          )

print(message.sid)
print(message2.sid)
