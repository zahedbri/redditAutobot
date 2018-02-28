# redditautobot

A python reddit bot that has numerous functionality include posting a comment, replying to a comment,
gathering data, comment scraping, and liking comments.  This program can build up 'bots' reputations by
posting replies with a cronjob.  It can also help like or promote a post with the bots reputation.



### Prerequisites

python3
Mysql- if you want to use a different database then you must update the models/config file
Reddit bot- Create a reddit account and activate it under script.  Copy and past the info into your database. More bots
the better


### Installing

Using a virtualenv:
virtualenv venv -p python3
source/venv/bin/activate
pip3 install -r requirements.txt --no-cache
add your username,password to config file for database
add bots names to database

In order to run hassassub.py, you must enter a username and credentials in the python file

### How to run

To msg or upvote
python3 upvotecomment.py
python3 writecomment.py

#these are run under a cron. I run them every 12 hours ..
/path/to/your/cron/python harassasub.py # make sure you got a username added to the file.  Most likely username be banned so be cautious
/path/to/your/cron/python randomcomment.py

### Future Goals

Make comments over tor to help avoid bans. Provide anonymous commenting.
Praw proxy needed.


## Contributing

Feel free to fork on contribute

## Authors

* **Anekdotin




