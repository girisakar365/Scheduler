from random import *
from math import e, log
from main import *

class Coordinates:

    def __init__(self,cls:int,faculty:str,shift:str,
    sections:int,periods:int,days:int,opt:int):
        
        self.cls = cls
        self.faculty=faculty
        self.shift=shift[0]
        self.sections=sections
        self.periods=periods
        self.days=days
        self.opt=opt
        self.brk=(3,4)
        
        self.row_col={}

        self.lab_dict={}

        self.coordinates()

    def coordinates(self):#manages coordinates 
        
        if self.brk[0]<self.brk[1]:
            min,max=self.brk[0],self.brk[1]
        else:
            min,max=self.brk[1],self.brk[0]

        def gen_coordinates():
            days=[]
            count=0

            gap=((self.days+1)*self.opt)-1 #puts gap between sections

            for i in range((self.days+1)*self.sections):#rows 
                
                if i!= (self.days+1)*count:

                    for j in range(self.periods):#columns
                        
                        if self.periods>=min:

                            if i<=gap and j!=max or i>gap and j!=min:#manage breaks from data base remember to sort them
                                days.append((i,j))

                        else:days.append((i,j))

                else:count+=1
            
            return days

        def sort_coordintes():
            count=0
            
            days=gen_coordinates()

            if self.periods>min:
                end=(self.days*(self.periods-1))
            else:
                end=(self.days*(self.periods))

            for i in range(self.sections): 
                self.row_col[self.shift+str(i+1)]=days[count : end*(i+1)]      
                count+=end

        sort_coordintes()

        def lab_coordinates():
            lcord=[]

            checklist=[i for i in range(self.periods) if i%2!=0]#check list / break list
            if self.periods%2!=0:
                checklist.append(self.periods-1)

            for i in range(self.sections):#making list of [i,list.index(i)+1]
                
                for j in self.row_col[self.shift+str(i+1)]:
                    try:
                        
                        if self.faculty=='Science' and i>min:
                            checklist.append(2)
                        
                        if j[1] not in checklist:
                            lcord.append([j , self.row_col[self.shift+str(i+1)]
                                [self.row_col[self.shift+str(i+1)].index(j)+1]
                                ])

                    except Exception:
                       continue
            count=0
            for i in range( self.sections ):
                var=lcord[count : self.days * int(log(self.periods,2))*(i+1)]
                self.lab_dict[self.shift+str(i+1)]=var
                count+= self.days * int(log(self.periods,2))
        
        lab_coordinates()

class Data_Center(Coordinates):

    def __init__(self, cls: int,faculty:str,shift:str,sections:int,periods:int,days: int,opt:int):
        super().__init__(cls, faculty, shift, sections, periods, days, opt)


        self.subject={ i:[j[0] for j in DB.fetch(table=i)]#unit of subject 
        
        for i in {i[0] for i in DB.fetch(table='Professor',typ='specific',col='Subject')}#subject set
        }

        self.info={i:[] for i in self.subject}

        self._sections=[i for i in self.row_col]

        self.data={i:[] for i in self.subject}

        self.sort_teacher()
        self.sort_data()

    def sort_teacher(self):
        
        for j in self.subject:
            for i in DB.fetch('Professor','quiere','id',f'Subject = "{j}" AND Class = "{self.cls}"'):
                if len(self.info[j])<self.sections:
                    self.info[j].append(i[0])
                
            if len(self.info[j])<self.sections:
                for i in DB.fetch('Professor','quiere','id',f'Class = "both" AND Subject="{j}"'):
                    if len(self.info[j])<self.sections:
                        self.info[j].append(i[0])

    def sort_data(self):

        for i in self.info:
            TOTAL=len(self.info[i])

            while len(self.info[i])!=0:
                teacher=choice(self.info[i])

                _section=[]                
                try:
                    for sec in range( int( round (self.sections/TOTAL ,0) ) ):
                        
                        section=choice(self._sections)
                        _section.append(section)
                        self._sections.remove(section)

                except Exception:
                    self.info[i].remove(teacher)

                else:
                    self.info[i].remove(teacher)
                    self.data[i].append(teacher)
                    self.data[i].append(tuple(_section))

            else:
                self._sections=[i for i in self.row_col]
                
domy=Data_Center(11,'Science','Day',18,7,6,2)