class MessageToSend:
    text="no Text";
    recipent=""
def send_email(user, pwd, recipient, subject, body):
    import smtplib
    print("sending mail to {} with body {}".format(recipient,body))
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    # TO = recipient if type(recipient) is list else [recipient]
    TO = recipient

    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
        print("message")
        print(body)
    except Exception as e:
        print (e);
        print ("failed to send mail")

def createMessage(statusConnection,usersInfo):
    recipent="unknown@ss.cl"
    if statusConnection.st==1 :
        connectionAccion="Se ha conectado"

    else :
        if statusConnection.st==2:
            connectionAccion="se Ha desconectado"
    for userInfo in usersInfo:
        if userInfo.id==statusConnection.id:
            recipent=userInfo.email
            name=userInfo.nombre
    messageToSend=MessageToSend()
    text="{}  {}".format(name,connectionAccion)
    messageToSend.text=text
    messageToSend.recipent=recipent
    return messageToSend;