from bs4 import BeautifulSoup
import requests
from sanitizer import Sanitizer

def print_information(information):
    print('-----------------------')
    for spec in information:
        spec_value = spec.text
        print(spec_value)

def print_trims(trim_info):
    for trim in trim_info:
        print('--------------------')
        trim_text = trim.text
        trim_text_array = trim_text.split('\n')
        for text in trim_text_array:
            if text and \
                            str(text).lower().rstrip() != 'seats' and \
                            str(text).lower() != 'view details' and \
                            str(text).lower() != 'optional engines and transmissions':
                print(str(text).lstrip())

#get input
search = input('search for (enter car year make and model): ')

#clean up info to create query
sanitizer = Sanitizer()
query = sanitizer.sanitize_input(search)

#verify that we received data back, and make a request
if query:
    r = requests.get('http://www.cars.com/research/' + query)
else:
    exit(0)

#parse html response using beautiful soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
soup = BeautifulSoup(r.text, 'html.parser') #get the entire html of the site
specs = soup.findAll('div', {'class': 'mmy-spec'}) #find all list items in the list
other_trims = soup.findAll('div', {'class': 'trim_listing'}) #find other trims

#print info
print_information(specs)
print_trims(other_trims)