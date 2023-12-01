# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Tue Nov 28 10:34:34 2023

@author: User
"""
# phones = {
#     "ali": "galaxy s21",
#     "dilmurod": "iphone 12",
#     "halim": "huawei",
#     "ravshan": "galaxy a02"
#     }
# print(phones.items())
# print(phones.keys())
# print(phones.values())
# for key, value in phones.items():
#     print(f"Key: {key.title()}")
#     print(f"Value: {value.title()}" + "\n")
# my_phones  = ["iphone 12","nokia 2210","huawei"]
# for phone in phones.values():
#     if phone in my_phones:
#         print(f"Listdagi telefonlar ichida \
#               menda borlari: {phone.title()}")
# for phone in sorted(phones):
#     print(phone)
# fan = set(phones)
# print(fan)
# python1 = {
#     "boolean":"mantiqiy tur",
#     "integer":"butun son",
#     "for":"sikl operatori",
#     "while":"sikl operatori",
#     "if":"shart operatori",
#     "opencv":"computer vision sohasi kutubxonasi"
    
#     }
# # for key,value in python1.items():
# #     print(f"{key.capitalize()} - {value.capitalize()}")
# print(python1[input("Qaysi operator izohini bilishni xohlaysiz? \n>>>")].capitalize())
menu  = {
    "manti": 25000,
    "lag`mon": 22000,
    "lavash": 30000,
    "gulxonim": 20000,
    "somsa": 5000,
    "chuchvara": 25000,
    "jiz": 35000,
    "sho`rva": 18000
    }
list1 =[]
print("3 ta taom buyurtma bering:")
for x in range(3):
    list1.append(input(f"{x+1} - taom   \n>>>"))
    
    
for y in list1:
    if y in menu:
        print(f"{y} -  {menu[y]} so`m")
    else:
        print(f"Kechirasiz, bizda {y} yo`q ")
