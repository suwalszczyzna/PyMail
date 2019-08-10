# -*- coding: utf-8 -*-

import argparse
from EmailServer import EmailServer
import config

parser = argparse.ArgumentParser(prog='pyMail')
parser.add_argument('-i', '--input', action='store_true',
                    help='Allows you to input required values into program, not in command line')
parser.add_argument('-e', '--email', action='store', type=str, help='email address of receiver')
parser.add_argument('-s', '--subject', action='store', type=str, help='subject of your email')
parser.add_argument('-m', '--message', action='store', type=str, help='message')
args = parser.parse_args()

if not args.input:
    email_receiver = args.email
    subject = args.subject
    message = args.message
    if any(arg is None for key, arg in vars(args).items()):
        can_be_send = False
        print('Program cannot run. Email address, subject or message is missing. Type -h for help')
    else:
        can_be_send = True

else:
    email_receiver = input('To [email]: ')
    subject = input('Subject: ')
    message = input('Message: ')
    can_be_send = True

if can_be_send:
    pymail = EmailServer(config.smtp_server,
                         config.smtp_port,
                         config.sender_email,
                         config.password)
    pymail.send_email(email_receiver, subject, message)
