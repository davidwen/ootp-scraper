from bs4 import BeautifulSoup

class Loader(object):
    
    def __init__(self):
        pass

    def get_soup(self, filename):
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read())