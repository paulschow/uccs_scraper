#!/usr/bin/env python

# Scrape grades from my.uccs.edu
# Use with comparefiles.py to check grades
# run with a crontab like this for every 10 minutes
# */10 * * * * cd /home/paul/gradescrape && /home/paul/gradescrape/uccsscraper.py
# */11 * * * * cd /home/paul/gradescrape && /home/paul/gradescrape/comparefiles.$



import bs4
import mechanize
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()

f = open("grades.txt", "w")
print f


# uccs portal login page
br.open("https://portal.prod.cu.edu/psp/epprod/UCCS2/ENTP/h/?tab=CU_STUDENT")

print br.title()

# Select the login form
br.select_form(nr=0)
# Enter username and password
br.form['pf.username'] = 'uccs username'
br.form['pf.pass'] = 'uccs password'
# Click submit to login
br.submit()

# Get past the no JS warning
br.select_form(nr=0)
br.submit()

print br.title()

# XHR request for grades section
br.open("https://portal.prod.cu.edu/psp/epprod/UCCS2/ENTP/h/?cmd="
    "getCachedPglt&pageletname=CU_STUDENT_SCHEDULE&tab"
    "=CU_STUDENT&PORTALPARAM_COMPWIDTH=Narrow&ptlayout=N")


# Put the XHR into beautifulsoup
response = br.response().read()
soup = bs4.BeautifulSoup(response)

# Pick out the section div id='2147-2'
# Which is where my grades are
grades = soup.find('div', id='2147-2')

# If something goes wrong grades will only have the word 'None'
if str(grades) != 'None':
    # Write the grades to a file
    f.write(str(grades))
    print 'Success'
else:
    # This does error checking
    # but I want it to email me anyways
    # so it just writes the file regardless
    f.write(str(grades))
    print 'Error'
