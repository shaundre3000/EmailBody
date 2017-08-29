def send_html_email(email_body, subject, sender, recipient, cc=None):
    """ Send an html email using smtp server. Only call this when using email tracebacks.
    See models>allocators/teamView.py or
    http://code.activestate.com/recipes/442459-email-pretty-tracebacks-to-yourself-or-someone-you/
    for an example of how to do so

    email_body: html input for your message
    subject: subject line as string
    sender: sender email address as string
    recipient: semicolon delimited string of recipients
    """

    import smtplib
    from bcat import db
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    if cc:
        msg['CC'] = cc

    part = MIMEText(email_body, 'html')

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    user, pw = db.gmail_login()
    server.login(user, pw)
    server.sendmail(sender, recipient.split(';'), msg.as_string())
    server.close()

