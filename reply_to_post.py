'''
    This python script is called to handle reddit API calls and replying to
    messages sent to the bot.
'''
import re
import praw
from main import main

def process_comment(message):
    '''
        Processes whatever message is sent to the bot
    '''
    if re.search('/u/car_spec_bot', message.body, re.IGNORECASE):
        print('------found a request!', message.body)
        reply = main(message.body)
        if reply:
            message.reply(reply)
        else:
            message.reply('To get information, your comment must only contain:'
                          '\"/u/-car_spec_bot <make> <model> <year>\"'
                          '(remove the -, order does not matter)'
                          'you will need to make a new comment, I do not go back'
                          ' and check edited comments.'
                          'Some issues persist, for example you may need to say '
                          '\'fr_s\' instead of frs or fr-s.'
                          'I\'m working on this in my free time, but please '
                          'direct message me with suggestions/bugs')
            print('not found :(')
def start():
    '''
        Function called to start processing
    '''
    reddit = praw.Reddit('car_spec_bot')
    for item in reddit.inbox.unread(limit=None):
        print('trying to reply to ', item.author)
        process_comment(item)
        item.mark_read()
start()
