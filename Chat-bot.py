#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

import random

def obt_resp(user_input):
    split_msg = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    resp = check_msg(split_msg)
    return resp

def prob_msg(user_msg, plbs_conocidas, resp_unica = False, plbs_necesarias = []):
    fij_msg = 0
    tiene_plbs_necesarias = True

    for plb in user_msg:
        if plb in plbs_conocidas:
            fij_msg += 1

    validez = float(fij_msg) / float (len(plbs_conocidas))

    for plb in plbs_necesarias:
        if plb not in user_msg:
            tiene_plbs_necesarias = False
            break
    if tiene_plbs_necesarias or resp_unica:
        return int(validez * 100)
    else:
        return 0

def check_msg(msg):
        alta_prob = {}

        def resp(resp_bot, lst_plbs, resp_unica = False, plbs_necesarias = []):
            nonlocal alta_prob
            alta_prob[resp_bot] = prob_msg(msg, lst_plbs, resp_unica, plbs_necesarias)

        resp("¡Buenas! :)", ["hola", "buenas", "hello", "hey", "hi"], resp_unica = True)
        resp("Con muchos ánimos y feliz, ¿Usted?", ["como", "estas", "que", "tal", "onda"], resp_unica = True)
        resp("Es bueno saberlo. ¿Puedo hacer algo por usted?", ["bien", "genial", "mas", "o", "menos", "todo", "cool", "perfecto"], resp_unica = True)
        resp("Espero mejore pronto... ¿Puedo hacer algo por usted?", ["mal", "terrible", "horrible", "enfermo", "un", "poco", "algo", "tanto"], resp_unica = True)

        match = max(alta_prob, key = alta_prob.get)
        #print(highest_prob)

        return unknown() if alta_prob[match] < 1 else match

def unknown():
    resp = ["No sé a qué te refieres.", "Realmente no lo sé", "Hm... Internet podría ayudarte."][random.randrange(3)]
    return resp

while True:
    print("Bot: " + obt_resp(input('You: ')))


# In[ ]:




