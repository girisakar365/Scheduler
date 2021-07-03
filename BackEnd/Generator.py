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

        self.info={}

        self.coordinates()

    def coordinates(self):#manages coordinates 
        
        def gen_coordinates():
            days=[]
            count=0

            gap=((self.days+1)*self.opt)-1 #puts gap between sections

            for i in range((self.days+1)*self.sections):#rows 
                
                if i!= (self.days+1)*count:

                    for j in range(self.periods):#columns
                        
                        if self.periods>=self.brk[0]:

                            if i<=gap and j!=self.brk[0] or i>gap and j!=self.brk[1]:#manage breaks from data base remember to sort them
                                days.append((i,j))

                        else:days.append((i,j))

                else:count+=1
            
            return days

        def sort_coordintes():
            count=0
            
            days=gen_coordinates()

            if self.periods>self.brk[0]:
                end=(self.days*(self.periods-1))
            else:
                end=(self.days*(self.periods))

            for i in range(self.sections): 
                self.row_col[self.shift+str(i+1)]=days[count : end*(i+1)]      
                count+=end

        sort_coordintes()

domy=Generator(11,'Science','Day',sections=18,periods=8,days=6,opt=2)