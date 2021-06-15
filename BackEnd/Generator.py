from random import * 
from math import log
from typing import get_origin

class Generator:

    def __init__(self,f:str,s:str,ts:int,optii:tuple,tp:int):
        
        self.faculty=f

        self.shift=s
        
        self.total_section=ts

        self.optii=optii

        self.tp=tp

        self.sub_dict={
        'Science':['Mechanics-I','Thermodynamics','Optics','GPA-I','GPA-II',
        'Inorganic','Literature','Grammar','Nepali','Electrostatics','Mechanics-II',
        'Organic','Calculas','Algebra','Geometery'],
        
        'Management':['Account','Economics','Nepali','Grammar','Literature'],
        
        'Law':['Constitutional Law','Jurispredunce','Procedrual Law','Nepali','Social','English'],

        'optii':['Computer','Biology','Hotel Management','B.Studies'],
        }

        self.dcord_dict={}

        self.lab_dict={}

        self._dcord()
        self.brks()
        self._lcord()

    def _dcord(self):
        dcord=[]

        count=0
        for i in range(7*self.total_section):
            if i!=7*count:
                for j in range(self.tp):
                    dcord.append((i,j))
            else:
                count+=1
        count=0
        for i in range(self.total_section):
            self.dcord_dict[self.shift+str(i+1)]=[dcord[i+count] for i in range(self.tp*6)]
            count+=self.tp*6

    def _lcord(self):
        lcord=[]

        checklist=[i for i in range(self.tp) if i%2!=0]#check list / break list
        if self.tp%2!=0:
            checklist.append(self.tp-1)

        for i in range(self.total_section):#making list of [i,list.index(i)+1]
            
            for j in self.dcord_dict[self.shift+str(i+1)]:
                try:
                    
                    if self.faculty=='Science' and i>self.optii[0]:
                        checklist.append(2)
                    
                    if j[1] not in checklist:
                        lcord.append([j , self.dcord_dict[self.shift+str(i+1)]
                            [self.dcord_dict[self.shift+str(i+1)].index(j)+1]
                            ])

                except Exception:
                   continue
        count=0
        for i in range( self.total_section ):
            var=lcord[count : 6 * int(log(self.tp,2))*(i+1)]
            self.lab_dict[self.shift+str(i+1)]=var
            count+=6* int(log(self.tp,2))
        
    def brks(self):

        rng=self.total_section

        if self.faculty=="Science":
            for i in range(self.optii[0]+1,self.total_section):
                for j in self.dcord_dict[self.shift+str(i+1)]:
                    col,row=j
                    if row==3:
                        self.dcord_dict[self.shift+str(i+1)].pop(
                            self.dcord_dict[self.shift+str(i+1)].index(j))
                rng=self.optii[0]+1

        for i in range(rng):
            for j in self.dcord_dict[self.shift+str(i+1)]:
                col,row=j
                if row==4:
                    self.dcord_dict[self.shift+str(i+1)].pop(
                        self.dcord_dict[self.shift+str(i+1)].index(j))
        
    
    def gen_class(self,sec):
        if sec in  [i for i in self.dcord_dict.keys()]:
            shuffle(self.dcord_dict[sec])
            td=choice(self.dcord_dict[sec])
            
            self.dcord_dict[sec].pop(self.dcord_dict[sec].index(td))
            return td

    def gen_lab(self,sec):
        if sec in  [i for i in self.lab_dict.keys()]:
            shuffle(self.lab_dict[sec])
            ld=choice(self.lab_dict[sec])
            
            self.lab_dict[sec].pop(self.lab_dict[sec].index(ld))
            for i in ld:
                self.dcord_dict[sec].pop(self.dcord_dict[sec].index(i))
            return ld

a=Generator('Science','D',10,(3,14),2)