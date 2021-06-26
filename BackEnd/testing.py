from random import *
from DataBase.main import DB
class DataGen:
    def id_gen():
        capitalChar = 'abcdefghijklmnopqrstuvwxyz'.upper()
        number = '0123456789'
        all = capitalChar+number
        return ''.join(sample(all,5))  

    def gen_data(limit:int=27):
        name = ['Uttam Raj','Ram','Shyam', "Hari", 'Samip', 'Varun', 'Bardan' ,
                'Ashutosh', 'Darwin', 'Bikalpa', 'Swostik', 'Sanshkar',
                'Abiyan', 'Dev','Nagendra','Bhola','Rajesh','Prakash','Dash','Rikesh','Devendra',
                'Uttam','Ankit','Pratik']
        
        sname=['Bhusal','Arayal','Galwali','Arayal','Ghimire','Shrestha', 'Ghimire','Sharma','Acharya', 'Giri', 'Nepal', 'Kharel','Kadel',
            'Barma','Timalsina','Poudle','Panthi','Tiwari','Pudasini','Niraula',
            'Maharjan']
        
        data_lst=[]

        for i in range(limit):

            fristName=choice(name)
            secondName=choice(sname)
            email=fristName.lower().capitalize()+secondName.lower()+'@gmail.com'
            id=DataGen.id_gen()
            SUBJECT='Physics'
            _class=choice(['11','12','both'])

            data_lst.append([fristName,secondName,id,SUBJECT,email,_class])

        return data_lst