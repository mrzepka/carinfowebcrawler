'''
    Contains main function that executes webcrawling of cars.com
    Returns the string to be used in the reply to the message received
'''
from bs4 import BeautifulSoup
import requests
from sanitizer import Sanitizer

def print_information(information):
    '''prints out base information for make model year'''
    output = ''
    # output = output + '-----------------------\n'
    for spec in information:
        spec_value = spec.text
        output = output + spec_value + '\n\n'
    return output

def print_trims(trim_info):
    '''returns information on all trims for make/model/year'''
    output = ''
    for trim in trim_info:
        output = output + '--------------------\n'
        trim_text = trim.text
        trim_text_array = trim_text.split('\n')
        for text in trim_text_array:
            if text and \
                            str(text).lower().rstrip() != 'seats' and \
                            str(text).lower() != 'view details' and \
                            str(text).lower() != 'optional engines and transmissions':
                output = output + text.lstrip() + '\n\n'
    return output

def main(search):
    '''
        executes serach for car using make-model-year and cars.com
        params: search is the reddit message/comment body that should
            contain the make model year information that we would like to
            look up
    '''
    search = search.lower()
    #clean up info to create query
    output = ''
    sanitizer = Sanitizer()
    query = sanitizer.sanitize_input(search)

    #verify that we received data back, and make a request
    if query:
        print('making request with', query)
        req = requests.get('http://www.cars.com/research/' + query)
    else:
        return output

    #parse html response using beautiful soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    soup = BeautifulSoup(req.text, 'html.parser') #get the entire html of the site
    specs = soup.findAll('div', {'class': 'mmy-spec'}) #find all list items in the list
    other_trims = soup.findAll('div', {'class': 'trim_listing'}) #find other trims

    #print info
    if bool(specs) or bool(other_trims):
        output = output + print_information(specs)
        output = output + '\n\n---\n\n '\
        'in order to not be annoying I am not printing all trims!'
        # output = output + print_trims(other_trims, output)
    return output
