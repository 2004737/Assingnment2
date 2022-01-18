def create_message(sender, to, subject, message_text):

  
  message = MIMEText(message_text)
  message['to'] = to 
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())

"""
Above is the way to create message but not the send, for that there would be command below
"To" would be addressed towards the person who is sending the message
"From" is coming from the writer
"Subject" is obligated towards the topic that you would want to talk about
And the next commands fast forwards the data 





"""

def send_message(service, user_id, message):

try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print 'Message Id: %s' % message['id']
    return message
except errors.HttpError, error:
    print 'An error occurred: %s' % error



    """
This would relate towards sending the actual message
"Message" - creates the variables that would be used in the future 
"Print" command highlight the actual message that would be writtem 
"Return " fastforwards the message to the person
And the rest of the code is there to catch and handle message that would be sent back
    """