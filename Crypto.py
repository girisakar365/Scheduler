from random import *

try:
    from database import Password

except ImportError:
    from .database import Password

UNIQUE_CHAR = "!@#$%&*^-_=+/.><~ "
NORMAL_CHAR = "abcdefghijklmnopqrstuvwxyz"
CAPITAL_CHAR = NORMAL_CHAR.upper()
NUMBER = "0123456789"


def randomPassword():
    all = UNIQUE_CHAR + CAPITAL_CHAR + NORMAL_CHAR + NUMBER

    length = randint(10, 12)

    return "".join(sample(all, length))


class Cryptography:
    def __init__(self, password, process:str):

        self.All =[UNIQUE_CHAR, CAPITAL_CHAR, NORMAL_CHAR, NUMBER]

        self.mainValue = [iter_str for iter_list in self.All for iter_str in iter_list]
        
        if len(Password.fetch('00100100')) == 80:
            self.mainKey = Password.fetch('00100100')
        
        else: self.mainKey = self.generate_key()

        self.result = None

        if process == 'enc': 
            Password.insert('10100101',self.encrypt(password))
        
        elif process == 'dec':
            if password == self.decrypt(Password.fetch('10100101'), password):
                self.result = True
            else: self.result =  False

    def generate_key(self):
        lst = [iter_str for iter_list in self.All for iter_str in iter_list]
        lst[lst.index(' ')] = '|'
        shuffle(lst)
        return ''.join(lst)

    def specific_key(self):
        self.mainKey = self.generate_key()
        Password.insert('00100100', self.mainKey)
        return self.mainKey

    def salt(self, lenght: int):

        password = ""

        length = lenght

        for i in range(length):
            password += choice(self.mainKey)

        return password

    def encrypt(self, password: str):

        key = {k:v for k,v in zip(self.mainValue, self.mainKey)}

        cipher = ''
        
        for i in password:
            cipher += self.salt(5)
            cipher += key[i]

        byte = (256 - len(cipher)) // 2

        return self.salt(byte) + cipher + self.salt(byte)

    def decrypt(self, cipher: str, hashword: str):

        value = {k: v for k, v in zip(self.mainKey, self.mainValue)}

        password = ""

        byte = (256 - (len(hashword) * 6)) // 2 # position of actual pass: encrypted bit + 5 extra bits after every acutal bit.
        
        count = 0

        for i in cipher[byte:byte + (len(hashword)*6)]:# starting point : starting point + len of encrypted bit + 5 extra bit.

            count += 1
            
            if count == 6: # skip 5 extra bit, decrypt the acutal letter, repeat
                password += value[i]
                count = 0

        if hashword == password:
            return password

        else:
            return False