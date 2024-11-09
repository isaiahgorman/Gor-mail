import smtplib

sender = "hello@demomailtrap.com"
receiver = "isaiahgorman090203@gmail.com"
subject = input("Subject: ")
response = input("Enter Your Message: ")

message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}

{response}"""

with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "d8845204fc853b0784e1f0202e80eebb")
    server.sendmail(sender, receiver, message)