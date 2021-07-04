from random import *
from math import log

class Generator:

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

        self.info={}

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