import smtplib
from email.message import EmailMessage

sender_email = input("Enter your email address: ")
receiver_email = input("Enter recipient's email address: ")
password = input("Enter your email password: ")

msg = EmailMessage()
msg['Subject'] = 'nari mukti Songothon'
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content('nesha nari tas tile tile kore sorbo nash')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.send_message(msg)