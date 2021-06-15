from random import * 

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

a=Generator('Science','D',18,(1,17),8)
count=0

for i in range(a.total_section):
    
    for j in a.dcord_dict[a.shift+str(i+1)]:
        try:
            print([j , a.dcord_dict[a.shift+str(i+1)][
                a.dcord_dict[a.shift+str(i+1)].index(j)+1
            ]])
        except Exception:
           continue