import smtplib
import ssl
import configparser
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = sys.modules['__main__']
CONFIG = os.path.dirname( app.__file__ ) + '/config.ini'

class sender:
    __FROM__ = None
    __SUBJECT__ = None
    __SERVER__ = None
    __PORT__ = None
    __USER__ = None
    __PSWD__ = None
    __LOG__ = None
    __ulist__ = []


    def __init__(self, test, SUBJECT, type):
        if( test ):
            config = configparser.ConfigParser()
            config.read(CONFIG)
            self.__SERVER__ = config['TEST']['server']
            self.__PORT__ = config['TEST']['port']
            self.__USER__ = config['TEST']['user']
            self.__PSWD__ = config['TEST']['password']
            self.__FROM__ = config['TEST']['from']
            self.__ulist__ = config['TEST']['receivers'].split('\n')
            self.__SUBJECT__ = SUBJECT
        elif( type == 'power' ):
            config = configparser.ConfigParser()
            config.read( CONFIG )
            self.__SERVER__ = config['SMTP']['server']
            self.__PORT__ = config['SMTP']['port']
            self.__USER__ = config['SMTP']['user']
            self.__PSWD__ = config['SMTP']['password']
            self.__FROM__ = config['POWER']['from']
            self.__ulist__ = config['POWER']['receivers'].split('\n')
            self.__SUBJECT__ = SUBJECT
        elif( type == 'speed' ):
            config = configparser.ConfigParser()
            config.read(CONFIG)
            self.__SERVER__ = config['SMTP']['server']
            self.__PORT__ = config['SMTP']['port']
            self.__USER__ = config['SMTP']['user']
            self.__PSWD__ = config['SMTP']['password']
            self.__FROM__ = config['SPEED']['from']
            self.__ulist__ = config['SPEED']['receivers'].split('\n')
            self.__SUBJECT__ = SUBJECT


    def send(self, template):
        message = MIMEMultipart( "alternative" )
        message['Subject'] = self.__SUBJECT__
        message['From'] = self.__FROM__
        message.attach( MIMEText(template, 'html') )

        context = ssl.create_default_context()
        with smtplib.SMTP( self.__SERVER__, self.__PORT__ ) as gsmtp:
            gsmtp.starttls(context=context)
            gsmtp.login( self.__USER__, self.__PSWD__ )

            for TO in self.__ulist__:
                message['To'] = TO
                gsmtp.sendmail(self.__FROM__, TO, message.as_string())
