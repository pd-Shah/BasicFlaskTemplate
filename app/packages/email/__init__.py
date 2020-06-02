from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText


class BaseEmailConfig():
    def __init__(self, app):
        self.server = app.config.get('SMTP_SERVER')
        self.sender = app.config.get('SMTP_USERNAME')
        self.username = app.config.get('SMTP_USERNAME')
        self.password = app.config.get('SMTP_PASSWROD')
        self.tls = app.config.get("SMTP_USE_TLS")
        self.port = app.config.get("SMTP_PORT")
        self.source = app.config.get("SOURCE_SERVER_NAME")


class Email(BaseEmailConfig):
    def __init__(self, app=None):
        self.text_subtype = 'plain'
        if app is not None:
            super(Email, self).__init__(app=app)

    def init_app(self, app, ):
        super(Email, self).__init__(app=app)

    def send(self, cls, destination):
        try:
            msg = MIMEText(cls.content, self.text_subtype)
            msg['Subject'] = cls.subject
            msg['From'] = self.sender
            with SMTP(host=self.server) as smtp:
                smtp.set_debuglevel(1)
                smtp.login(self.username, self.password)
                smtp.sendmail(self.sender, destination, msg.as_string())

        except Exception as e:
            print(e)
            print("[-] mail failed; %s" % "CUSTOM_ERROR")
