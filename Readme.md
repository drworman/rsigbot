Reddit Signature Bot
------------
Reddit Signature Bot is a bot for Reddit written in Python.

This particular bot will iterate over your entire post history and apply a user
defined signature line to every text post and comment in your post history.


Features & Behavior
------------
The default behavior is to run once against your entire post history,
however there is also a daemon mode for constantly scanning your post
history and applying the signature as you make new posts and replies.

Supports variable signatures on a per-subreddit basis, or exclusion
of specific subreddits from receiving an automatic signature.


Requirements
------------
- Python >=3.6.5 
	- Modules:
		- praw

    If you need help with this, Google is your friend.


Configuration
------------
**You must configure Reddit Signature Bot for your own usage:**

- Configure rsigbotcfg.py as desired


Running The Bot
------------
Make sure that `rsigbot` is executable.

CD into the directory where you have cloned the repo or add that directory to your $PATH, then:

`./rsigbot &`

OR

set a cron job to run the **rsigbot_cronjob.sh** BASH script.
