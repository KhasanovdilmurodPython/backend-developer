# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:13:45 2023

@author: User
"""

# talaba = {
#     'yosh': 28,
#     "ism": 'alniyoz',
#     'kurs':3,
#     'baho':4,
#     'manzil':'Jizzax viloyati, zafarobod tumani, nurafshon mahalla'
#     }
# print(talaba.values())
car0 = {
        'model':"nexia",
        "rang":"oq",
        "yil": 2016,
        "km": 16000,
        'karobka':"avtomat"
        }
car1 = {
        'model':"lacetti",
        "rang":"sariq",
        "yil": 2020,
        "km": 23000,
        'karobka':"avtomat"
        }
car2 = {
        'model':"nexia 3",
        "rang":"oq",
        "yil": 2013,
        "km":42000,
        'karobka':"mexanika"
        }
car3 = {
        'model':"tahoe",
        "rang":"qora",
        "yil": 2021,
        "km": 10000,
        'karobka':"avtomat"
        }
# car =car3
# print(f"{car['model'].title()}, {car['yil']} - yil, {car['rang']} rang"  )
cars = [car0,car1,car2,car3]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['yil']}-yil,"
#           f"{car['rang']} rang")
gentras = []
for n in range(10):
    new_car = {
            'model':"Gentra",
            "rang":None,
            "yil": 2020,
            'narx':None,
            "km": 0,
            'karobka':"avtomat"
            }
    gentras.append(new_car)

for gentra in gentras[:3]:
    gentra['rang']='qizil'

for gentra in gentras[3:6]:
    gentra['rang']='qora'
    
# for gentra in gentras:
#     print(gentra)
for gentra in gentras[6:]:
    gentra['rang']='qora'
    gentra['karobka'] = 'mexanika'
    
# for gentra in gentras:
#     print(gentra)  
for gentra in gentras:
    if gentra['karobka'] == 'avtomat':
        gentra['narx'] = 15000
    else:
        gentra['narx'] = 13500
# for gentra in gentras:
#     print(gentra)

dasturchilar = {
    'ali': ['sql','c#','python'],
    'g`ani': ['c++','python','javascript'],
    'soli': ['sql','java','r'],
    'chori':['golang','c++','c','c#']
    }
# for ism, tillar in dasturchilar.items():
#     print(f"{ism.title()} quyidagi dasturlash tillarida dastur yoza oladi:")
#     for til in tillar:
#         print('-', til.upper())
hamkasblar = {
    'dilmurod': {
        'familya':'xasanov',
        'tyil': 1995,
        'malumot':'oliy',
        'tillar': ['php','python','sql']
        },
    'ravshan': {
        'familya':'shirinboyev',
        'tyil':1997,
        'malumot':'oliy',
        'tillar':['html','css','js']        
        },
    'maruf': {
        'familya':'tojiyev',
        'tyil': 1992,
        'malumot': 'oliy',
        'tillar':['python','c++','c#']
        }
    
    }

for ism, info in hamkasblar.items():
    print(f" {ism.title()} {info['familya'].title()},"
          f"{info['tyil']}-yilda tug'ilgan."
          f"Ma'lumoti: {info['malumot'].title()}."
          f" Quyidagi dasturlash tillarida dastur yoza oladi:"
          
          )
    for til in info['tillar']:
        print(f"-{til.upper()}")