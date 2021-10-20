from random import *

UNIQUE_CHAR = "!@#$%&*^-_=+/.><~ "
NORMAL_CHAR = "abcdefghijklmnopqrstuvwxyz"
CAPITAL_CHAR = NORMAL_CHAR.upper()
NUMBER = "0123456789"


def randomPassword():
    all = UNIQUE_CHAR + CAPITAL_CHAR + NORMAL_CHAR + NUMBER

    length = randint(8, 20)

    return "".join(sample(all, length))


class Cryptography:
    def __init__(self):

        self.All =[UNIQUE_CHAR, CAPITAL_CHAR, NORMAL_CHAR, NUMBER]

        self.mainValue = [iter_str for iter_list in self.All for iter_str in iter_list]
        self.mainKey = self.generate_key()

    def generate_key(self):
        lst = [iter_str for iter_list in self.All for iter_str in iter_list]
        lst[lst.index(' ')] = '|'
        shuffle(lst)
        return ''.join(lst)

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
            
            if count == 6: # skip 5 extra bit, decrypt the acutal letter, repate
                password += value[i]
                count = 0

        if hashword == password:
            return password

        else:
            return False