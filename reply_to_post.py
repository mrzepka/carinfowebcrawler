import praw
import re
import os
from main import main
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
for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search('car_spec_bot', comment.body, re.IGNORECASE):
        reply = main(comment.body)
        if reply:
            comment.reply(reply)
            print(reply)
        else:
            comment.reply('To get information, your comment must only contain:\n'
                          '\"car_spec_bot <make> <model> <year>\" (order does not matter')
            print('not found :(')


with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + '\n')