from os.path import (
    abspath,
    dirname,
    join
)
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from jinja2 import (
    FileSystemLoader,
    Environment,
)


class BaseEmailConfig():
    def __init__(self, app):
        self.server = app.config.get('SMTP_SERVER')
        self.sender = app.config.get('SMTP_USERNAME')
        self.username = app.config.get('SMTP_USERNAME')
        self.password = app.config.get('SMTP_PASSWROD')
        self.tls = app.config.get("SMTP_USE_TLS")
        self.port = app.config.get("SMTP_PORT")
        self.source = app.config.get("SERVER_NAME")


class Email(BaseEmailConfig):
    def __init__(self, app=None):
        self.text_subtype = 'html'
        if app is not None:
            super(Email, self).__init__(app=app)

    def init_app(self, app, ):
        super(Email, self).__init__(app=app)

    def send(self, html_template_name, subject, destination, debuglevel=0, **kwargs):
        template_loader = FileSystemLoader(searchpath=join(abspath(dirname(__file__)), 'templates/'))
        template_env = Environment(loader=template_loader)
        template = template_env.get_template(html_template_name)
        template = template.render(**kwargs)

        try:
            msg = MIMEText(template, self.text_subtype)
            msg['Subject'] = subject
            msg['From'] = self.sender
            with SMTP(host=self.server) as smtp:
                smtp.set_debuglevel(debuglevel)
                smtp.login(self.username, self.password)
                smtp.sendmail(self.sender, destination, msg.as_string())
        except Exception as e:
            print("[-] mail failed; %s" % e)
