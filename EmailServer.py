import smtplib
import config as config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def prepare_result_message(subject: str, message: str) -> str:
    msg = MIMEMultipart('alternative')
    charset = 'utf-8'
    msg.set_charset(charset)
    body_string = message
    msg['Subject'] = Header(subject, charset)
    _attach = MIMEText(body_string.encode(charset), 'html', 'UTF-8')
    msg.attach(_attach)
    return msg.as_string()


class EmailServer:
    def __init__(self, smtp_host, port, sender_email, password):
        self.smtp_host = smtp_host
        self.port = port
        self.sender_email = sender_email
        self.password = password
        self.server = smtplib.SMTP(config.smtp_server, config.smtp_port)

    def _login(self):
        self.server.login(self.sender_email, self.password)
        print('Login success')

    def send_email(self, rec_email, subject, message):
        try:
            print(f'Email will send from: \"{config.sender_email}\"')
            self.server.ehlo()
            self.server.starttls()
            self._login()
            result_message = prepare_result_message(subject, message)
            _result = self.server.sendmail(self.sender_email, rec_email, result_message)
            print('Sending message...')
            self.server.quit()
            print('Server connection has been closed')
            print('Success!')
        except Exception as e:
            print('Something goes wrong:')
            print(repr(e))
