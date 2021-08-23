from random import * 
from database import *
from Coordinates import Coordinates

class Allocate(Coordinates):

    def __init__(self, cls: int,faculty:str,shift:str,sections:int,periods:int,days: int,opt:int):
        super().__init__(cls, faculty, shift, sections, periods, days, opt)


        self.subject={ i:[j[0] for j in DB.fetch(table = i)]#unit of subject 
        
        for i in {i[0] for i in DB.fetch(table='Professor',typ = 'specific',col = 'Subject')}#subject set
        }

        self.teacher = {i:[] for i in self.subject}

        self.sections = [i for i in self.row_col]

        self.subject_teacher = {}
        
        self.subject_section = {}

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

                        else: break # End if section list is empty

                    section = [sec for sec in self.row_col]

                    try: self.manage_data(self.subject[i][j], teacher, stored_section) # sending data to sort function
                    
                    except Exception: pass

                    stored_section.clear()
                    
    def manage_data(self,*args):
        unit, teacher, section = args 
        self.subject_teacher[unit] = tuple(teacher)  # sorting data to main dict
        self.subject_section[unit] = tuple(section)  # sorting data to main dict