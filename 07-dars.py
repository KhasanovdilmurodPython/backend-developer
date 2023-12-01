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
for gentra in gentras:
    print(gentra)

