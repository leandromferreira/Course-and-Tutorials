import smtplib

host = "smtp.gmail.com"
port = 587
username = "email@gmail.com"
password = "PASSWORD"
from_email = username
to_list = ["email@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "<b>Hello</b><br/> there this is an email message")
email_conn.quit()
