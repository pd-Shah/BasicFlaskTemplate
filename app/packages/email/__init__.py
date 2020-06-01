from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText


class BaseEmailConfig():
    def __init__(self, app):
        self.SMTP_server = app.config.get('SMTP_SERVER')
        self.sender = app.config.get('SMTP_USERNAME')
        self.username = app.config.get('SMTP_USERNAME')
        self.password = app.config.get('SMTP_PASSWROD')


class Email(BaseEmailConfig):
    def __init__(self, app, cls):
        super(Email, self).__init__(app=app)
        self.content = cls.content
        self.subject = cls.subject
        self.text_subtype = 'plain'

    def send(self, destinations):
        try:
            msg = MIMEText(self.content, self.text_subtype)
            msg['Subject'] = self.subject
            msg['From'] = self.sender
            conn = SMTP(self.SMTP_server)
            conn.set_debuglevel(False)
            conn.login(self.username, self.password)
            try:
                conn.sendmail(self.sender, destinations, msg.as_string())
            finally:
                conn.quit()
        except Exception as e:
            print(e)
            print("[-] mail failed; %s" % "CUSTOM_ERROR")
