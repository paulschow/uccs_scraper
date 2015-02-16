# uccs_scraper
Small script I wrote to escape grades from the UCCS peoplesoft website, and and accompanying script to email if they change.

The main script is uccsscraper.py. It goes to my.uccs.edu, logs in, finds your grades, and saves them to a file called grades.txt.


The comparefiles.py looks at the file and compares it to a file called nogrades.txt. 
If they are different, it sends out an email containing grades.txt. 
Then it deletes nogrades.txt and renames grades.txt to nogrades.txt.

I set this up in cron for every 10 minutes, that was probably overkill.

You'll probably have to hunt around each semester to find the new div_id for that semesters' grades. 
Should be easy with any modern browser and the element inspector.
