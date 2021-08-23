from random import *
from math import log

class Coordinates:

    def __init__(self,cls:int,faculty:str,shift:str,
    sections:int,periods:int,days:int,opt:int):
        
        self.CLASS = cls
        self.FACULTY = faculty
        self.SHIFT = shift[0]
        self.SECTIONS = sections
        self.PERIODS = periods
        self.DAYS = days
        self.OPT = opt
        self.BREAKS = (3,4)
        
        self.row_col = {}

        self.lab_dict = {}

        self.coordinates()

    def coordinates(self):#manages coordinates 
        
        if self.BREAKS[0] < self.BREAKS[1]:
            min, max = self.BREAKS[0], self.BREAKS[1]
        else:
            min, max = self.BREAKS[1], self.BREAKS[0]

        def gen_coordinates():
            days = []
            count = 0

            gap = ((self.DAYS + 1) * self.OPT) - 1 #puts gap between sections

            for i in range((self.DAYS + 1) * self.SECTIONS):#rows 
                
                if i != (self.DAYS + 1) * count:

                    for j in range(self.PERIODS):#columns
                        
                        if self.PERIODS >= min:

                            if i <= gap and j != max or i > gap and j != min:#manage breaks from data base remember to sort them
                                days.append((i, j))

                        else:days.append((i, j))

                else: count += 1
            
            return days

        def sort_coordintes():
            count=0
            
            days=gen_coordinates()

            if self.PERIODS > min: end = (self.DAYS * (self.PERIODS - 1))
            
            else: end = (self.DAYS * (self.PERIODS))

            for i in range(self.SECTIONS): 
                self.row_col[self.SHIFT + str(i + 1)] = days[count : end * (i + 1)]      
                count += end

        sort_coordintes()

        def lab_coordinates():
            lcord = []

            checklist = [i for i in range(self.PERIODS) if i % 2 != 0]#check list / break list
            
            if self.PERIODS % 2 != 0: checklist.append(self.PERIODS - 1)

            for i in range(self.SECTIONS):#making list of [i,list.index(i)+1]
                
                for j in self.row_col[self.SHIFT + str(i + 1)]:
                    try:
                        
                        if self.faculty == 'Science' and i > min: checklist.append(2)
                        
                        if j[1] not in checklist:
                            lcord.append([j, self.row_col[self.SHIFT + str(i + 1)]
                                [self.row_col[self.SHIFT + str(i + 1)].index(j) + 1]
                                ])

                    except Exception:
                       continue
            count = 0
            for i in range(self.SECTIONS):
                var = lcord[count : self.DAYS * int(log(self.PERIODS, 2)) * (i + 1)]
                self.lab_dict[self.SHIFT + str(i + 1)] = var
                count += self.DAYS * int(log(self.PERIODS, 2))
        
        lab_coordinates()