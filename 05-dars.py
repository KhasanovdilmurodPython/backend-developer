# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 22:14:55 2023

@author: DeeLiKk
"""

# friends = [ "Ali","Vali","Husan","Hasan","Olim"]
# for friend in friends:
#     print(f"""Hurmatli {friend}, sizni 29-noyabr kuni el oshi
# dasturonimizga taklif etamiz.\nHurmat bilan Isarovlar xonadoni.""")
friends = []
# for n in range(5):
#     friends.append(input(f"{n+1} - do`stingizni ismini kiriting."))
# print(friends)
# ismlar = ["Anvar","Yanvar","Feruz","Jobir","Yobir"]
# for ism in ismlar:
#     print(f"Salom {ism}, qaley ishlar")
# print(f"Kod {len(ismlar)} marta takrorlandi")
t_sonlar = list(range(11,100,2))
for kub in t_sonlar:
    print(kub**3)
    if kub==21:
        break