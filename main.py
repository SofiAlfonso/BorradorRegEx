import re
from codecs import*
from tkinter import*

def diccionario():
    palabras=[]
    begin = ord('a')
    print(begin)
    end = ord('z') + 1
    print(end)
    i = begin
    while i != end:
        caracter = chr(i)
        ruta= str(caracter)+".txt"
        try:
            abrir= open(ruta,'r', "utf-8")
            lineas = abrir.readlines()
            for linea in lineas:
                dividir = re.search(',', linea)
                if  dividir:
                    palabra = linea.split(',')
                    palabra2 = palabra[0][:len(palabra[0]) - 2] + palabra[1].lstrip().strip()
                    palabras.append(palabra[0])
                    palabras.append(palabra2)

                else:
                    palabra = linea.strip()
                    palabras.append(palabra)

            i += 1
        except FileNotFoundError:
            print("No se encontro el archivo " + str(caracter))
    return palabras


def Emogis(texto,pag):
    for e in range (0,2,1):
        if e==0:
            Caracteres = [";-;","<3","xD"]
            car=" emogis: "
            y=90
        #else:
            #Caracteres= diccionario()
            #print(Caracteres)
            #car= " palabras en español:"
            #y=110
        patron = ""
        for b in range(0, len(Caracteres), 1):
            if patron == "":
                patron = Caracteres[b]
            else:
                patron = patron + "|" + Caracteres[b]

        prueba = re.compile(patron)
        print(prueba.findall(texto))
        coincidencias = "Se encontraron "+ str(len(prueba.findall(texto)))+ car + str(prueba.findall(texto))
        mensaje = Label(pag, text=coincidencias)
        mensaje.pack()
        mensaje.place(x=50, y=y)

def Pagina():
    pag = Tk()
    tbox = Entry()
    tbox.place(x=50, y=50)
    enviar = Button(text="Envía tu frase", command=lambda: Emogis(tbox.get(), pag))
    enviar.place(x=50, y=70)
    pag.mainloop()



if __name__ == '__main__':
    Pagina()


