from random import *
from Allocation import Allocate

# NOTE: Algorithum does not hold validation for less than five classes.

class Generator(Allocate):

    def __init__(self, cls: int,faculty:str,shift:str,sections:int,periods:int,days: int,opt:int):
        super().__init__(cls, faculty, shift, sections, periods, days, opt)

        self.__iter__()

    def __iter__(self):
        
        for i in self.subject_section:

            for j in self.subject_section[i]:
                print(i)
                self.__next__(j)

    def __next__(self, sections: list):
        
        coordintes = []

        avoide_rows = None
        
        condition = True

        for i in sections: 

            print(choice( self.row_col[i] ))

domy_data = (11, 'Science', 'Day', 18, 7, 6, 2)

domy = Generator(*domy_data)