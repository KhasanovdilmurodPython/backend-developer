# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:26:42 2023

@author: User
"""
# a=1
# while a<=5:
#     print(a, end=',')
#     a+=1
# print("Sanoq tugadi")

savol = "Istalgan son kiriting "
savol +="(Dasturni to`xtatish uchun 'exit' deb yozing):>>>"
qiymat =''
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat!='exit':
#         print(int(qiymat)**2)

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora =False
#     else:
#         print(int(qiymat)**2)
# print("Dastur tugadi")

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(int(qiymat)**2)
# print("Dastur tugadi")

son =0

while son<=20:
    son+=1
    if son%3!=0:
        continue
    else:
        print(f"{son} ning kvadrati {son**2}")