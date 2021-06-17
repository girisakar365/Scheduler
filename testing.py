from random import *
teacher=['Uttam Raj Bhusal','Nagendra Arayal','Bhola Galwali',
         'Rajesh Shrestha', 'Prakash Ghimire','Rikesh Sharma',
         'Dash Barma','Ram Hari Shankar','Uttam Arayal']

name = ['Ram','Shyam', "Hari", 'Samip', 'Varun', 'Bardan' ,
        'Ashutosh', 'Darwin', 'Bikalpa', 'Swostik', 'Sanshakar',
        'Abiyan', 'Dev']

sname=['Ghemire','Acharya', 'Giri', 'Nepal', 'Kharel','Kadel',
       'Timalsina','Poudle','Panthi','Tiwari','Pudasini','Niraula',
       'Maharjan']

for i in range(100):
    teacher.append(choice(name)+' '+choice(sname))
    
def id_gen():
    capitalChar = 'abcdefghijklmnopqrstuvwxyz'.upper()
    number = '0123456789'
    all = capitalChar+number
    return ''.join(sample(all,5))  

nt=''
count=0
for j in teacher:
    for i in j.split(' '):
        nt+=i.lower()
    count+=1
    print('Acount No:'+str(count))
    print('Name: '+j)
    print('Email: '+nt+'@gmail.com')
    print('id: '+id_gen())
    _class=choice(['both','11','12'])
    print('Classes Handeled: '+_class)
    print()
    nt=''

    

