import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# تنظیمات ایمیل
email_sender = 'your_email@example.com'
email_password = 'your_password'
email_recipients = ['recipient1@example.com', 'recipient2@example.com']
subject = 'Subject of the email'
body = 'This is the body of the email.'

# تابع ارسال ایمیل
def send_email():
    try:
        # اتصال به سرور SMTP
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(email_sender, email_password)

        for recipient in email_recipients:
            # ایجاد پیام ایمیل
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # ارسال ایمیل
            server.sendmail(email_sender, recipient, msg.as_string())
            print(f'Email sent to {recipient}')

        # قطع اتصال از سرور
        server.quit()
    except Exception as e:
        print(f'Error: {e}')

# زمان‌بندی ارسال ایمیل
schedule.every().day.at("09:00").do(send_email)  # ارسال هر روز ساعت 9 صبح

print("Email scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(1)
