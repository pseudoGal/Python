#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on mon jan  25 22:04:10 2021

@author: pratiksha

"""

import smtplib

FROMADDR = "sender's_gmail_id"
LOGIN    = FROMADDR
PASSWORD = "your_password"
TOADDRS  = ["receivers_address"]
#TOADDRS  = ["yourid@gmail.com"]

SUBJECT  = "Test"

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += " Wellcome to our website!!!\r\n"
#25,587,465
server = smtplib.SMTP('smtp.gmail.com',587 )
server.set_debuglevel(1)
server.ehlo()

server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()

