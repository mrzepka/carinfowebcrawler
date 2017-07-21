'''
Class to sanitize/reorder input given to us so that we can form a valid query
to search for in the main python script
'''
class Sanitizer:
    def create_makes_dict(self): #Creates mapping of makes -> what they should be for query
        dict = {}
        f = open('makes.txt', 'r')
        for line in f.readlines():
            line_arr = line.split('/')
            dict[line_arr[0]] = line_arr[1].rstrip() #strip off \n from file line
        return dict

    def __init__(self):
        self.makes_dictionary = self.create_makes_dict()
        self.make_found = False
        self.make = ''
        self.model = ''
        self.year = ''

    def is_make(self, input):
        if input.lower() in self.makes_dictionary.keys():
            return True
        return False


    def is_year(self, input):
        try:
            int(input)
            return True
        except ValueError:
            return False


    def get_make_info(self, input):  # if someone puts in romeo alfa then we need to fix that..
        return self.makes_dictionary[input]

    def verify(self):
        return bool(self.make and self.model and self.year)

    def create_query(self):
        return self.make + '-' + self.model.lstrip().replace(' ', '_') + '-' + self.year

    def sanitize_input(self, input):  # goal is to return something like make_2-model_2-year
        list_of_input = input.split(' ')  # could be a mangled mess of input...
        for item in list_of_input:
            if self.is_make(item):
                if self.make_found:
                    None
                else:
                    self.make = self.get_make_info(item)
                    self.make_found = True
            elif self.is_year(item):
                self.year = self.year + item  # in case someone does something like 1 9 2 3...
            else:
                self.model = self.model + ' ' + item

        if self.verify():
            return self.create_query()
        else:
            print('Could not create valid info from input given')
            return ''