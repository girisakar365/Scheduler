from random import *

UNIQUE_CHAR = '!@#$%&*^-_=+|/.><~'
NORMAL_CHAR = 'abcdefghijklmnopqrstuvwxyz'
CAPITAL_CHAR = NORMAL_CHAR.upper()
NUMBER = '0123456789'

def randomPassword():
    all = UNIQUE_CHAR + CAPITAL_CHAR + NORMAL_CHAR + NUMBER
    
    length=randint(8, 20)
    
    return ''.join(sample(all, length)) 

class Cryptography:

    def __init__(self):
        
        self.All=[UNIQUE_CHAR, CAPITAL_CHAR, NORMAL_CHAR, NUMBER]

        self.mainValue=[i for a in self.All for i in a]
        self.mainKey=self.generate_key()

    def generate_key(self):
        shuffle(self.mainValue)
        return ''.join(self.mainValue)

    def specific_key(self,key):self.mainKey=key 
    
    def salt(self,lenght:int):
        password=''
        length=lenght
        for i in range(length):
            password+=choice(self.mainKey)
        return password


    def encrypt(self,password:str):
        key={key:value for key,value in zip(self.mainValue,self.mainKey)}
        cipher=''
        for i in password:
            cipher+=key[i]

        byte=(256-len(cipher))//2
        return self.salt(byte)+cipher+self.salt(byte)

    def decrypt(self,cipher:str,hashword:str):
        value={key:value for key,value in zip(self.mainKey,self.mainValue)}
        password=''
        
        byte=(256-(len(hashword)))//2
        for i in cipher[byte:byte+(len(hashword))]:
            password+=value[i]
                
        if hashword==password:
            return password
        else:
            return False