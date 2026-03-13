import smtplib

def send_email():

    sender = "your_email@example.com"
    receiver = "receiver@example.com"
    message = "Subject: Test Email\n\nThis is an automated email."

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, "your_password")
        server.sendmail(sender, receiver, message)

    print("Email sent successfully")

if __name__ == "__main__":
    send_email()
