import praw
import pdb
import re
import os

#Create reddit instance
reddit = praw.Reddit('car_spec_bot')

#make sure we're not replying to old posts by getting posts we've replied to
if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
else:
    #with opens/closes file and handles errors
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = f.read()
        #split on newline
        posts_replied_to = posts_replied_to.split('\n')
        # create list of posts we've replied to, filtering out empty spaces
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search('car_spec_bot_test', submission.title, re.IGNORECASE):
            submission.reply('car spec bot says hi')
            print('replied to: ', submission.title)
            posts_replied_to.append(submission.id)


with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + '\n')