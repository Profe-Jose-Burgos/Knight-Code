#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#libreria para bot en el telegram
import telebot 

#Variables para precios, envíos (beta) y asesoría de presupuestos (beta)
prod1 = "-Celulares."
prod2 = "-Book´s."
prod3 = "-Tablet´s."

cel1 = "-Galaxy Z Flip4 5G"
cel2 = "-Galaxy Z Fold4 5G"
cel3 = "-Galaxy S22 5G"
cel4 = "-Galaxy S22 Ultra 5G"
cel5 = "-Galaxy A53 5G"

celp1 = 999.99
celp2 = 1.919
celp3 = 799.99
celp4 = 919.99
celp5 = 429.00

book1 = "-Galaxy Book2 Pro 360"
book2 = "-Galaxy Book Go 5G"
book3 = "-Galaxy Book Flex2 Alpha"

bookp1 = 949.99
bookp2 = 609.99
bookp3 = 659.99

tab1 = "-Galaxy Tab A7 Lite"
tab2 = "-Galaxy Tab A8 WiFi"
tab3 = "-Galaxy Tab S6 Lite"
tab4 = "-Galaxy Tab S8 Ultra"

tabp1 = 134.00
tabp2 = 234.50
tabp3 = 274.97
tabp4 = 1.149




import re

import random



#definiciones necesarias para "despertar" del bot
def get_response(user_input):
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
        
        #respuestas secundarias pero primarias
        resp("¡Buenas! :)", ["hola", "buenas", "hello", "hey", "hi"], resp_unica = True)
        resp("Con muchos ánimos y feliz, ¿Usted?", ["como", "estas", "que", "tal", "onda"], resp_unica = True)
        resp("Es bueno saberlo. ¿Puedo hacer algo por usted?", ["bien", "genial", "mas", "o", "menos", "todo", "cool", "perfecto"], 
             resp_unica = True)
        resp("Espero mejore pronto... ¿Puedo hacer algo por usted?", ["mal", "terrible", "horrible", "enfermo"], resp_unica = True)
        
        #mercancia
        resp("Éstos son nuestros productos a disponibilidad por el momento, elija alguno: \n{} \n{} \n{}".format(
            prod1, prod2, prod3), ["productos", "mercancia", "producto", "mercancias"], resp_unica = True)
        resp("Éstos son nuestros modelos de celulares disponibles: \n{} \n{} \n{} \n{} \n{}\nSi gustas consultar los precios, menciona los dispositivos a consultar.".format(cel1, cel2, cel3, cel4, cel5),
            ["cel", "celular", "celulares", "telefono", "telefonos"], resp_unica = True)
        resp("Éstos son nuestros modelos de Book´s disponibles: \n{} \n{} \n{}".format(book1, book2, book3), ["book", "books", "computadoras", "muestrame"], resp_unica = True)
        resp("Éstos son nuestros modelos de Tablet´s disponibles: \n{} \n{} \n{} \n{}".format(tab1, tab2, tab3, tab4), 
             ["tableta", "tablet", "tablets"], resp_unica = True)
        
        #precios
        resp("El precio del {} es de {}$".format(cel1, celp1), ["flip", "galaxy", "samsung"], resp_unica = True)
        resp("El precio del {} es de {}$".format(cel2, celp2), ["fold", "galaxy", "samsung"], resp_unica = True)
        resp("El precio del {} es de {}$".format(cel3, celp3), ["s", "galaxy", "samsung"], resp_unica = True)
        resp("El precio del {} es de {}$".format(cel4, celp4), ["ultra", "galaxy", "samsung"], resp_unica = True)
        resp("El precio del {} es de {}$".format(cel5, celp5), ["a", "galaxy", "samsung"], resp_unica = True)
        
        resp("El precio del {} es de {}$".format(book1, bookp1), ["pro", "book"], resp_unica = True)
        resp("El precio del {} es de {}$".format(book2, bookp2), ["go", "book"], resp_unica = True)
        resp("El precio del {} es de {}$".format(book3, bookp3), ["flex", "alpha", "book"], resp_unica = True)
        
        resp("El precio del {} es de {}$".format(tab1, tabp1), ["tab", "lite"], resp_unica = True)
        resp("El precio del {} es de {}$".format(tab2, tabp2), ["tab", "wifi"], resp_unica = True)
        resp("El precio del {} es de {}$".format(tab3, tabp3), ["tab", "lite", "s"], resp_unica = True)
        resp("El precio del {} es de {}$".format(tab4, tabp4), ["tab", "ultra"], resp_unica = True)
        
        #lista de carrito de compras (beta)
        
        
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(cel1), ["reserva", "carrito", "compras", "wishlist", "flip"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(cel2), ["reserva", "carrito", "compras", "wishlist", "fold"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(cel3), ["reserva", "carrito", "compras", "wishlist", "s"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(cel4), ["reserva", "carrito", "compras", "wishlist", "ultra"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(cel5), ["reserva", "carrito", "compras", "wishlist", "a"], resp_unica = True)
        
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(book1), ["reserva", "carrito", "compras", "wishlist", "pro", "book"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(book2), ["reserva", "carrito", "compras", "wishlist", "go", "book"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(book3), ["reserva", "carrito", "compras", "wishlist", "flex", "book"], resp_unica = True)
        
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(tab1), ["reserva", "carrito", "compras", "wishlist", "lite", "tab"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(tab2), ["reserva", "carrito", "compras", "wishlist", "wifi", "tab"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(tab3), ["reserva", "carrito", "compras", "wishlist", "lite", "s", "tab"], resp_unica = True)
        resp("¡Perfecto! Añadido el {} al carrito de compras.".format(tab4), ["reserva", "carrito", "compras", "wishlist", "ultra" "tab"], resp_unica = True)
        
        match = max(alta_prob, key = alta_prob.get)

        return unknown() if alta_prob[match] < 1 else match

def unknown():
    resp = ["No sé a qué te refieres.", "Repítemelo, por favor.", "No te entiendo."][random.randrange(3)]
    return resp

#Reservas y envío de pedidos (beta)
#import pandas as pd

#def append_row(df, row):
#    return pd.concat([
#                df, 
#                pd.DataFrame([row], columns=row.index)]
#           ).reset_index(drop=True)

#df = pd.DataFrame(columns=('Fecha', 'Nombre'))
#new_row = pd.DataFrame(columns=('2022-12-20','Jackie'))

#df = append_row(df, new_row)

token = "5886565999:AAGfJKf808zpwMHR2Qg6XDSXlltpGxVBQJA"


# In[2]:


bot = telebot.TeleBot(token)


# In[3]:


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


# In[4]:


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    
    response = get_response(message.text)
    bot.reply_to(message, response)
    print(f'Mensaje para usuario BOT : {response}')
    print(f'mensaje de Usuario: {message.text}')


# In[ ]:


bot.infinity_polling()


# In[ ]:




