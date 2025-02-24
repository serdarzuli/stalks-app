import smtplib
from .config import SENDER_EMAIL, SENDER_EMAIL_PASSWORD

def send_mail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
    
    # message to be sent
    message = "HI Serdar this a Test!"
    
    # s.sendmail("sender_email_id", "receiver_email_id", message)
    s.sendmail(SENDER_EMAIL, SENDER_EMAIL, message)
    s.quit()
