
import smtplib
import requests

FROMADDRESS = "sender's@gmail.com"
LOGIN    = FROMADDRESS
PASSWORD = "sender's password"
TOADDRESS  = ["Receiver's@gmail.com"]

r = requests.get('https://example.com', timeout=5)

#if responds isnt 200, then your website is down & we should get informed by email
if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587)as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(FROMADDRESS,PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up.'
        msg = f'Subject: {subject}\n\n{body}'


        smtp.sendmail(FROMADDRESS,TOADDRESS,msg)
