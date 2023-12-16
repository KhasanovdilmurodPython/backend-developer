# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:24:04 2023

@author: User
"""
# friends =[]

# n=1
# while True:
#     name = input(f"{n} - do`stingizni kiriting:\n>>>")
#     friends.append(name)
#     yangi = input("Yana do`stingizni kiritasizmi? (ha/yoq):\n>>>")
#     n+=1
#     if yangi !='ha':
#         break
# friends ={}

# flag = True
# while flag:
#     name = input("Do`stingizni ismini kiriting:\n >>>")
#     age =input(f"{name.title()}ning yoshini kiriting: \n>>>")
#     friends[name] =int(age)
#     yangisi =input("Yana do`stlaringizni bormi? (ha/yoq) \n>>>")
#     if yangisi!='ha':
#         flag =False
# for k,v in friends.items():
#     print(f"{k} {v} yoshda")
# phones = ['samsung','iphone','redmi','huawei','vivo','samsung']
# while 'samsung' in phones:
#         phones.remove('samsung')
# print(phones)

talabalar = ['olim','halim','salim','komil']

baholangan_talabalar = {}

while talabalar:
    talaba = talabalar.pop()
    baho =input(f"{talaba.title()}ning bahosini kiriting:\n >>>")
    baholangan_talabalar[talaba] = float(baho)
print(baholangan_talabalar)




















