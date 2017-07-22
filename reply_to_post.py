import praw
import re
import os
from main import main
#Create reddit instance
reddit = praw.Reddit('car_spec_bot')

def process_comment(comment):
    # print('searching, comment: ', comment.body)
    if re.search('/u/car_spec_bot', comment.body, re.IGNORECASE):
        print('------found a request!')
        reply = main(comment.body.replace('/u/car_spec_bot', ''))
        if reply:
            comment.reply(reply)
            print(reply)
        else:
            comment.reply('To get information, your comment must only contain:\n'
                          '\"/u/-car_spec_bot <make> <model> <year>\" (remove the -, order does not matter)\n'
                          'you will need to make a new comment, I do not go back and check edited comments')
            print('not found :(')

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
    if comment.id not in posts_replied_to:
        process_comment(comment)
        print(comment.id, 'replied to:', comment.body)
        posts_replied_to.append(comment.id)
        with open('posts_replied_to.txt', 'w') as f:
            print('writing to posts we\'ve replied to')
            for post_id in posts_replied_to:
                f.write(post_id + '\n')


