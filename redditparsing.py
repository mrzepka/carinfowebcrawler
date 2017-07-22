import praw

reddit = praw.Reddit('car_spec_bot')
subreddit = reddit.subreddit('cars')

for submission in subreddit.hot(limit=5):
    print('Title: ', submission.title)
    print('Text : ', submission.selftext)
    print('Score: ', submission.score)
    print('------------------------------\n')