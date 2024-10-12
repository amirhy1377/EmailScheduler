This code is an email scheduling program that automatically sends emails to multiple recipients every day at 9:00 AM. Here's an explanation of the different sections of this code:

1. Importing Libraries:
smtplib: Used for sending emails via SMTP (Simple Mail Transfer Protocol).
email.mime.text.MIMEText and email.mime.multipart.MIMEMultipart: Used to format the email and attach the email body.
schedule: Used for scheduling tasks (in this case, scheduling email sending).
time: Used to create delays in program execution and check the scheduled tasks.



2. Email Settings:
In this section, the information regarding the sender's and recipients' emails is specified:

email_sender: The sender's email (for example, the email address from which the email will be sent).
email_password: The password of the sender's email (for logging into the SMTP server).
email_recipients: A list of email addresses for the recipients.
subject: The subject of the email.
body: The main body of the email that will be sent to the recipients.



3. Email Sending Function (send_email):
This function is responsible for sending the email to the specified recipients.

Connecting to the SMTP Server: First, it connects to the SMTP server (here assumed to be smtp.example.com) on port 587 and uses starttls() to establish a secure connection.

Logging into the Email Account: Using server.login(email_sender, email_password), the program logs into the email server with the provided email and password.

Creating and Sending the Email: For each recipient, an email message is created using MIMEMultipart(), and information like sender, recipient, and subject are added to the email. Then, the email body (through MIMEText(body, 'plain')) is attached to the message and sent using server.sendmail().

Disconnecting from the Server: After sending the emails, the connection to the email server is closed using server.quit().

Error Handling: If an error occurs at any stage, the error is caught by the except block, and the error message is printed.



4. Email Scheduling (schedule.every().day.at("09:00").do(send_email)):
This line of code is responsible for scheduling the email:

Using the schedule library, emails will be sent every day at 9:00 AM. The function send_email() is executed at this specific time.


5. Execution Loop:
schedule.run_pending(): This function checks if it's time to run a scheduled task (in this case, sending the email).
time.sleep(1): Pauses the program for one second to avoid putting too much pressure on the system, and keeps the loop ready to check the scheduled tasks.
Final Output:
The program starts with the message "Email scheduler started..." and will then send emails to the recipients every day at 9:00 AM.

Notes:
You need to replace placeholders like your_email@example.com, your_password, and smtp.example.com with the actual values.
This code is suitable for sending simple emails and can be easily expanded (e.g., adding attachments).


این کد یک برنامه زمان‌بندی ارسال ایمیل است که هر روز در ساعت 9 صبح به صورت خودکار ایمیل‌هایی به چندین گیرنده ارسال می‌کند. در اینجا بخش‌های مختلف این کد را توضیح می‌دهیم:

1. وارد کردن کتابخانه‌ها:
smtplib: برای ارسال ایمیل با استفاده از پروتکل SMTP (Simple Mail Transfer Protocol).
email.mime.text.MIMEText و email.mime.multipart.MIMEMultipart: برای ساختن قالب ایمیل و پیوست کردن متن ایمیل.
schedule: برای زمان‌بندی کارها (در اینجا زمان‌بندی ارسال ایمیل).
time: برای ایجاد تاخیر در اجرای برنامه و بررسی زمان‌بندی‌ها.
2. تنظیمات ایمیل:
در این بخش اطلاعات مربوط به ایمیل فرستنده و گیرنده‌ها مشخص می‌شود:

email_sender: ایمیل فرستنده (به عنوان مثال، آدرس ایمیلی که از آن ایمیل ارسال می‌شود).
email_password: رمز عبور ایمیل فرستنده (برای ورود به سرور SMTP).
email_recipients: یک لیست از آدرس‌های ایمیل گیرندگان.
subject: موضوع ایمیل.
body: متن اصلی ایمیل که به گیرندگان ارسال می‌شود.
3. تابع ارسال ایمیل (send_email):
این تابع مسئول ارسال ایمیل به گیرندگان مشخص شده است.

اتصال به سرور SMTP: ابتدا به سرور SMTP (در اینجا فرضاً smtp.example.com) در پورت 587 وصل می‌شوید و از دستور starttls() برای ایجاد یک اتصال امن استفاده می‌شود.

ورود به حساب ایمیل: با استفاده از server.login(email_sender, email_password)، برنامه با ایمیل و رمز عبور وارد سرور ایمیل می‌شود.

ایجاد و ارسال ایمیل: برای هر گیرنده، یک پیام ایمیل با استفاده از MIMEMultipart() ایجاد شده و اطلاعاتی مانند فرستنده، گیرنده و موضوع به ایمیل اضافه می‌شود. سپس متن ایمیل (از طریق MIMEText(body, 'plain')) به پیام پیوست می‌شود و با server.sendmail() ارسال می‌شود.

قطع اتصال از سرور: پس از ارسال ایمیل‌ها، اتصال از سرور ایمیل قطع می‌شود با server.quit().

مدیریت خطا: اگر در هر مرحله خطایی رخ دهد، آن خطا توسط دستور except گرفته شده و پیام خطا چاپ می‌شود.

4. زمان‌بندی ارسال ایمیل (schedule.every().day.at("09:00").do(send_email)):
این خط کد وظیفه زمان‌بندی را دارد:

با استفاده از کتابخانه schedule، ایمیل‌ها هر روز ساعت 9 صبح ارسال می‌شوند. تابع send_email() در این زمان خاص اجرا می‌شود.
5. حلقه اجرای زمان‌بندی:
schedule.run_pending(): این تابع بررسی می‌کند که آیا زمان اجرای کاری (در اینجا ارسال ایمیل) رسیده است یا خیر.
time.sleep(1): هر یک ثانیه برنامه را متوقف می‌کند تا از فشار زیاد بر روی سیستم جلوگیری شود و همچنین حلقه برای بررسی کارهای برنامه‌ریزی شده آماده باشد.
خروجی نهایی:
برنامه با نمایش پیام "Email scheduler started..." آغاز می‌شود و سپس هر روز رأس ساعت 9 صبح ایمیل‌ها را به گیرندگان ارسال می‌کند.

نکات:
باید جایگزین‌های صحیح برای your_email@example.com, your_password, و smtp.example.com قرار داده شوند.
این کد برای ارسال ایمیل‌های ساده مناسب است و می‌تواند به سادگی گسترش یابد (مثلاً افزودن پیوست).






