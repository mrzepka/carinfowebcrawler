'''
Class to sanitize/reorder input given to us so that we can form a valid query
to search for in the main python script
'''

def create_makes_dict():
    '''Creates mapping of makes -> what they should be for query'''
    makes = {}
    with open('makes.txt', 'r') as makesfile:
        for line in makesfile.readlines():
            line_arr = line.split('/')
            makes[line_arr[0]] = line_arr[1].rstrip() #strip off \n from file line
    return makes

def is_make(text, makes):
    '''returns true if text is defined in the makes dictionary'''
    if text.lower() in makes.keys():
        return True
    return False

def is_year(text):
    '''returns true if the text is a number to be used as a year'''
    try:
        int(text)
        return True
    except ValueError:
        return False

def get_base_query(message):
    '''
        Pulls out everything after /u/car_spec_bot in the message
        params: message is the comment/message body from reddit inbox
    '''
    bodylist = message.split(' ')
    indexofquery = bodylist.index('/u/car_spec_bot')
    return bodylist[indexofquery + 1:]

class Sanitizer:
    '''
        Sanitizer class that takes in input and cleans it up to create
        a query. The query created will be used in the webcrawler to
        create the URL that we will be pulling data from.
    '''
    def __init__(self):
        self.makes_dictionary = create_makes_dict()
        self.make_found = False
        self.make = ''
        self.model = ''
        self.year = ''

    def get_make_info(self, text):
        '''returns information about a make. Uses dictionary to match
            partial words, abbreviations, and a few misspellings into
            actual makes that can be used in the query
        '''
        return self.makes_dictionary[text]

    def verify(self):
        '''Make sure everything is initialized'''
        return bool(self.make and self.model and self.year)

    def create_query(self):
        '''return the string that will be used in the query'''
        if self.verify():
            return self.make + '-' + self.model.lstrip().replace(' ', '_')\
                 + '-' + self.year

    def sanitize_input(self, text):
        '''
            essentially the "main" of this class. begins sanitation of input
            params: text given is comment body from reddit message/comment
        '''
        list_of_input = get_base_query(text)
        for item in list_of_input:
            if is_make(item, self.makes_dictionary):
                if not self.make_found:
                    self.make = self.get_make_info(item)
                    self.make_found = True
            elif is_year(item):
                self.year = self.year + item  # in case someone does something like 1 9 2 3...
            else:
                self.model = self.model + ' ' + item

        return self.create_query()
