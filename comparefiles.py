#!/usr/bin/env python

# Compare two scraped grade text files from UCCS
# and send an email if they are different
# use with uccsscraper.py

import filecmp
import smtplib
import os
from time import strftime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

try:
    # Compare grade files
    status = filecmp.cmp('nogrades.txt', 'grades.txt')
    print status
except OSError:
    print 'File not found'
    status = True

if status is False:
    ### Send email
    fromaddr = "from address"
    toaddr = "to address"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Grades Changed!"

    #body = "One of your grades has changed on my.uccs.edu"
    grades = open('grades.txt')
    body = str(grades.read())
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("gmail usename", "gmail password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    # Rename the old file to the day and time
    os.rename('nogrades.txt', strftime("%d:%H:%M:%S.txt"))
    # Rename the new file to the old file
    os.rename('grades.txt', 'nogrades.txt')

elif status is True:
    print 'They are the same'

else:
    print 'Error'
