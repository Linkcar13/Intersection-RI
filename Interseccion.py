import os
import time


# Definición de Colores

black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"


#Barra de progreso
def progress_bar(progreso,total):
    porcentaje = 100 * (progreso/float(total))
    barra = (f'''{bblue}|'''*int(porcentaje) + f'''{bblue}.''' * (100 - int(porcentaje)) )
    print (f'''\r{bblue}[{barra}]{porcentaje:.2f}%''',end='''\r''')
#Carga para interfaz    
def cargando():
    i = 1
    carga = 3
    for i in range(carga):
        time.sleep(2)
        progress_bar(i+1,carga)

#Funcipon De Búsqueda e Intersección

def intersection (terminos,dic = {1: "verde que te quiero verde", 2: "verde viento", 3: "verde ramas", 4: "la higuera frota su viento"}):

    respuesta = {}
    p1 = 0
    p2 = 0
    auxlist=[]
    listas = []
    #print (f'''\n{listas}''')
    for t in terminos:
        #print (f'''\n {t}''')
        for i in dic:
            #print (f'''\n {i}''')
            if ((str(t) in dic.get(i)) and str.count(dic[i],str(t))!=0):
                auxlist.append(i)
                #p1 = p1 + 1
        listas.append (auxlist)
        auxlist = []        
        print (f'''{green}\n \n[✓]lista de docs para el termino {t}:''')    
        print (f'''{green}[✓]{listas[p2]}''')
        p2 = p2 + 1
        #p1 = 1
   
    #Se realiza la intersección de las 2 listas y se tira los 2 documentos como resultado
    for p in range(len(listas)):
        if (len(respuesta)==0):
            respuesta = [value for value in listas[p-1] if value in listas[p]]
        else:
            respuesta = respuesta + [value for value in respuesta if value in listas[p-1]]
            respuesta = respuesta + [value2 for value2 in respuesta if value2 in listas[p]]
            respuesta = respuesta + [value for value in listas[p-1] if value in listas[p]]
            resp = []
            [resp.append(value) for value in respuesta if value not in resp]   
    print (f'''{bgreen}\n[#] Resultados de la busqueda los documentos: {resp}''')
#Banner del Programa

baner = f'''
{bcyan}88                                                                                          88                          
{bcyan}88                ,d                                                                 ,d     ""                          
{bcyan}88                88                                                                 88                                 
{bcyan}88  8b,dPPYba,  MM88MMM  ,adPPYba,  8b,dPPYba,  ,adPPYba,   ,adPPYba,   ,adPPYba,  MM88MMM  88   ,adPPYba,   8b,dPPYba, 
{bcyan}88  88P'   `"8a   88    a8P_____88  88P'   "Y8  I8[    ""  a8P_____88  a8"     ""    88     88  a8"     "8a  88P'   `"8a
{bgreen}88  88       88   88    8PP"""""""  88           `"Y8ba,   8PP"""""""  8b            88     88  8b       d8  88       88
{bgreen}88  88       88   88,   "8b,   ,aa  88          aa    ]8I  "8b,   ,aa  "8a,   ,aa    88,    88  "8a,   ,a8"  88       88
{bgreen}88  88       88   "Y888  `"Ybbd8"'  88          `"YbbdP"'   `"Ybbd8"'   `"Ybbd8"'    "Y888  88   `"YbbdP"'   88       88
{" "*120}   {yellow}Version v1.0.0
{" "*125}   {bpurple}[By Linkcar]
'''

print(baner)


print(f'''\n{blue}[+] Cargando Documentos:\r\r''')
cargando()
print (f'''\n{blue}[+] Indexando Documentos en el Diccionario:\r\r''')
dicionario = {'1': "verde que te quiero verde", '2': "verde viento", '3': "verde ramas", '4': "la higuera frota su viento"}
cargando()
print(f'''{blue}{dicionario}''')
print(f'''\n{yellow}[*] Ingrese los Terminos para la búsqueda:\r\r''')
print(f'''\n{red}[x] Escriba exit si desea dejar de agregar terminos\r\r''')
#Ideado para agregar un bucle de terminos
count_T=1
terminos = []
t1=""
while t1!="exit":
    t1 = input(f'''{yellow}[*] Termino {count_T}:''')
    terminos.append(t1)
    count_T = count_T + 1

terminos.pop()    
#print (terminos[0])
print(f'''\n{blue}[:)] Realizando la Busqueda espere:\r\r''')
os.system("sleep 1")
cargando()
intersection(terminos,dicionario)




    



