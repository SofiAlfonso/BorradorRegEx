import re
from codecs import*
from tkinter import*

def diccionario(caracter):
    print(caracter)
    palabras=[]
    ruta= "Diccionario/"+caracter+".txt"
    try:
        abrir= open(ruta,'r', "utf-8")
        lineas = abrir.readlines()
        for linea in lineas:
            dividir = re.search(',', linea)
            if  dividir:
                palabra = linea.split(',')
                palabra2 = palabra[0][:len(palabra[0]) - 2] + palabra[1].lstrip().strip()
                num = re.search("[0-9]", palabra[0])
                if num != None:
                    palabra[0] = palabra[0].replace(num[0], '', 1)
                num1 = re.search("[0-9]", palabra2)
                if num != None:
                    palabra2 = palabra2.replace(num[0], '', 1)

                palabras.append(palabra[0])
                palabras.append(palabra2)

            else:
                palabra = linea.strip()
                num=re.search("[0-9]",palabra)
                if num!=None:
                    palabra=palabra.replace(num[0], '',1)
                palabras.append(palabra)


    except FileNotFoundError:
        print("No se encontro el archivo " + caracter)

    #ordenamiento
    n= len(palabras)

    for i in range(n-1):
        for j in range( n-1-i):
            if len(palabras[j])< len(palabras[j+1]):
                palabras[j], palabras[j+1]= palabras[j+1], palabras[j]

    print(palabras)
    patron=""
    for a in range(0,len(palabras),1):
        if patron=="":
            patron=palabras[a]
        else:
            patron= patron +"|" + palabras[a]
    return patron

def enpantalla(texto,emogis,palabras,nulos,pag):
    print("ya")
    patron= "(:\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-]"

    for i in palabras:
        if patron == "":
            patron = i
        else:
            patron = patron + "|" + i
    for i in nulos:
        if patron == "":
            patron = i
        else:
            patron = patron + "|" + i
    patron= patron + ")"


    partes= re.split(patron,texto)

    pos= 50
    for mensajes in partes:
        if mensajes != '':
            if mensajes in emogis:
                #impemogis(mensajes)
                mostrar = Label(pag, text= ":)")
                mostrar.pack()
                mostrar.place(x=pos, y=250)
                pos= pos + 50
            else:
                mostrar = Label(pag, text=mensajes)
                mostrar.pack()
                mostrar.place(x=pos, y=250)
                pos= pos+ (len(mensajes)*10)








def dic(texto, pag,original,resultado):
    coincidencias=[]
    nocoincide=[]
    texto= texto.replace(" ", '')
    while len(texto)!=0:
        inicio = str(texto[0]).lower()
        patron=diccionario(inicio)
        encontradas= re.findall(patron,texto.lower())

        if len(encontradas)!=0 and (type(encontradas[0])== str):
            print(encontradas[0])
            coincidencias.append(encontradas[0])
            texto= texto.lower().replace(encontradas[0],'',1)
        else:
            nocoincide.append(inicio)
            texto= texto.lower().replace(inicio,'',1)

        mensaje= "Se encontraron "+ str(len(coincidencias))+ " palabras en español: "+ str(coincidencias)
        mostrar= Label(pag, text=mensaje)
        mostrar.pack()
        mostrar.place(x=50, y=110)
        if len(nocoincide)>0:
            mensaje2= "Se encontraron "+ str(len(nocoincide))+ " palabras que no coinciden con el español: "+ str(nocoincide)
            mostrar2 = Label(pag, text=mensaje2)
            mostrar2.pack()
            mostrar2.place(x=50, y=190)
    enpantalla(original,resultado,coincidencias,nocoincide,pag)


def Emogis(texto,pag):
    original = texto.lower()
    prueba = re.compile(":\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-]")
    resultado=prueba.findall(texto)
    coincidencias = "Se encontraron "+ str(len(resultado))+ " emogis"+ str(resultado)
    mensaje = Label(pag, text=coincidencias)
    mensaje.pack()
    mensaje.place(x=50, y=90)
    for i in range(0,len(resultado),1):
        texto= texto.replace(resultado[i],'', 1)
    dic(texto,pag,original,resultado)

def Pagina():
    pag = Tk()
    tbox = Entry()
    tbox.place(x=50, y=50)
    enviar = Button(text="Envía tu frase", command=lambda: Emogis(tbox.get(), pag))
    enviar.place(x=50, y=70)
    pag.mainloop()



if __name__ == '__main__':
    Pagina()






