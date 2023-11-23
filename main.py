import re #Expresiones regulares
from codecs import*
from tkinter import* #Creación de la página
from PIL import Image, ImageTk #Manejo de imagenes

#Creo la página
pag = Tk()
pag.title("Proyecto Final Lenguajes de Programación")
pag.iconbitmap("Escudo_Universidad_EAFIT.ico")
pag.geometry('500x500')
pag.resizable(height=False,width=False)
pag.config(background="black")

#Imagen de la uni
logo= Image.open("logo_eafit_completo.png")
logo2= logo.resize((150,100))
render1= ImageTk.PhotoImage(logo2)
show= Label(pag,image= render1)
show.place(x=0, y=0)

#Título de la página
titulo= Label(pag,text="Proyecto Final Lenguajes", bg="black",font=('Times New Roman',25) , fg= "white")
titulo.place(x=160, y=30)

#Cuadro de texto
tbox = Entry()
tbox.place(x=280, y=90)
tbox.config(width=30,fg="black")
label1= Label(pag, text="Ingrese su frase: ", bg="black",fg="white", font=('Times New Roman', 10))
label1.place(x=180, y=90)

#Botón
enviar = Button(text="Procesar", command=lambda: Emogis(tbox.get()))
enviar.config(bg="midnight blue",font=('Times New Roman',12),fg="white")
enviar.place(x=180, y=120)

#Busca el archivo del diccionario con la letra enviada, si no lo encuentra asume que el caracter no está en español
def diccionario(caracter):
    #Crea una lista con las palabras del archivo cargado (sin números, parentesis ni espacios al final y/o inicio)
    palabras=[]
    ruta= "Diccionario/"+caracter+".txt"
    #Busca el archivo, lo codifica y lo abre
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
    #ordena las palabras de la de mayor longitud a la de menor (garantiza que la expresión regular encuentre la palabra más larga que coincida)
    n= len(palabras)
    for i in range(n-1):
        for j in range( n-1-i):
            if len(palabras[j])< len(palabras[j+1]):
                palabras[j], palabras[j+1]= palabras[j+1], palabras[j]
    #Se crea el patrón que se utilizrá dentro de la expresión regular
    patron=""
    for a in range(0,len(palabras),1):
        if patron=="":
            patron=palabras[a]
        else:
            patron= patron +"|" + palabras[a]
    return patron

#Muestra en pantalla la imagén correspondiente a los emogis ingresados
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
    img1.place(x=pos,y=345)

#Muestra en pantalla el texto ingresado
def enpantalla(texto,emogis,palabras,nulos):
    #subtitulo para la frase
    label2= Label(pag, text="SU FRASE ES",fg="midnight blue",bg="black", font=('Times New Roman', 15))
    label2.place(x=190, y=280)
    #El patron está conformado por los emogis, las palabras encontradas y los caracteres que no coinciden con el español
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
    #Separa el texto original en las palabras y emogis antes mencionados y los muestra en pantalla
    partes= re.split(patron,texto)
    pos= 30
    for mensajes in partes:
        if mensajes != '':
            if mensajes in emogis:
                pos=pos+5
                impemogis(mensajes,pos)
                pos= pos + 60
            else:
                mostrar = Label(pag, text=mensajes, fg="white", bg="black", font=('Times New Roman', 12))
                mostrar.place(x=pos, y=350)
                pos= pos+ (len(mensajes)*10)

#Se encarga de encontrar y guardar las palabras que coinciden con alguna del diccionario y las que no
def dic(texto,original,resultado):
    print(texto)
    coincidencias=[]
    nocoincide=[]
    texto= texto.replace(" ", '')
    #Se busca dentro del texto que ya no contiene emogis, se toma el primer caracter para buscar el archivo que le corresponda en el diccionario
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
        #Se muestra en pantalla las palabras encontradas y las que no coinciden
        mensaje= "Se encontraron "+ str(len(coincidencias))+ " palabras en español: "+ str(coincidencias)
        mostrar= Label(pag, text=mensaje, fg= "white", bg="black", font=('Times New Roman', 12))
        mostrar.place(x=20, y=200)
        if len(nocoincide)>0:
            mensaje2= "Se encontraron "+ str(len(nocoincide))+ " palabras que no coinciden con el español: "+ str(nocoincide)
            mostrar2 = Label(pag, text=mensaje2,fg= "white", bg="black", font=('Times New Roman', 12))
            mostrar2.place(x=20, y=220)
    enpantalla(original,resultado,coincidencias,nocoincide)

#Encuentra los emogis dentro del texto y se imprimen en pantalla
def Emogis(texto):
    original = texto
    prueba = re.compile(":\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-]")
    resultado=prueba.findall(texto)
    coincidencias = "Se encontraron "+ str(len(resultado))+ " emogis: "+ str(resultado)
    mensaje = Label(pag, text=coincidencias, fg= "white", bg="black", font=('Times New Roman', 12))
    mensaje.place(x=20, y=180)
    #Se eliminan los emogis encontrados para pasar a encontrar las palabras
    for i in range(0,len(resultado),1):
        texto= texto.replace(resultado[i],'', 1)
    #Se eliminan los backslash sobrantes (estos causan error en el patrón) a veces son producidos por el emogi '\\m/'
    if "\\" in texto:
        texto = texto.replace("\\", '')
    dic(texto,original,resultado)

pag.mainloop()










