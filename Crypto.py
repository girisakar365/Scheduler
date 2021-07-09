from random import *

def randomPassword():

    uniqueChar = '!@#$%&*'
    capitalChar = 'abcdefghijklmnopqrstuvwxyz'.upper()
    normalChar = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    all = uniqueChar+capitalChar+normalChar+number
    
    length=randint(8,20)
    
    return ''.join(sample(all,length)) 

class Cryptography:
    
    uniqueChar = '!@#$&-_.%<*>?;:+=~/^ '
    capitalChar = 'abcdefghijklmnopqrstuvwxyz'.upper()
    normalChar = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    All=[uniqueChar,capitalChar,normalChar,number]


    mainKey='-:+F@QKTWRC~nciPMjqwBSE28vshpfgy#xrLU$.=1_bao7%^?/ZXO!>GIJ<&;3mVDdl*z906tkue5Y4NAH|'
    mainValue=[i for a in All for i in a]

    def key_generator():
        mainValue=[i for a in Cryptography.All for i in a]
        
        shuffle(mainValue)
        key=''
        for i in mainValue:
            key+=i
        
        return key

    def salt(lenght:int):
        shuffle(Cryptography.All)
        password=''
        length=lenght
        for i in range(length):
            choose=choice(Cryptography.All)
            password+=choice(choose)
        return password


    def encrypt(password:str):
        key={key:value for key,value in zip(Cryptography.mainValue,Cryptography.mainKey)}
        cipher=''
        for i in password:
            cipher+=Cryptography.salt(5)
            cipher+=key[i]

        byte=int((256-len(cipher))/2)
        return Cryptography.salt(byte)+cipher+Cryptography.salt(byte)

    def decrypt(cipher:str,hashword:str):
        value={key:value for key,value in zip(Cryptography.mainKey,Cryptography.mainValue)}
        password=''
        count=0
        
        byte=int((256-(len(hashword)*6))/2)
        for i in cipher[byte:byte+(len(hashword)*6)]:
            count+=1
            if count==6:
                password+=value[i]
                count=0
                
        if hashword==password:
            return password
        else:
            return False

def test(typ:str=None):                
    from Textography import txt

    def auto():
        count=0
        while True: 
            from time import sleep 

            password=randomPassword()
            cipher=Cryptography.encrypt(password)
            count+=1
            print()
            print("Orginal Password: "+password)
            print()
            print('Encrypted Password: '+cipher)
            print()
            print('Decrypted Password: '+Cryptography.decrypt(cipher,password))
            print()
            print(count)
            sleep(2)

    def manual():
            password=str(input('>>> '))
            cipher=Cryptography.encrypt(password)
            print('Encrypted: '+cipher)
            print()
            pascode=str(input('Your password: '))
            print()
            print("Decrypted:",Cryptography.decrypt(cipher,pascode))

    if typ=='auto':
        auto()
    elif typ=='manual':
        manual()

