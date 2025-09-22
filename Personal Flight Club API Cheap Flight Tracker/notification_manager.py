import smtplib
from twilio.rest import Client

TWILIO_SID = SECRET_SID #twilio
TWILIO_AUTH_TOKEN = SECRET_AUTO_TOKEN #twilio
TWILIO_VIRTUAL_NUMBER = SECRET_NR
VERIFIED_RECIVER_NUMBER = SECRET_NR_RECIVE

MY_EMAIL = GMAIL_TEST
PASSWORD = P_ENV

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=VERIFIED_RECIVER_NUMBER,
        )
        print(f"Low price message sent with sid: {message.sid}")

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
            print(f"Low price message sent to: {len(emails)} emails.")
