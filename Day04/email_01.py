import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Send email alert

load_dotenv()
send_email = os.getenv("EMAIL_ID")
send_pwd = os.getenv("EMAIL_PW")
recv_email = "97dmstjs2@gmail.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587                           

text = "반가워요 은선님!!"

msg = MIMEText(text, 'plain', 'utf-8') 
msg['Subject'] = "메일 제목 입력"  
msg['From'] = send_email          
msg['To'] = recv_email            

email_string = msg.as_string()
print(email_string)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, email_string)
s.quit()
print("Email SUCCESS")