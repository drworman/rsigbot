# Visit https://www.reddit.com/prefs/apps/ to create an application
# for your bot to run as. Set the redirect URL to whatever you want,
# then fill in the blanks below
#
client_id: str = ''
client_secret: str = ''
#
# The username and password for the reddit account you wish to use.
username: str = ''
password: str = ''
#
# Signature texts, supports Reddit markup
default_signature = "***Automatic signature provided by Reddit Signature Bot.***"
#
# Populate the dictionary below with subreddit names for a per-subreddit signature.
# Use a value of None for no signature in a given subreddit.
# Add additional lines as needed.
userSignatures = {
    "subreddit1": "***Automatic signature for r/subreddit1 provided by Reddit Signature Bot.***",
    "subreddit2": None,
}
#
#
# Daemon Mode:
#   True: Run continuously against existing and new submissions and comments
#   False: Run once against your existing submissions and comments, then exit
daemon_mode: bool = False
