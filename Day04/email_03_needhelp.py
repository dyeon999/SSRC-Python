'''
다시해봐야해요.
'''

import os
import re
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

def mail_sender(report_file):
    send_email = "dobbidd0@gmail.com"
    send_pwd = "ilzd tius paje anay"
    recv_email = "dobbidd0@gmail.com"

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    