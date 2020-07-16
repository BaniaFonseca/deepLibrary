from django.db import models

class ElectronicDocument:

    def __init__(self):
        self.type = 'book'
        self.title = 'introduction to algorithms'
        self.authors = ['T H O M A S H. C O R M E N', 'C H A R L E S E. L E I S E R S O N', 
                        'R O N A L D L. R I V E S T', 'C L I F F O R D STEIN']

