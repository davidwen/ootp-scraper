from loaders.loader import Loader

class DateLoader(Loader):

    CURRENT_DATE = None

    def __init__(self):
        if not DateLoader.CURRENT_DATE:
            DateLoader.CURRENT_DATE = self.get_current_date()    
        self.date = DateLoader.CURRENT_DATE
        Loader.__init__(self)

    def get_current_date(self):
        pass