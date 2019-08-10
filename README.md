# PyMail
Simple python command line script made as module for my other project. 
I've used [argparse](https://docs.python.org/3/library/argparse.html) library to make a [CLI](https://realpython.com/command-line-interfaces-python-argparse/), and [smtplib](https://docs.python.org/3/library/smtplib.html) to send emails.
### Getting started
First of all you should fill in some variables in **config.py** file, line an your email address, password, smtp host and port:
```python
sender_email = "your.amazing@email.address"
password = "R3aIIy5trongPswd"
smtp_server = 'smtp.gmail.com'
smtp_port = 587
```

##### Run PyMail
PyMail you can run in your terminal or command line. There is two options.
###### 1. Run as a script 
By filling all required parameters, example:
```
python pylib.py -e 'myFriends@email.com' -s 'PyMail message' -m 'Hi there! I'm message from python!'

Warning: If you are using Windows OS, please, run this in PowerShell. 
For some reason default CMD in Windows has a problem with multi-words arguments.

```

###### 2. Run with inputs in console program
By run with `-i` flag, and type all required values, example:
```
python pylib.py -i
```

_Example of running program:_
```
To [email]: myFriends@email.com
Subject: PyMail message
Message: Hi there! I'm message from python!
```
