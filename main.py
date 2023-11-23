import re
from codecs import*
from tkinter import*
from PIL import Image, ImageTk


pag = Tk()
tbox = Entry()
tbox.place(x=50, y=50)
enviar = Button(text="Envía tu frase", command=lambda: Emogis(tbox.get()))
enviar.place(x=50, y=70)

def diccionario(caracter):

    palabras=[]
    ruta= "Diccionario/"+caracter+".txt"
    try:
        abrir= open(ruta,'r', "utf-8")
        lineas = abrir.readlines()
        for linea in lineas:
            dividir = re.search(',', linea)
            if  dividir:
                palabra = linea.split(',')
                palabra2 = palabra[0][:len(palabra[0]) - 2] + palabra[1].lstrip().strip() #Creo las palabras que van en masculino y femenino por aparte
                num = re.search("[0-9]", palabra[0]) #Busco y elimino números dentro de las palabras
                if num != None:
                    palabra[0] = palabra[0].replace(num[0], '', 1)
                num1 = re.search("[0-9]", palabra2)
                if num1 != None:
                    palabra2 = palabra2.replace(num1[0], '', 1)

                palabras.append(palabra[0])
                palabras.append(palabra2)

            else:
                palabra = linea.strip()
                num=re.search("[0-9]",palabra)
                if num!=None:
                    palabra=palabra.replace(num[0], '',1)
                palabras.append(palabra)

    except FileNotFoundError:
        return "4r1hjlksthpuv" #Patrón cualquiera poco probable de estar en la cadena, así se clasificará al carácter como no identificado

    #ordenamiento
    n= len(palabras)

    for i in range(n-1):
        for j in range( n-1-i):
            if len(palabras[j])< len(palabras[j+1]):
                palabras[j], palabras[j+1]= palabras[j+1], palabras[j]


    patron=""
    for a in range(0,len(palabras),1):
        if patron=="":
            patron=palabras[a]
        else:
            patron= patron +"|" + palabras[a]
    return patron

def impemogis(emogi,pos):
    if emogi== "\\m/":
        emogi= "\\\\m/"
    Imagenes={":)":"png/feliz.png", ":(":"png/triste.png", ":D":"png/Gran_sonrisa.png", ";)":"png/guino.png", ":P":"png/lengua.png","xD":"png/risa.png",":-)":"png/Feliz1.png", ":-(":"png/triste2.png", "(y)":"png/pulgararriba.png", "(n)":"png/pulgarabajo.png", "<3":"png/corazon.png","\\\\m/":"png/manocachos.png",":-O":"png/sorpresa.png", ":O":"png/sorpresa2.png",":-|":"png/Indiferente.png",":|":"png/Indiferente2.png",":*":"png/beso.png", ">:(":"enojado.png", "^^":"png/ojossonrientes.png",":-]":"png/feliz2.png"}
    ruta=Imagenes[emogi]
    img= Image.open(ruta)
    nimg= img.resize((50,50))
    render= ImageTk.PhotoImage(nimg)
    img1= Label(pag,image= render)
    img1.image= render
    img1.place(x=pos,y=230)


def enpantalla(texto,emogis,palabras,nulos):
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

    print(patron)
    partes= re.split(patron,texto)

    pos= 50
    for mensajes in partes:
        if mensajes != '':
            if mensajes in emogis:
                pos=pos+5
                impemogis(mensajes,pos)
                pos= pos + 60
            else:
                mostrar = Label(pag, text=mensajes)
                mostrar.pack()
                mostrar.place(x=pos, y=250)
                pos= pos+ (len(mensajes)*10)

def dic(texto,original,resultado):
    print(texto)
    coincidencias=[]
    nocoincide=[]
    texto= texto.replace(" ", '')
    while len(texto)!=0:
        inicio = str(texto[0]).lower()
        patron=diccionario(inicio)
        encontradas= re.findall(patron,texto.lower())


        if len(encontradas)!=0 and (type(encontradas[0])== str):

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
            mostrar2.place(x=50, y=130)
    enpantalla(original,resultado,coincidencias,nocoincide)


def Emogis(texto):
    original = texto
    prueba = re.compile(":\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-]")
    resultado=prueba.findall(texto)
    print(resultado)
    coincidencias = "Se encontraron "+ str(len(resultado))+ " emogis: "+ str(resultado)
    mensaje = Label(pag, text=coincidencias)
    mensaje.pack()
    mensaje.place(x=50, y=90)
    for i in range(0,len(resultado),1):
        texto= texto.replace(resultado[i],'', 1)
    if "\\" in texto:
        texto = texto.replace("\\", '')
    dic(texto,original,resultado)



pag.mainloop()










