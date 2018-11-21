# -*- coding: utf-8 -*-
import poplib
import string
import random
import StringIO, rfc822
import logging


class Mail:
    SERVER = "pop.gmail.com"
    USER = "*"
    PASSWORD = "*"
    logging.debug('connecting to ' + SERVER)
    server = poplib.POP3_SSL(SERVER)
    # login
    logging.debug('logging in')
    server.user(USER)
    server.pass_(PASSWORD)
    # list items on server
    logging.debug('listing emails')
    resp, items, octets = server.list()
    # download the first message in the list
    id, size = string.split(items[-1])
    resp, text, octets = server.retr(id)
    # convert list to Message object
    text = string.join(text, "\n")
    file = StringIO.StringIO(text)
    message = rfc822.Message(file)
    email = ''

    # sorting mails
    if (message['From'] == '*'):
        email = (message['Subject'])
    #    print(message['From']),
    #    print(message['Date']),
    # print(message.fp.read())
