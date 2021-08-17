from random import *
from math import log
from database import *

# NOTE: Algorithum does not hold validation for less than five classes.

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


class Allocate(Coordinates):

    def __init__(self, cls: int,faculty:str,shift:str,sections:int,periods:int,days: int,opt:int):
        super().__init__(cls, faculty, shift, sections, periods, days, opt)


        self.subject={ i:[j[0] for j in DB.fetch(table = i)]#unit of subject 
        
        for i in {i[0] for i in DB.fetch(table='Professor',typ = 'specific',col = 'Subject')}#subject set
        }

        self.teacher = {i:[] for i in self.subject}

        self.sections = [i for i in self.row_col]

        self.data = {}

        self.sort_teacher()
        self.merge_data()

    def sort_teacher(self):
        
        for j in self.subject:

            for i in DB.fetch('Professor','quiere','id',f'Subject = "{j}" AND Class = "{self.CLASS}"'):

                if len(self.teacher[j]) < self.SECTIONS: self.teacher[j].append(i[0])
                
            if len(self.teacher[j]) < self.SECTIONS:

                for i in DB.fetch('Professor','quiere','id',f'Class = "both" AND Subject="{j}"'):

                    if len(self.teacher[j]) < self.SECTIONS: self.teacher[j].append(i[0])
                
    def merge_data(self):

        section = self.sections

        stored_section = []

        for i in self.teacher: # specifies required teacher for each unit in each classroom
            
            current_teacher = self.teacher[i]
            
            current_subject = self.subject[i]

            TEACHERS_PER_UNIT = round( len(current_teacher) / len(current_subject) )

            if len(current_subject) > len(current_teacher): TEACHERS_PER_UNIT = len(current_teacher)

            SECTIONS_PER_TEACHER = round( self.SECTIONS / TEACHERS_PER_UNIT)

            for j in range( round( len(current_teacher) / TEACHERS_PER_UNIT) ): # filters teachers

                if len(current_teacher) >= TEACHERS_PER_UNIT: # Handeling population error (ValueError)

                    teacher = sample(current_teacher, k = TEACHERS_PER_UNIT)

                    # removing used teachers from current_teacher list
                    for choosen in teacher: current_teacher.pop( current_teacher.index(choosen) )

                    for k in range(self.SECTIONS): # Distribute Sections

                        if len(section) >= SECTIONS_PER_TEACHER and len(teacher) != len(stored_section): 
                            # Handeling population error (ValueError) and equal divison errors     

                            random_section = sample( section, k = SECTIONS_PER_TEACHER)

                            stored_section.append(random_section)

                            # removing used sections from section list:
                            for choosen in random_section: section.pop( section.index( choosen ))

                        elif len(section) != 0: # Handle left over sections
                            
                            for k in section:

                                index = randint(0, len(stored_section) - 1)

                                stored_section[index].append(k)

                                section.pop( section.index(k) )

                        else: break # End if setion list is empty

                    section = [sec for sec in self.row_col]

                    try: self.manage_data(self.subject[i][j], teacher, stored_section) # sending data to sort function
                    
                    except Exception: pass

                    stored_section.clear()
                    
    def manage_data(self,*args):
        unit, teacher, section = args 
        self.data[unit] = [tuple(teacher), tuple(section)]  # sorting data to main dict